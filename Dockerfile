# Choisir une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers du répertoire local dans le répertoire /app du conteneur
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel ton application va tourner
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "main.py"]
