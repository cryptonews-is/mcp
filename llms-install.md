# Installing the cryptonews.is MCP server

This is a hosted remote server. Do not clone, build or run anything.

1. Add a remote MCP server named `cryptonews` with this URL, using the Streamable HTTP transport:
   `https://mcp.cryptonews.is/mcp`
2. Authentication, either:
   - **OAuth (preferred):** the server answers unauthenticated requests with `401` and OAuth protected-resource metadata. The client registers itself (dynamic client registration) and the user signs in with their email.
   - **API key:** if the user has a key (`cnis_live_...`) from https://mcp.cryptonews.is/account, send it as the header `Authorization: Bearer <key>`. Never write the key into a shared file; read it from an environment variable such as `CRYPTONEWS_API_KEY`.
3. Check the connection by calling the `status` tool. It returns the plan, usage and data freshness.

Every tool is read-only. Free accounts can use `latest_stories`, `get_sentiment`, `get_market` and `status`; other tools answer with the plan they need.
