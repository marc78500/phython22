# a= int (input("Entrer la valeur pour le coefficient a : "))

# b= int (input("Entrer la valeur pour le coefficient b : "))

# print("la salolution est x = ",-b/a)

age_int = 0
while age_int == 0:
    age_str = input("Quel est votre age? : ")
    try:
        age_int = int(age_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if age_int == 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif age_int < 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            age_int = 0   #je réaffecte 0 à age_int pour revenir à la condition initiale
        elif age_int > 25:
            print("Vous n'êtes pas un peu vieux pour cette formation!?")
            age_int = 0
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez {} ans.".format(age_int))
