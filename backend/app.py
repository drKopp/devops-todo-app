from flask import Flask, jsonify, request

# Création de l'application Flask principale
# Flask utilise __name__ pour connaître le point d'entrée du programme
# Cela permet à Flask de localiser les ressources (templates, fichiers statiques, etc.)
app = Flask(__name__)

# Liste des tâches stockées temporairement en mémoire (pas de base de données)
todos = []


# Définition de la route pour récupérer toutes les tâches (liste To-Do)
# Méthode HTTP : GET → pour lire les données
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


# Définition de la route pour ajouter une nouvelle tâche
# Méthode HTTP : POST → pour créer une ressource
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()  # On récupère les données JSON envoyées
    todo = {
        "id": len(todos) + 1,  # On crée un identifiant unique simple
        "title": data["title"],  # Le titre de la tâche
        "done": False,  # Par défaut, la tâche n'est pas encore faite
    }
    todos.append(todo)  # On ajoute la nouvelle tâche à la liste
    return jsonify(todo), 201  # 201 = Code HTTP "Créé"


# Définition de la route pour marquer une tâche comme terminée
# Méthode HTTP : PUT → pour modifier une ressource existante
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def mark_done(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True  # On marque la tâche comme faite
            return jsonify(todo)
    return jsonify({"error": "Tâche non trouvée"}), 404  # Si l'ID n'existe pas


# Définition de la route pour supprimer une tâche par son ID
# Méthode HTTP : DELETE → pour supprimer une ressource
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [
        t for t in todos if t["id"] != todo_id
    ]  # On garde les tâches sauf celle à supprimer
    return jsonify({"message": "Tâche supprimée"}), 200


# Lancer le serveur Flask uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    # Le mode debug permet d'afficher les erreurs en détail pendant le développement
    app.run(debug=True)
