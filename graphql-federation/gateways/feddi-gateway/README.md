# feddi-gateway

[feddi-gateway](https://github.com/feddi-dev/feddi-gateway) by [feddi](https://feddi.dev) is an open-source (Apache 2.0)
JVM-native gateway for the [GraphQL Federation spec](https://graphql.github.io/graphql-federation-spec/), built on
[GraphQL Java](https://github.com/graphql-java/graphql-java).

- `install.sh` installs the latest feddi release from [feddi.dev/releases](https://feddi.dev/releases) (calver
  `YYYY-MM-DD-HHMM`, reported in the results), checked against the sha256 in its release manifest.
  `BENCH_GATEWAY_VERSION=<version>` installs that release instead (feddi.dev keeps at least the last 10 releases
  and all of the last 30 days).
- `start.sh` starts the gateway and uploads the subgraph schemas, which it composes at runtime.
- Subgraphs use alias batching (`batching: alias` in `subgraph-config/<name>/config.yaml`).
