import flask
from flask import request, jsonify

# Utiliser __name__ pour le nom de l'application Flask
app = flask.Flask(__name__)

app.config["DEBUG"] = True

employees = [
    {"id": 0, "Nom": "Dupont", "Prénom": "Jean", "Fonction": "Développeur", "Anciennete": "5"},
    {"id": 1, "Nom": "Durand", "Prénom": "Elodie", "Fonction": "Directrice Commerciale", "Anciennete": "4"},
    {"id": 2, "Nom": "Lucas", "Prénom": "Jeremie", "Fonction": "DRH", "Anciennete": "4"}
]

@app.route('/user', methods=['GET'])
def api_all():
    return jsonify(employees)

# Lancer l'application
if __name__ == '__main__':
    app.run()
