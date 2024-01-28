# The Finals Leaderboard

A free API for The Finals ranking data. You can find data such as rank, name, total player cashouts, etc... . Feel free to use the api for your projects. You can also quote the depot when you use it. Thanks

# API Endpoints

Crossplay :

> [https://soraclee.github.io/tfleaderboard/leaderboard-crossplay.json](https://soraclee.github.io/tfleaderboard/leaderboard-crossplay.json)

Steam :

> [https://soraclee.github.io/tfleaderboard/leaderboard-steam.json](https://soraclee.github.io/tfleaderboard/leaderboard-steam.json)

Xbox :

> [https://soraclee.github.io/tfleaderboard/leaderboard-xbox.json](https://soraclee.github.io/tfleaderboard/leaderboard-xbox.json)

PlayStation :

> [https://soraclee.github.io/tfleaderboard/leaderboard-psn.json](https://soraclee.github.io/tfleaderboard/leaderboard-psn.json)

Returns the latest leaderboard data

## Example Response

```json
[
  {
    "name": "TwitchTvPookOut#5437",
    "rank": 1,
    "fame": 414045,
    "old_fame": 404880,
    "old_rank": 1,
    "cashouts": 94420202,
    "networks": {
      "steam": "PookOut",
      "psn": "",
      "xbox": ""
    }
  },
  {...}
]
```
