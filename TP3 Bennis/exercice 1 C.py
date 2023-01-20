liste = []
entier = 0

while len(liste) != 10:
    
    entier = int(input("Veuillez entrer un nombre : "))
    
    if entier < 0 or entier > 20:
        
        entier = int(input("Le nombre doit être compris entre 0 et 20 : "))
        
    else:
        
        liste.append(entier)

inf10 = 0
f10to15 = 0
ab15 = 0

for x in (liste):
    
    if x < 10:
        
        inf10 += 1
        
    elif x >= 10 and x < 15:
        
        f10to15 += 1
        
    elif x >= 15:
        
        ab15 += 1
        
print("\n")

print("Il y a ", inf10, "valeurs < 10.")

print("\n")

print("Il y a ", f10to15, "valeurs >= 10 et < 15.")

print("\n")

print("Il y a ", ab15, "valeurs >= 15.")