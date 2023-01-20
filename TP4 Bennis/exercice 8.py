dico={}

dico['firstname']="Mathéo"
dico['lastname']="Roesch"
dico['promo']="RT1"
dico['group']="rt122"

print(f"Mon nom est {dico['firstname']} {dico['lastname']} de la promo {dico['promo']} et du groupe {dico['group']}")
input("Continuer\n")

print(f"Les clefs du dico sont:\n-{list(dico.keys())[0]}\n-{list(dico.keys())[1]}\n-{list(dico.keys())[2]}\n-{list(dico.keys())[3]}")
print(f"Les valeurs du dico sont:\n-{list(dico.values())[0]}\n-{list(dico.values())[1]}\n-{list(dico.values())[2]}\n-{list(dico.values())[3]}")
print(f"Les Tuplets du dico sont:\n-{list(dico.items())[0]}\n-{list(dico.items())[1]}\n-{list(dico.items())[2]}\n-{list(dico.items())[3]}")

input("Continuer\n")

dico2={}

dico2['firstname']="Matheo"
dico2['lastname']="Roesch"
dico2['promo']="RT1"
dico2['group']="rt122"

binome={}

binome['Matheo']=dico
binome['Henry']=dico2

print(f"Les étudiants formants le binôme sont:\n-L'étudiant {binome['Henry']['firstname']} du groupe {binome['Henry'] ['group']}\n- L'étudiant {binome['Matheo']['firstname']} du groupe {binome['Matheo'] ['group']}")
