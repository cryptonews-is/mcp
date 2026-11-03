"""Why is crypto news bearish (or bullish) right now? Standard library only."""
import json
import os
import urllib.request

request = urllib.request.Request(
    "https://api.cryptonews.is/v1/sentiment?window=24h&limit=5",
    headers={"Authorization": f"Bearer {os.environ['CRYPTONEWS_API_KEY']}"},
)
with urllib.request.urlopen(request) as response:
    reading = json.load(response)

print(json.dumps(reading, indent=2)[:2000])
