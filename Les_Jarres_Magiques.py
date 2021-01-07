import random

print("Bienvenue dans le jeu !...")

# compteur de cles magiques

keys = 0

# reporter les manches de notre jeu


while(keys < 3):
        
    print("vous disposez de 5 jarres devant vous. Choisit 1, 2, 3, 4 ou 5")

    # choix aleatoire de la jarre qui fait perdre notre joueur 
    snake_jar = random.randint(1,5) # nombre au hasard entre 1 et 5
    #demander a notre joueur  de mettre une valeur 

    choix = int(input())  

    while(choix < 0 or choix > 5):
        print("vous ne pouvez choisir des jarres compris entre 1 et 5")
        choix = int(input())  


    print("le joueur a choisis la jarre numero:",choix)


    #verification

    if (choix == snake_jar): #le joueur a perdu
        print("perdu ! un serpent apparait !")
    

        #si le joueur n'a pas de cle  
        
        if(keys > 0):
            keys -=1 
            #print("Tu as actuellement",keys,"/3 cles")
            print(f"Tu as actuellement {keys}/3 cles")
    
    else:
        print("Gagne ! tu obtiens une cle magique ! ")
        print("la jarre infecte etait:",snake_jar)
        keys += 1
        # print("Tu as actuellement",keys,"/3 cles")
        print(f"Tu as actuellement {keys}/3 cles")


print("Tu deviens le rois du temple !...")
 

 
