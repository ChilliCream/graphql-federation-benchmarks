"""Static consistency tests: workflow, docs, scripts and results.

These guard the .NET-only setup assumptions shared across the workflow,
local runner scripts, result generation and documentation.
"""

import glob
import os
import subprocess
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORKFLOW = os.path.join(REPO_ROOT, ".github", "workflows", "benchmark.yml")
README = os.path.join(REPO_ROOT, "README.md")
BENCHMARK_SH = os.path.join(REPO_ROOT, "k6", "benchmark.sh")
GENERATE_RESULTS = os.path.join(REPO_ROOT, "k6", "generate-results.py")
BUILD_MATRIX = os.path.join(REPO_ROOT, "k6", "build-matrix.py")

# Retired spec slug, built without embedding it verbatim: this file itself is
# scanned by the tracked-files regression test below, so a literal would
# flag the guard's own source once tests/ is tracked.
RETIRED_SPEC_SLUG = "composite" + "-schemas-" + "spec"


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.workflow = read(WORKFLOW)

    def test_dedicated_runner_group(self):
        self.assertIn("group: benchmark-runners", self.workflow)
        self.assertNotIn("benchmarking-1", self.workflow)

    def test_no_rust_subgraph_references(self):
        self.assertNotIn("subgraphs-rust", self.workflow)

    def test_no_dual_tech_outputs(self):
        self.assertNotIn("gateways_net", self.workflow)
        self.assertNotIn("EXPECTED_GATEWAYS_NET_JSON", self.workflow)

    def test_latency_uses_main_matrix(self):
        self.assertIn(
            "gateway: ${{ fromJson(needs.prepare-matrix.outputs.gateways) }}",
            self.workflow,
        )

    def test_no_sdk_dependent_fallback(self):
        self.assertNotIn("falling back to local rebuild", self.workflow)
        self.assertNotIn("fallback build script", self.workflow)

    def test_matrix_built_by_script(self):
        self.assertIn("run: python3 k6/build-matrix.py", self.workflow)

    def test_prepare_matrix_checks_out_repo_first(self):
        # prepare-matrix runs k6/build-matrix.py from the repo, so it must
        # check out the repository before executing the script. A fresh
        # ubuntu-latest runner has no checkout otherwise and matrix
        # preparation fails.
        start = self.workflow.index("prepare-matrix:")
        end = self.workflow.index("build-subgraphs:", start)
        section = self.workflow[start:end]
        self.assertIn("actions/checkout", section)
        self.assertIn("k6/build-matrix.py", section)
        self.assertLess(
            section.index("actions/checkout"),
            section.index("k6/build-matrix.py"),
        )

    def test_benchmark_summary_depends_on_prepare_matrix(self):
        # benchmark-summary gates on needs.prepare-matrix.outputs.should_publish,
        # and GitHub only exposes outputs of direct dependencies — so
        # prepare-matrix must be in its needs list or the condition can never
        # resolve and latest-result publishing/cleanup never runs.
        start = self.workflow.index("benchmark-summary:")
        section = self.workflow[start:]
        self.assertIn(
            "needs.prepare-matrix.outputs.should_publish",
            section,
        )
        needs_start = section.index("needs:")
        needs_end = section.index("if:", needs_start)
        needs_block = section[needs_start:needs_end]
        self.assertIn("prepare-matrix", needs_block)

    def test_no_undefined_run_started_at_context(self):
        # github.run_started_at is not a defined GitHub context property
        # (actionlint); timestamps are captured with shell date instead.
        self.assertNotIn("github.run_started_at", self.workflow)
        self.assertNotIn("run_started_at", self.workflow)

    def test_timestamps_captured_via_shell_date(self):
        self.assertIn("started_utc=$(date -u", self.workflow)
        # Line 916-equivalent summary timestamp is generated at summary time,
        # so it must not be labeled "Started".
        self.assertIn("Summary generated (UTC): **$(date -u", self.workflow)
        self.assertNotIn("Started (UTC): **$(date -u", self.workflow)


class BenchmarkScriptTests(unittest.TestCase):
    def setUp(self):
        self.script = read(BENCHMARK_SH)

    def test_no_rust_defaults(self):
        self.assertNotIn("subgraphs-rust", self.script)

    def test_rejects_non_dotnet_override(self):
        self.assertIn("only 'subgraphs-net' is supported", self.script)

    def test_prebuilt_checks_bundled_runtime(self):
        self.assertIn(".dotnet/shared/Microsoft.NETCore.App", self.script)
        # The old SDK-presence probe must be gone: benchmark machines have no SDK.
        self.assertNotIn("command -v dotnet", self.script)

    def test_prebuilt_checks_apphosts(self):
        self.assertIn("bin/Release/net*/", self.script)


class SubgraphScriptTests(unittest.TestCase):
    FAMILIES = ("apollo-federation", "composite-schema")

    def test_build_sh_bundles_sdk(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                content = read(
                    os.path.join(REPO_ROOT, family, "subgraphs-net", "build.sh")
                )
                self.assertIn('.dotnet', content)
                self.assertIn('--install-dir "$BUNDLED_DOTNET_DIR"', content)
                self.assertIn('global.json', content)
                # Builds with the bundled SDK, never a machine-wide one.
                self.assertIn('"$DOTNET" build', content)

    def test_start_sh_launches_apphosts_on_bundled_runtime(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                content = read(
                    os.path.join(REPO_ROOT, family, "subgraphs-net", "start.sh")
                )
                self.assertIn("DOTNET_ROOT", content)
                self.assertIn("bin/Release", content)
                self.assertIn("no bundled .NET runtime", content)
                # No `dotnet run` invocation (comments may mention it to
                # explain why the apphost is used instead).
                self.assertNotRegex(content, r"(?m)^\s*(exec\s+)?dotnet run\b")
                # The apphost ignores launchSettings.json, so start.sh must
                # replicate the configured URLs explicitly.
                self.assertIn("ASPNETCORE_URLS", content)
                self.assertIn("launchSettings.json", content)

    def test_analyzer_refs_are_analyzer_only(self):
        # hotchocolate-best-practices: the source generator ships as an
        # analyzer-only package (IncludeAssets/PrivateAssets), never as
        # OutputItemType="Analyzer".
        for family in self.FAMILIES:
            with self.subTest(family=family):
                projs = sorted(
                    glob.glob(
                        os.path.join(
                            REPO_ROOT,
                            family,
                            "subgraphs-net",
                            "eShop.*",
                            "*.csproj",
                        )
                    )
                )
                self.assertTrue(projs, f"expected csprojs in {family}")
                for proj in projs:
                    content = read(proj)
                    if "HotChocolate.Types.Analyzers" in content:
                        self.assertNotIn("OutputItemType", content)
                        self.assertIn("<IncludeAssets>", content)
                        self.assertIn("<PrivateAssets>all</PrivateAssets>", content)

    def test_no_rust_subgraph_dirs(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                # Tracked Rust sources are gone (git rm); only possibly
                # leftover ignored build residue could remain on disk.
                self.assertFalse(
                    os.path.exists(
                        os.path.join(REPO_ROOT, family, "subgraphs-rust", "Cargo.toml")
                    ),
                    f"{family}/subgraphs-rust sources should be removed",
                )

    def test_generated_bundle_inputs_gitignored(self):
        gitignore = read(os.path.join(REPO_ROOT, ".gitignore"))
        for family in self.FAMILIES:
            with self.subTest(family=family):
                self.assertIn(f"{family}/subgraphs-net/.dotnet/", gitignore)
                self.assertIn(f"{family}/subgraphs-net/global.json", gitignore)


class FusionGatewayTests(unittest.TestCase):
    # Both Fusion gateways must disable only gateway-side cost enforcement:
    # HotChocolate 16.7+ enforces FusionCostOptions limits by default
    # and rejects the deeply nested benchmark query with HC0047, while the
    # default security policy (introspection etc.) must stay enabled. The
    # ModifyCostOptions API only exists on versions with cost enforcement, so
    # Program.cs compiles the call in only when install.sh resolved HotChocolate
    # 16.7 or greater and defined FUSION_16_7_OR_GREATER in the gitignored
    # bench.props; a plain `dotnet build` on older pins compiles it out.
    # Mirrors the composite-schema subgraphs only in keeping header
    # propagation and file composition, not their disableDefaultSecurity.
    GATEWAYS = (
        os.path.join(
            "composite-schema", "gateways", "fusion",
            "eShop.Gateway", "Program.cs",
        ),
        os.path.join(
            "apollo-federation", "gateways", "fusion-nightly-fed",
            "eShop.Gateway", "Program.cs",
        ),
    )
    INSTALL_SCRIPTS = (
        os.path.join("composite-schema", "gateways", "fusion", "install.sh"),
        os.path.join(
            "apollo-federation", "gateways", "fusion-nightly-fed", "install.sh"
        ),
    )
    GATEWAY_CSPROJS = (
        os.path.join(
            "composite-schema", "gateways", "fusion",
            "eShop.Gateway", "eShop.Gateway.csproj",
        ),
        os.path.join(
            "apollo-federation", "gateways", "fusion-nightly-fed",
            "eShop.Gateway", "eShop.Gateway.csproj",
        ),
    )

    def test_fusion_gateways_disable_only_cost_enforcement(self):
        for rel in self.GATEWAYS:
            with self.subTest(gateway=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertIn("#if FUSION_16_7_OR_GREATER", content)
                self.assertIn("ModifyCostOptions", content)
                self.assertIn("EnforceCostLimits = false", content)

    def test_fusion_gateways_have_no_reflection_cost_helper(self):
        # The late-bound FusionCostPolicy helper is gone: no reflection
        # traces may remain in either Program.cs.
        for rel in self.GATEWAYS:
            with self.subTest(gateway=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertNotIn("System.Reflection", content)
                self.assertNotIn("System.Linq.Expressions", content)
                self.assertNotIn('GetMethod("ModifyCostOptions")', content)
                self.assertNotIn("Expression.Lambda", content)
                self.assertNotIn("FusionCostPolicy", content)
                self.assertNotIn("IL2026", content)
                self.assertNotIn("IL2075", content)
                self.assertNotIn("IL3050", content)

    def test_fusion_gateways_keep_default_security(self):
        # Cost-only disable: the broad disableDefaultSecurity switch must
        # not be used, so the default security policy (including the
        # introspection restriction) stays in effect.
        for rel in self.GATEWAYS:
            with self.subTest(gateway=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertNotIn("disableDefaultSecurity", content)
                self.assertIn("AddGraphQLGateway()", content)

    def test_fusion_gateways_keep_auth_and_composition(self):
        # The cost-only change must not take header propagation
        # (benchmark Authorization header) or file composition with it.
        for rel in self.GATEWAYS:
            with self.subTest(gateway=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertIn('options.Headers.Add("Authorization")', content)
                self.assertIn("app.UseHeaderPropagation()", content)
                self.assertIn('AddFileSystemConfiguration("./gateway.far")', content)

    def test_install_scripts_define_cost_constant_from_resolved_version(self):
        # Each install.sh resolves the HotChocolate version per channel at build
        # time and must define FUSION_16_7_OR_GREATER (via DefineConstants in
        # the generated bench.props) exactly when that version is 16.7 or
        # greater, so Program.cs compiles the ModifyCostOptions call in.
        for rel in self.INSTALL_SCRIPTS:
            with self.subTest(script=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertIn("FUSION_16_7_OR_GREATER", content)
                self.assertIn("DefineConstants", content)
                self.assertIn("SELECTED_VERSION", content)
                # Prerelease suffixes (e.g. 16.7.0-p.26) must not break the
                # numeric major.minor comparison.
                self.assertIn("${SELECTED_VERSION%%-*}", content)

    def test_gateway_csprojs_import_bench_props(self):
        # Both gateway csprojs must import the install.sh-generated bench.props
        # when present; without the import the cost define would be inert and a
        # plain `dotnet build` must still compile with the call compiled out.
        for rel in self.GATEWAY_CSPROJS:
            with self.subTest(csproj=rel):
                content = read(os.path.join(REPO_ROOT, rel))
                self.assertIn('Import Project="bench.props"', content)
                self.assertIn("Condition=\"Exists('bench.props')\"", content)


class ResultGenerationTests(unittest.TestCase):
    def setUp(self):
        self.script = read(GENERATE_RESULTS)

    def test_no_net_only_output_split(self):
        self.assertNotIn("EXPECTED_GATEWAYS_NET_JSON", self.script)

    def test_description_dotnet_only(self):
        self.assertIn("4 HotChocolate subgraphs", self.script)
        self.assertNotIn("Results are split by subgraph technology", self.script)

    def test_no_tech_suffix_inference(self):
        self.assertNotIn('endswith("-rust")', self.script)
        self.assertNotIn('endswith("-net")', self.script)

    def test_historical_subgraphs_qualified(self):
        # Historical non-.NET measurements are still rendered, so the setup
        # description must qualify its .NET claim instead of describing every
        # benchmark as a .NET run.
        self.assertIn("Historical note", self.script)
        self.assertIn("historical_kinds", self.script)


class DocsTests(unittest.TestCase):
    def setUp(self):
        self.readme = read(README)

    def test_no_rust_subgraph_setup(self):
        self.assertNotIn("subgraphs-rust", self.readme)
        # The old variant list is gone; the historical-results note may still
        # name the retired stack.
        self.assertNotIn("`subgraphs-rust` = Rust", self.readme)

    def test_documents_runner_group_and_dotnet_only(self):
        self.assertIn("benchmark-runners", self.readme)
        self.assertIn("subgraphs-net", self.readme)
        self.assertIn("k6/build-matrix.py", self.readme)

    def test_pinned_hotchocolate_version_documented(self):
        self.assertIn("16.6.8", self.readme)
        self.assertIn("HotChocolate", self.readme)

    def test_historical_results_marked(self):
        for results_file in ("RESULTS_CONSTANT.md", "RESULTS_BURST.md"):
            with self.subTest(file=results_file):
                content = read(os.path.join(REPO_ROOT, results_file))
                self.assertIn("Historical results", content)
                # Honest history: old Rust rows are preserved, not relabeled.
                self.assertIn("Rust Subgraphs", content)

    def test_federation_spec_link(self):
        self.assertIn(
            "https://graphql.github.io/graphql-federation-spec/", self.readme
        )
        self.assertNotIn(RETIRED_SPEC_SLUG, self.readme)

    def test_no_retired_spec_url_in_tracked_files(self):
        # Regression guard: doc rewrites must not reintroduce the retired
        # spec URL (see RETIRED_SPEC_SLUG). Historical measurements are
        # excluded: they are preserved as measured, never rewritten.
        historical = ("benchmark-runs/", "RESULTS_CONSTANT.md",
                      "RESULTS_BURST.md", "RESULTS_CONSTANT_LATENCY.md")
        tracked = subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=REPO_ROOT
        ).split(b"\0")
        offenders = []
        for raw in tracked:
            if not raw:
                continue
            rel = raw.decode("utf-8", "surrogateescape")
            if rel.startswith(historical):
                continue
            try:
                content = read(os.path.join(REPO_ROOT, rel))
            except (OSError, UnicodeDecodeError):
                continue
            if RETIRED_SPEC_SLUG in content:
                offenders.append(rel)
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
