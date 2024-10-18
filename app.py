import flask
from flask import request, jsonify, render_template, redirect, url_for
import bcrypt

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'trfml'  # Nécessaire pour les sessions Flask

# Base de données en mémoire pour stocker les utilisateurs
users = []

# Route pour la page d'accueil
@app.route('/')
def home():
    return '''<h1>Gestion des utilisateurs</h1>
              <p>Bienvenue dans l'application de gestion des utilisateurs.</p>
              <a href="/add_user">Ajouter un utilisateur</a><br>
              <a href="/list_users">Lister les utilisateurs</a>
           '''

# Route pour afficher le formulaire d'ajout d'utilisateur
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        # Hachage du mot de passe avec bcrypt
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Ajouter l'utilisateur à la liste
        users.append({"username": username, "password": hashed_password})

        # Redirection vers la liste des utilisateurs après ajout
        return redirect(url_for('list_users'))

    return '''
        <h1>Ajouter un utilisateur</h1>
        <form method="POST">
            Nom d'utilisateur : <input type="text" name="username" required><br>
            Mot de passe : <input type="password" name="password" required><br>
            <input type="submit" value="Ajouter">
        </form>
        <br>
        <a href="/">Retour à l'accueil</a>
    '''

# Route pour lister les utilisateurs
@app.route('/list_users', methods=['GET'])
def list_users():
    user_list = '<h1>Liste des utilisateurs</h1><ul>'
    for user in users:
        user_list += f'<li>Nom d\'utilisateur : {user["username"]}</li>'
    user_list += '</ul><br><a href="/">Retour à l\'accueil</a>'
    return user_list

# Route pour ajouter un utilisateur via une API (POST)
@app.route('/api/users', methods=['POST'])
def api_add_user():
    # Récupération des données JSON envoyées via l'API
    if request.json and 'username' in request.json and 'password' in request.json:
        username = request.json['username']
        password = request.json['password'].encode('utf-8')

        # Hachage du mot de passe
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Ajouter l'utilisateur à la liste
        users.append({"username": username, "password": hashed_password})

        return jsonify({"message": "Utilisateur ajouté avec succès !"}), 201
    else:
        return jsonify({"error": "Les données envoyées sont incorrectes."}), 400

if __name__ == "__main__":
    app.run()
