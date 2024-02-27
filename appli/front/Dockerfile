# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le container
WORKDIR /app

# Installer les dépendances
RUN pip install flask requests

# Copier les fichiers d'application dans le répertoire de travail
COPY app.py /app
COPY templates /app/templates

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 80

# Commande pour exécuter l'application lorsque le container démarre
CMD ["python", "app.py"]