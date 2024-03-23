import requests
import json
import re

leaderboard_array = [
    "https://storage.googleapis.com/embark-discovery-leaderboard/s2-leaderboard-crossplay-discovery-live.json",
    "https://storage.googleapis.com/embark-discovery-leaderboard/s2-leaderboard-steam-discovery-live.json",
    "https://storage.googleapis.com/embark-discovery-leaderboard/s2-leaderboard-xbox-discovery-live.json",
    "https://storage.googleapis.com/embark-discovery-leaderboard/s2-leaderboard-psn-discovery-live.json"
]

for leaderboard_url in leaderboard_array:
    # Extract the platform name using regular expression
    match = re.search(r'leaderboard-(.*?)-discovery-live\.json', leaderboard_url)
    if match:
        platform = match.group(1)
    else:
        platform = "unknown"

    response = requests.get(leaderboard_url)
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

    # Construct the output file name
    output_filename = f'leaderboard-{platform}.json'

    with open(output_filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

    print(f"Data for {platform} leaderboard saved to {output_filename}")
