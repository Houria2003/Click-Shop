# Utilise l'image officielle de Python 3.8
FROM python:3.8-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie tous les fichiers du projet dans le conteneur
COPY . /app

# Installe les dépendances depuis le fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port 5000 (par défaut pour Flask)
EXPOSE 5000

# Démarre l'application avec Flask
CMD ["python", "main.py"]
