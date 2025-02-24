# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source dans le conteneur
COPY . .

# Exposer le port que l'application utilisera (par défaut, Flask utilise le port 5000)
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app/main.py"]
