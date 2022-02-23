from bdd import BDD
import unidecode

# Connexion à la base de donnée.
bdd = BDD("localhost", "trombinoscope", "root", "root", 8890)

# Récupération de l'id, nom, prénom.
user_info = bdd.dbSelectNomPrenom()


adresses = []
with open("adresses.txt", "r") as file:
    for row in file:
        # Enlever le retour à la ligne.
        row = row.replace('\n', '')

        # Isoler nom et prénom
        adresses.append(row)

user_with_email = {}

# On parcourt chaque éléments de notre base de données
for user_bdd in user_info:
    nom_bdd = user_bdd[1].lower().replace(' ', '-')
    prenom_bdd = user_bdd[2].lower().replace(' ', '-')

    # Enlever les accents.
    nom_bdd = unidecode.unidecode(nom_bdd)
    prenom_bdd = unidecode.unidecode(prenom_bdd)

    for adresse in adresses:
        prenom_adresse, nom_adresse = adresse.split('@')[0].split('.')

        if nom_bdd in nom_adresse and prenom_bdd in prenom_adresse:
            user_with_email[user_bdd[0]] = adresse

# Mise a jour de la base de donnée.
for key in user_with_email:
    bdd.dbUpdateUserEmail(key, user_with_email[key])
    # print(key, user_with_email[key])

