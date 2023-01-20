a=input("entrez la première valeur: ")
b=input("entrez la deuxième valeur: ")
c=input("entrez la troisième valeur: ")

print("les valeurs d'entrées sont : a = " + a + ", b = " + b + ", et c = " + c)
print("permutation: a ==> b, b ==> c, c ==> a")

aa = a
bb = b
cc = c

b = a
c = bb
a = cc
      
print("Les valeurs permutters sont: a = " + a + ", b = " + b + ", et c = " + c)
