nombre = int(input("Veuillez entrer un nombre : "))
nbreorig = nombre

liste = []

factorielle = 1

while nombre != 0:
    
    liste.append(nombre)
    
    nombre -= 1

ask = input("Voulez-vous utiliser une boucle While ou For (while / for) ? ")


if ask == "while":
    
    x = 1
    
    while x <= len(liste):
        
        factorielle = factorielle * x
        
        x = x + 1
    

if ask == "for":
    
    factorielle = 1
    
    for x in range(len(liste)):
    
        factorielle *= liste[x]


print("La factorielle de", nbreorig, "est", factorielle, ".")