#Créez un programme demandant à l'utilisateur un animal
#, une couleur et un lieu et retournez-lui la phrase suivante: 
# J'ai trouvé un (nom de l'animal) de couleur (nom de la couleur) 
# dans mon lieu préféré: (nom du lieu). Implémentez la fonction de 
# sorte qu'elle ne prenne qu'un seul paramètre pour représenter les 
# trois mots de l'utilisateur.

def phrase_complet():
   
    animal = input("Veuillez entrer un animal : ")
    couleur = input("Veuillez entrer une couleur : ")
    lieu = input("Veuillez entrer un endroit : ")

    print(f"J'ai trouvé un {animal} de couleur {couleur} dans mon lieu prefere {lieu}")
    return None

phrase_complet()
phrase_complet()
phrase_complet()