heuredebut= int(input("Donnez l’heure de début de la location (un entier) :"))
heurefin= int(input("Donnez l’heure de fin de la location (un entier) :"))
result = 0
tarifnormal = 0
tarifmajore = 0

while heuredebut == heurefin or heuredebut>heurefin or heuredebut<0 or heuredebut>24 or heurefin>24 or heurefin<0:
    
    if heuredebut>heurefin:
        print("Attention ! le début de la location est après la fin ...")
        print("\n")
        heuredebut = int(input("Donnez l’heure de début de la location (un entier) :"))
        heurefin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    if heuredebut==heurefin:
        print("Attention ! l’heure de fin est identique à l’heure de début. ")
        print("\n")
        heuredebut = int(input("Donnez l’heure de début de la location (un entier) :"))
        heurefin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    if (heuredebut > 24 or heuredebut < 0) or (heurefin > 24 or heurefin < 0):
        print("Les heures doivent être comprises entre 0 et 24 !")
        print("\n")
        heuredebut = int(input("Donnez l’heure de début de la location (un entier) :"))
        heurefin = int(input("Donnez l’heure de fin de la location (un entier) :"))




for i in range(heuredebut,heurefin):
    
    if i>=7 and i<17:
        result += 2
        tarifmajore += 1
        
    if i<=7 and i>0 or i>=17 and i<24:
        result += 1
        tarifnormal +=1

print("Vous avez loué votre vélo pendant")
print(tarifnormal,"heure(s) au tarif horaire de 1.0 euro(s)")

if tarifmajore > 0:
    
    print(tarifmajore,"heure(s) au tarif horaire de 2.0 euro(s)")
    
print("Le montant total à payer est de",result,"euro(s).")