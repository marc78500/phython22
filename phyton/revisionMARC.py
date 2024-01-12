print("calculer le carrer d'un nombre")
debut=int(input("entrer le début de la plage: "))
fin= int(input("entrer la fin plage: "))
somme=0
for nombre in range(debut,fin + 1):
    if nombre%2 ==0:
        somme+= nombre**2
print(f"la somme de carrer de nombre paire est :{somme}")