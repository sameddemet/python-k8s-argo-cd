from flask import Flask, jsonify
from flask_cors import cross_origin
import random

app = Flask(__name__)


# Chemin vers le fichier texte contenant les histoires
CHEMIN_FICHIER = "/nuno.txt"

# Fonction pour lire une ligne aléatoire dans le fichier texte
def lire_ligne_aleatoire():
    with open(CHEMIN_FICHIER, "r", encoding="utf-8") as fichier:
        lignes = fichier.readlines()
        return random.choice(lignes)

# Endpoint pour raconter une histoire
@app.route('/racontemoiunehistoire', methods=['GET'])
@cross_origin()
def raconte_moi_une_histoire():
    try:
        ligne = lire_ligne_aleatoire()
        return jsonify({"histoire": ligne}), 200
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)