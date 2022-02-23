
class Utilisateur:
    
    def __init__(self, nom, prenom, photo, email):
        self.nom = nom
        self.prenom = prenom
        self.photo = photo
        self.email = email

    def formater_nom(self):
        return(self.nom + " " + self.prenom)

    def formater_image(self) :
         return(".\\trombi\\" + self.photo + ".jpg")
       