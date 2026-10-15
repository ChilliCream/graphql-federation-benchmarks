# feddi Gateway

[feddi Gateway](https://feddi.dev) ([feddi-dev/feddi-gateway](https://github.com/feddi-dev/feddi-gateway))
is a JVM-native GraphQL composite-schema federation gateway built on
[GraphQL Java](https://github.com/graphql-java/graphql-java). It composes source
schemas, plans cross-subgraph operations, and executes requests entirely inside
the JVM.

## How this integration works

feddi is built from source (there is no published OSS binary) and configured for
the benchmark port layout (gateway on `5220`, subgraphs on `5221`–`5224`).

- **`install.sh`**
  1. Bundles a JDK 25 into `./.jdk` (feddi requires Java 25+).
  2. Clones `feddi-dev/feddi-gateway` at a pinned commit into `./source`.
  3. Builds the distribution (`./gradlew :app:feddiGatewayDistZip`) and extracts
     it to `./dist`.
  4. Copies the subgraph SDLs from the canonical HotChocolate exports in
     `../../subgraphs-net` into `./subgraph-config` (no hand-maintained copies).
  5. Assembles `./subgraphs.zip` from `./subgraph-config`.
- **`start.sh`** launches `dist/feddi-gateway/bin/feddi-gateway`, waits for the
  admin endpoint, uploads `subgraphs.zip` (feddi composes the supergraph at
  runtime), verifies the composed schema serves queries, then stays attached so
  the harness can manage the process.
- **`feddi-gateway.yml`** sets the gateway port (`5220`), admin port (`9091`),
  and management/health port (`9090`, `GET /actuator/health`).
- **`subgraph-config/<name>/`** holds each subgraph's `config.yaml` (its `url`
  and `batching: variables`); `install.sh` adds the `schema.graphqls`.

### Variable batching

Each subgraph is configured with `batching: variables`: feddi sends the entity
lookups of one plan step as a single request with a `variables` array and reads
the `application/jsonl` response (HotChocolate's variable batching). At startup
feddi checks that each subgraph supports it; a subgraph that does not get alias
batching instead (one request with an aliased copy of the lookup per entity),
with an error in the gateway log.

### Subgraph connection pool

feddi's default subgraph connection pool (500 connections per subgraph host) is
used as is: with variable batching the benchmark query makes 8 subgraph calls,
and 50 VUs keep about 70 connections per subgraph open. Set
`FEDDI_SUBGRAPH_MAX_CONNECTIONS` to override the limit.
