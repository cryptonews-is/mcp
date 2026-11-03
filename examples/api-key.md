# API key instead of OAuth

For clients without OAuth support, create a key at https://mcp.cryptonews.is/account and send it as a Bearer header. Keep the key in an environment variable, not in a committed file.

```json
{
  "mcpServers": {
    "cryptonews": {
      "type": "http",
      "url": "https://mcp.cryptonews.is/mcp",
      "headers": { "Authorization": "Bearer ${CRYPTONEWS_API_KEY}" }
    }
  }
}
```

REST takes API keys only; OAuth connector tokens work on MCP only.
