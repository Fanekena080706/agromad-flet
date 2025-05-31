import json
import os
from datetime import date

# Fichier de stockage
DATA_FILE = "data.json"

# Données initiales
default_data = {
    "boeufs": [],
    "production": {},
    "ventes": {},
    "utilisateurs": [],
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return default_data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Charger les données à l'ouverture
data = load_data()
