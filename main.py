from bdd import BDD
import fenetre as f

def main():
    bdd = BDD("localhost", "trombinoscope", "root", "root", 8890)

    tous = bdd.dbSelectInfo()

    f.afficher(tous)

main()