from flask import Flask, render_template, jsonify
import os
import requests

app = Flask(__name__)

# Récupérer l'adresse du backend depuis la variable d'environnement BACKEND_URL
backend_url = os.environ.get('BACKEND_URL', 'http://localhost:5000/racontemoiunehistoire')

# Page d'accueil avec le frontend
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint pour appeler le backend depuis le frontend
@app.route('/goapi')
def go_api():
    try:
        # Faire la requête au backend
        response = requests.get(backend_url)
        data = response.json()
        histoire = data.get('histoire', 'Erreur lors de la récupération de l\'histoire')
        return jsonify({"histoire": histoire}), 200
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)