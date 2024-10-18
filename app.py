import flask
from flask import request, render_template, redirect, url_for, flash

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Définir une clé secrète pour les sessions et les messages flash
app.secret_key = 'bonnechancence'  # Changez cela par une valeur plus complexe et sécurisée

# Liste d'employés
employees = []

@app.route('/')
def home():
    return render_template('ajouter_utilisateur.html')

@app.route('/ajouter', methods=['POST'])
def ajouter_utilisateur():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    fonction = request.form.get('fonction')

    if not nom or not prenom or not fonction:
        flash('Tous les champs sont requis !')
        return redirect(url_for('home'))

    new_id = len(employees)  # Assignation d'un nouvel ID
    employees.append({"id": new_id, "Nom": nom, "Prénom": prenom, "Fonction": fonction})
    flash('Utilisateur ajouté avec succès !')
    return redirect(url_for('liste_utilisateurs'))

@app.route('/utilisateurs')
def liste_utilisateurs():
    return render_template('liste_utilisateurs.html', employees=employees)

if __name__ == '__main__':
    app.run()
