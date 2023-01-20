nMax = 3
v1 = []
v2 = []

n = int(input(f"Choisir la taille des vecteur(entre 1 et {nMax})"))

while n < 1 or n > nMax:
    n = int(input(f"La taille des vecteurs n'est pas valide (entre 1 et {nMax}"))

for i in range(n):
    v1.append(int(input(f"Entrez la composante v1[{1}]")))
    v2.append(int(input(f"Entrez la composante v2[{1}]")))

produit_Scalable = 0
for i in range(n):
    produit_Scalable += v1[1] * v2[1]

print(f"Le produit scalaire de v1 par v2 vaut {produit_Scalable}")

