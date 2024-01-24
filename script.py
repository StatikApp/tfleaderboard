from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Effectuer une requête HTTP vers l'API de The Finals pour obtenir le leaderboard
    # Remplacez l'URL et les paramètres en fonction de l'API que vous utilisez
    response = requests.get('https://storage.googleapis.com/embark-discovery-leaderboard/leaderboard-crossplay-discovery-live.json')
    
    # Traiter la réponse JSON
    data = response.json()
    
    # Stocker les données dans un fichier JSON
    with open('leaderboard.json', 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
