from datetime import date
from pages.categories.data.data_stote import save_data,data
from pages.stores.store import connector




# Fonction pour ajouter un utilisateur
def ajouter_utilisateur(email, last_name, first_name, password):
    data["utilisateurs"].append({
        "email": email,
        "last_name": last_name,
        "first_name": first_name,
        "password": password,
        "boeufs": [],
        "ventes": {},
        "production": {},
    })
    save_data(data)

def ajouter_boeuf(id_boeuf, nom, race, sexe, actif=True):
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            a["boeufs"].append({
                "id": id_boeuf,
                "nom": nom,
                "race": race,
                "sexe": sexe,
                "actif": actif,
                "production": {},
                "vacination": [],
            })
    save_data(data)

def supprimer_boeuf_user(id_boeuf):
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            for b in a["boeufs"]:
                if b["id"] == id_boeuf:
                    #del {b["actif"]}
                    a["boeufs"].remove(b)
                    break
    save_data(data)

def ajouter_production_user(id_boeuf, litres):
    jour = str(date.today())
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            for b in a["boeufs"]:
                if b["id"] == id_boeuf:
                    if jour not in b["production"]:
                        b["production"][jour] = []
                    b["production"][jour].append({
                        "litres": litres
                    })
                    break
            if jour not in a["production"]:
                a["production"][jour] = []
            a["production"][jour].append({
                "id": id_boeuf,
                "litres": litres
            })
    save_data(data)

def supprimer_production_user(jour, id_boeuf):
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            for b in a["boeufs"]:
                if b["id"] == id_boeuf:
                    if jour in b["production"]:
                        del b["production"][jour]
                    break
    save_data(data)

def ajouter_vente_user(litres_vendus, prix_litre, jour=None):
    jour = jour or str(date.today())
    revenu = litres_vendus * prix_litre
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            if jour not in a["ventes"]:
                a["ventes"][jour] = {
                    "litres_vendus": litres_vendus,
                    "prix_litre": prix_litre,
                    "revenu": revenu
                }
            else:
                a["ventes"][jour]["litres_vendus"] += litres_vendus
                a["ventes"][jour]["revenu"] += revenu
                x = a["ventes"][jour]["revenu"] / a["ventes"][jour]["litres_vendus"]
                a["ventes"][jour]["prix_litre"] = x
            break
    save_data(data)

def supprimer_vente_user(jour):
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            if jour in a["ventes"]:
                del a["ventes"][jour]
            break
    save_data(data)


#=================================================
def supprimer_boeuf(id_boeuf):
    for b in data["boeufs"]:
        if b["id"] == id_boeuf:
            #del {b["actif"]}
            data["boeufs"].remove(b)
            break
    save_data(data)


# Fonction pour supprimer la production d'un jour
def supprimer_production(jour, id_boeuf):
    if jour in data["production"]:
        data["production"][jour] = [p for p in data["production"][jour] if p["id_boeuf"] != id_boeuf]
    save_data(data)

# Fonction pour supprimer une vente d'un jour
def supprimer_vente(jour):
    if jour in data["ventes"]:
        del data["ventes"][jour]
    save_data(data)


def ajouter_production(id_boeuf, litres, jour=None):
    jour = jour or str(date.today())
    if jour not in data["production"]:
        data["production"][jour] = []
    data["production"][jour].append({
        "id_boeuf": id_boeuf,
        "litres": litres
    })
    save_data(data)

def ajouter_vente(litres_vendus, prix_litre, jour=None):
    jour = jour or str(date.today())
    revenu = litres_vendus * prix_litre
    data["ventes"][jour] = {
        "litres_vendus": litres_vendus,
        "prix_litre": prix_litre,
        "revenu": revenu
    }
    save_data(data)
#=======================================================

def total_lait_produit_user(jour=None):
    for c in connector:
        email_connector = c["email"]
    total = 0
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            if jour:
                total += sum(p["litres"] for p in a["production"].get(jour, []))
            else:
                total += sum(
                    p["litres"]
                    for j in a["production"].values()
                    for p in j
                )
    return total

def total_vendu_user():
    for c in connector:
        email_connector = c["email"]
    total = 0
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            total += sum(v["revenu"] for v in a["ventes"].values())
    return total

def lait_restant_user():
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            total_produit = total_lait_produit_user()
            total_litres_vendus = sum(v["litres_vendus"] for v in a["ventes"].values())
            return total_produit - total_litres_vendus

#=======================================================

def total_lait_produit(jour=None):
    if jour:
        return sum(p["litres"] for p in data["production"].get(jour, []))
    else:
        return sum(
            p["litres"]
            for jour in data["production"].values()
            for p in jour
        )

def total_vendu():
    return sum(v["revenu"] for v in data["ventes"].values())

def lait_restant():
    total_produit = total_lait_produit()
    total_litres_vendus = sum(v["litres_vendus"] for v in data["ventes"].values())
    return total_produit - total_litres_vendus
#=======================================================

def ajouter_vaccination(id_boeuf, date_vaccin, type_vaccin):
    for c in connector:
        email_connector = c["email"]
    for a in data["utilisateurs"]:
        if a["email"] == email_connector:
            for b in a["boeufs"]:
                if b["id"] == id_boeuf:
                    b.setdefault("vacination", []).append({
                        "date": date_vaccin,
                        "type": type_vaccin
                    })
                    break
    save_data(data)