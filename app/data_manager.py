"""
Module data_manager

Ce module gère les opérations CRUD (Create, Read, Delete) pour les utilisateurs.
"""

class DataManager:
    """
    Classe DataManager pour gérer une liste d'utilisateurs.

    Attributes:
        users (list): Liste des utilisateurs enregistrés.
    """

    def __init__(self):
        """Initialise un gestionnaire avec une liste vide d'utilisateurs."""
        self.users = []

    def add_user(self, name: str, age: int) -> dict:
        """
        Ajoute un utilisateur à la liste.

        Args:
            name (str): Nom de l'utilisateur.
            age (int): Âge de l'utilisateur.

        Returns:
            dict: L'utilisateur ajouté.
        """
        user = {"id": len(self.users) + 1, "name": name, "age": age}
        self.users.append(user)
        return user

    def get_users(self) -> list:
        """
        Récupère tous les utilisateurs.

        Returns:
            list: Liste des utilisateurs enregistrés.
        """
        return self.users

    def delete_user(self, user_id: int) -> bool:
        """
        Supprime un utilisateur par son ID.

        Args:
            user_id (int): L'ID de l'utilisateur à supprimer.

        Returns:
            bool: True si l'utilisateur a été supprimé, False sinon.
        """
        for user in self.users:
            if user["id"] == user_id:
                self.users.remove(user)
                return True
        return False
