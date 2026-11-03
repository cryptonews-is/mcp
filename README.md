# cryptonews.is MCP server

<img src="assets/icon-400.png" alt="cryptonews.is" width="96" align="right">

Live crypto news as data for agents. cryptonews.is reads over 1,000 sources, groups their reports into stories, summarises each story in 28 languages, and scores the tone of the news minute by minute. This remote MCP server gives an agent the same data.

- **Server:** `https://mcp.cryptonews.is/mcp` (Streamable HTTP)
- **Sign-in:** OAuth 2.1 with dynamic client registration (sign in with your email), or an API key as a Bearer header
- **Registry name:** `is.cryptonews/news` in the [official MCP Registry](https://registry.modelcontextprotocol.io)
- **Docs:** https://mcp.cryptonews.is/docs?utm_source=github&utm_campaign=mcp-listing

This repository holds connection examples and listing metadata only. The service itself is hosted; there is nothing to install or run.

## Tools

Every tool is read-only.

| Tool | What it returns | Plans |
| --- | --- | --- |
| `latest_stories` | Ranked current stories, each with its coins, category, sentiment and how many outlets cover it | All |
| `get_sentiment` | The news sentiment reading (15 minutes to 24 hours) and the stories driving it | All |
| `get_market` | Market quotes, top coins, total market cap and coins named in current stories | All |
| `status` | Plan, usage and upstream freshness | All |
| `get_story` | One story with every outlet's report, in 28 languages, including archived stories | Standard, Pro |
| `get_sentiment_history` | Historical sentiment readings | Standard, Pro |
| `changes_since` | Stories added, changed or merged since a cursor | Standard, Pro |
| `search_stories` | Full-text story search ranked by relevance | Pro |

Example questions: "What's moving crypto right now?", "Why is crypto news bearish today?", "Show every outlet's report on the top story in German."

## Plans

One account covers MCP and REST.

| Plan | Price | Calls/day | Per minute |
| --- | --- | --- | --- |
| Free | $0 | 100 | 10 |
| Standard | $29 / 30 days | 10,000 | 60 |
| Pro | $99 / 30 days | 50,000 | 300 |

See the [docs](https://mcp.cryptonews.is/docs?utm_source=github&utm_campaign=mcp-listing) for limits, errors and arguments.

## Connect

**Claude (claude.ai and Claude Desktop):** Settings → Connectors → Add custom connector → `https://mcp.cryptonews.is/mcp`, then sign in.

**Claude Code:**

```bash
claude mcp add --transport http cryptonews https://mcp.cryptonews.is/mcp
```

**Other clients:** see [`examples/`](examples) for Cursor, VS Code, Windsurf, API-key and REST setups.

## Use and terms

Free is for personal use with credit. Standard and Pro may display data with credit and a link to the story. No resale or model training. The service and its data are governed by the [terms and privacy policy](https://mcp.cryptonews.is/terms). The examples in this repository are MIT licensed.

Support: api@cryptonews.is
