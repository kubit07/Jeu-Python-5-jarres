import random

key = 0


while (key < 3):

    print("Bienvenue dans le jeu !....")

    print("Vous disposez de 5 jarres devant vous veuillez faire un choix:")

    print("jarre 1")
    print("jarre 2")
    print("jarre 3")
    print("jarre 4")
    print("jarre 5")

    choix = int(input("veuillez choisir:"))

    while(choix<1 or choix >5):
        print("vous ne pouvez faire qu'un choix compris entre 1 et 5")
        choix = int(input("veuillez choisir:"))

    snake_jarre = random.randint(1,5)

    print(f"Vous avez choisis la jarre numero:{choix}")


    if (choix==snake_jarre):
        print("perdu ! un serpent apparait !...")
        if(key > 0):
            key -= 1
            print(f"Actuellement tu as {key}/3")

    else:
        
        print("Gagne ! tu obtiens une cle magique !...")
        print("la jarre infecte etait:",snake_jarre)
        print("une cle vient de s'ajouter a ton trousseau magique")
        key += 1
        print(f"Actuellement tu as {key}/3")
        

print("Tu deviens le Rois du temple")


