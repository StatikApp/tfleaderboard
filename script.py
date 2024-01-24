import json
import requests

response = requests.get('https://storage.googleapis.com/embark-discovery-leaderboard/leaderboard-crossplay-discovery-live.json')

data = response.json()

with open('leaderboard.json', 'w') as json_file:
    json_file.write(json.dumps(data, indent=2))
