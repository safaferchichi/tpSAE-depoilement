# Utiliser une image légère et moderne
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier uniquement requirements et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port 80
EXPOSE 80

# Démarrer l'application
CMD ["python", "api.py"]

