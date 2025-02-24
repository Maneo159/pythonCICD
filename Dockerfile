FROM python:3.9-slim

WORKDIR /app

# Copier tous les fichiers dans le répertoire /app
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "main.py"]
