from flask import Flask, request, jsonify
from data_manager import DataManager
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "API des utilisateurs",
        "description": "Cette API permet de gérer les utilisateurs.",
        "version": "1.0.0"
    },
    "host": "127.0.0.1:5000",
    "schemes": [
        "http"
    ]
})
data_manager = DataManager()

@app.route("/users", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur via une requête POST.
    ---
    parameters:
      - in: body
        name: user
        schema:
          type: object
          required:
            - name
            - age
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      201:
        description: Utilisateur ajouté avec succès.
        schema:
          id: user
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
      400:
        description: Paramètres manquants
    """
    data = request.json
    if "name" not in data or "age" not in data:
        return jsonify({"error": "Missing name or age"}), 400

    user = data_manager.add_user(data["name"], data["age"])
    return jsonify(user), 201

@app.route("/users", methods=["GET"])
def get_users():
    """
    Récupère tous les utilisateurs enregistrés.
    ---
    responses:
      200:
        description: Liste des utilisateurs.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              age:
                type: integer
    """
    return jsonify(data_manager.get_users())


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Supprime un utilisateur via son ID.
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        type: integer
        description: L'ID de l'utilisateur à supprimer
    responses:
      200:
        description: L'utilisateur a été supprimé avec succès.
      404:
        description: L'utilisateur n'a pas été trouvé.
    """
    if data_manager.delete_user(user_id):
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

