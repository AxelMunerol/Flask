# Gestion des Utilisateurs - Application Flask

Cette application est une simple démonstration d'un système de gestion des utilisateurs avec Flask. Elle permet d'ajouter des utilisateurs, de lister les utilisateurs enregistrés, et offre une API pour ajouter des utilisateurs via des requêtes POST. Les mots de passe sont hachés à l'aide de `bcrypt` pour garantir la sécurité.

## Fonctionnalités

- **Ajouter des utilisateurs** : Les utilisateurs peuvent être ajoutés via un formulaire web.
- **Lister les utilisateurs** : Affiche la liste des utilisateurs enregistrés (sans afficher les mots de passe).
- **API REST** : Permet d'ajouter des utilisateurs via des requêtes HTTP POST.

## Installation

### Prérequis

- Python 3.x
- Flask
- Bcrypt

### Installation des dépendances

1. Clonez ce dépôt dans votre environnement local.

```bash
git clone <url_du_dépôt>
cd <nom_du_dossier>
```

2. Installez les dépendances via `pip` (si vous utilisez un environnement virtuel, activez-le avant cette commande).

```bash
pip install Flask bcrypt
```

## Utilisation

1. Lancez l'application en exécutant le script principal :

```bash
python mainpage.py
```

2. L'application sera accessible à l'adresse suivante :

```
http://127.0.0.1:5000/
```

### Routes disponibles

#### Page d'accueil

- **Route** : `/`
- **Méthode** : GET
- **Description** : Affiche la page d'accueil de l'application avec des liens pour ajouter ou lister les utilisateurs.

#### Ajouter un utilisateur

- **Route** : `/add_user`
- **Méthode** : GET, POST
- **Description** : Affiche un formulaire pour ajouter un nouvel utilisateur. Le mot de passe est haché avant d'être stocké.

#### Lister les utilisateurs

- **Route** : `/list_users`
- **Méthode** : GET
- **Description** : Affiche la liste des utilisateurs enregistrés. Les mots de passe ne sont pas affichés.

#### Ajouter un utilisateur via l'API

- **Route** : `/api/users`
- **Méthode** : POST
- **Corps de la requête** : 
  ```json
  {
    "username": "nom_utilisateur",
    "password": "mot_de_passe"
  }
  ```
- **Description** : Permet d'ajouter un utilisateur via une requête HTTP POST en envoyant les données sous format JSON.
- **Réponse** : Renvoie un message de succès ou une erreur si les données sont incorrectes.

## Exemples d'utilisation de l'API

Vous pouvez tester l'API via **Postman** ou tout autre outil similaire.

### Requête POST - Ajouter un utilisateur

URL : `http://127.0.0.1:5000/api/users`

```json
{
  "username": "exemple",
  "password": "motdepasse"
}
```

Réponse :

```json
{
  "message": "Utilisateur ajouté avec succès !"
}
```

## Sécurité

Les mots de passe sont hachés à l'aide de `bcrypt` avant d'être stockés pour garantir qu'ils ne soient pas enregistrés en clair. Assurez-vous que votre application utilise une clé secrète (variable `app.secret_key`) pour les sessions Flask.

