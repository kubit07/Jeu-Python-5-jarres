import random

print("Bienvenue dans le jeu !...")

# choix du parametrage du niveau de diffuculte


print("Niveau 1 : Facile")
print("Niveau 2 : Moyen")
print("Niveau 3 : Difficile")

level = int(input("Veuillez choisr votre niveau du jeu:"))


# compteur de cles magiques

keys = 0

# reporter les manches de notre jeu


while(keys < 3):
        
    print("vous disposez de 5 jarres devant vous. Choisit 1, 2, 3, 4 ou 5")

    # tableau qui va contenir chacune des jarres 

    jarres = ['U','U','U','U','U']

    # boucle qui va tourner autant de fois qu'il doit y avoir de serpents
    for i in range(0 ,level):
        print("1 serpent a ete ajoute dans la jarre")
        jarres[i] = 'S'

# melange les  jarres
    random.shuffle(jarres)     

    #demander a notre joueur  de mettre une valeur 

    choix = int(input())  

    while(choix < 0 or choix > 5):
        print("vous ne pouvez choisir des jarres compris entre 1 et 5")
        choix = int(input())  


    print("le joueur a choisis la jarre numero:",choix)


    #verification

    
    if (jarres[choix-1 ]=='U'): # le joueur a gagne
        print("Gagne ! tu obtiens une cle magique ! ")
       # print("la jarre infecte etait:")
        keys += 1
        # print("Tu as actuellement",keys,"/3 cles")
        print(f"Tu as actuellement {keys}/3 cles")

    
    else: #le joueur a perdu
        print("perdu ! un serpent apparait !")
    

        #si le joueur n'a pas de cle  
        
        if(keys > 0):
            keys -=1 
            #print("Tu as actuellement",keys,"/3 cles")
            print(f"Tu as actuellement {keys}/3 cles")
    


print("Tu deviens le rois du temple !...")
 

 
