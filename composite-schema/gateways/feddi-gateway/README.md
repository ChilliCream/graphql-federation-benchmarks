# feddi-gateway

[feddi-gateway](https://github.com/feddi-dev/feddi-gateway) by [feddi](https://feddi.dev) is an open-source (Apache 2.0)
JVM-native gateway for the [GraphQL Federation spec](https://graphql.github.io/graphql-federation-spec/), built on
[GraphQL Java](https://github.com/graphql-java/graphql-java).

- `install.sh` builds it from source at a pinned commit (`FEDDI_GATEWAY_REF`) of a feddi release, whose version
  (`FEDDI_GATEWAY_VERSION`, calver `YYYY-MM-DD-HHMM`) is reported in the results. Released builds are at
  [feddi.dev/downloads](https://feddi.dev/downloads).
- `start.sh` starts the gateway and uploads the subgraph schemas, which it composes at runtime.
- Subgraphs use variable batching (`batching: variables` in `subgraph-config/<name>/config.yaml`).
