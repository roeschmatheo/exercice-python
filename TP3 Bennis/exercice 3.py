from random import*

alea = randint(0,100)

guess = -1

compteur = 0

while guess != alea:

    guess = int(input("Veuiller deviner le nombre : "))

    compteur +=1

    if guess < alea:

        print("Trop petit !")

    elif guess > alea:

            print("Trop grand !")

    elif guess == alea:

        print("Felicitation")

        break

print("\n")

print("Vous avez réussi au bout de ", compteur, "essais !")



