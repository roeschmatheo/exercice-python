entier = int(input("Veuillez entrer un nombre : "))

liste = []
somme = 0

while entier != 0:
    
    liste.append(entier)
    entier -= 1

for x in range(len(liste)):
    somme += liste[x]

print(somme)