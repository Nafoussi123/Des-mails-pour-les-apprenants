import mysql.connector as mysql
from utilisateur import Utilisateur
    
class BDD:

    # Constructeur.
    def __init__(self, host, database, user, password, port):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.curseur = None

    def connectBDD(self):
        # Connexion à la base de données.
        self.connexion = mysql.connect( host = self.host, 
                                        database = self.database, 
                                        user = self.user, 
                                        password = self.password,
                                        port = self.port) 


        # Cursor.
        self.curseur = self.connexion.cursor()

    # Close connection.
    def close(self):
        self.curseur.close()
        self.connexion.close()
        self.curseur = None
    
    def dbSelectNomPrenom(self):
        self.connectBDD()

        # SELECT id_personne, nom, prenom FROM personne;
        requete = "SELECT id_personne, nom, prenom FROM personne;"

        self.curseur.execute(requete)
        result = self.curseur.fetchall()
        

        self.close()
        return result
    
    def dbUpdateUserEmail(self, id, email):
        self.connectBDD()

        # SELECT id_personne, nom, prenom FROM personne;
        requete = "Update personne SET email = %s WHERE id_personne = %s"
        param = (email, id, )
        self.curseur.execute(requete, param)

        self.connexion.commit()        

        self.close() 
    
    def dbSelectInfo(self):
        self.connectBDD()

        requete = "SELECT nom, prenom, photo, email FROM personne"
        self.curseur.execute(requete)
        
        promo = []
        for elt in self.curseur :
            user = Utilisateur(elt[0], elt[1], elt[2], elt[3])
            promo.append(user)

        self.close()

        return promo

