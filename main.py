mot = "Udemy"
     
resultat = []
     
for lettre in reversed(mot):
        resultat.append(lettre)
     
resultat_formate = "".join(resultat)
print(resultat_formate.capitalize())