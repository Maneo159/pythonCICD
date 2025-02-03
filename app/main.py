from flask import Flask, request, jsonify
from app.data_manager import DataManager

app = Flask(__name__)
data_manager = DataManager()

@app.route("/users", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur via une requête POST.

    Expects JSON:
    {
        "name": "Alice",
        "age": 25
    }

    Returns:
        dict: L'utilisateur ajouté avec son ID.
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

    Returns:
        list: Liste des utilisateurs.
    """
    return jsonify(data_manager.get_users())

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Supprime un utilisateur via son ID.

    Args:
        user_id (int): L'ID de l'utilisateur à supprimer.

    Returns:
        dict: Message de confirmation ou d'erreur.
    """
    if data_manager.delete_user(user_id):
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
