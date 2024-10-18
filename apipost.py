import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Liste d'employés (ou d'utilisateurs)
employees = [
    {"id": 0, "Nom": "Dupont", "Prénom": "Jean", "Fonction": "Développeur", "Anciennete": "5"},
    {"id": 1, "Nom": "Durand", "Prénom": "Elodie", "Fonction": "Directrice Commerciale", "Anciennete": "4"},
    {"id": 2, "Nom": "Lucas", "Prénom": "Jeremie", "Fonction": "DRH", "Anciennete": "4"}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Annuaire Internet</h1>
<p>Pif pouf ce site est le prototype d’une API mettant à disposition des données sur les employés d’une entreprise.</p>'''

@app.route('/users', methods=['GET'])
def api_all():
    return jsonify(employees)

@app.route('/adduser', methods=['POST'])
def api_add_employee():
    new_employee = request.get_json()  # Récupère les données JSON envoyées dans la requête

    # Vérifier si l'utilisateur a fourni les champs requis
    if not new_employee or 'Nom' not in new_employee or 'Prénom' not in new_employee or 'Fonction' not in new_employee:
        return jsonify({"error": "Données incomplètes"}), 400

    # Ajouter un nouvel ID (le dernier ID + 1)
    new_id = employees[-1]['id'] + 1 if employees else 0
    new_employee['id'] = new_id

    employees.append(new_employee)  # Ajouter le nouvel utilisateur à la liste
    return jsonify(new_employee), 201  # Retourner le nouvel utilisateur avec le code de statut 201 (Created)

if __name__ == '__main__':
    app.run()
