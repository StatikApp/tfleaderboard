import json
import requests

response = requests.get('https://storage.googleapis.com/embark-discovery-leaderboard/leaderboard-crossplay-discovery-live.json')

data = response.json()

for entry in data:
    entry['rank'] = entry.pop('r', None)
    entry['fame'] = entry.pop('f', None)
    entry['old_fame'] = entry.pop('of', None)
    entry['old_rank'] = entry.pop('or', None)
    entry['cashouts'] = entry.pop('c', None)

    entry['networks'] = {
        'steam': entry.pop('steam', None),
        'psn': entry.pop('psn', None),
        'xbox': entry.pop('xbox', None)
    }

with open('leaderboard.json', 'w') as json_file:
    json_file.write(json.dumps(data, indent=2))
