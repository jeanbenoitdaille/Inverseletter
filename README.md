# Inverseletter
Inverser les lettres d'un mot 
Tout d'abord, commençons par dire qu'il est possible de réaliser cet exercice en une seule ligne, avec les slices :

    >>> mot = "Udemy"
    >>> print("Udemy"[::-1].capitalize())
    "Ymedu"

Mais pour faire durer un peu le plaisir, je vous montre une façon de faire un peu moins directe et qui vous permettra d'utiliser un peu plus de fonctions natives de Python.

Tout d'abord, pour inverser l'ordre des lettres, nous utilisons la fonction reversed :

    >>> mot = "Udemy"
    >>> print(reversed(mot))
    <reversed object at 0x10386b278>

Cette fonction nous retourne un object 'reversed', qui est en fait un itérateur. Nous pouvons donc passer à travers cet itérateur avec une boucle for et ajouter chaque lettre dans une liste :

    for lettre in reversed(mot):
        resultat.append(lettre)

Nous nous retrouvons ainsi avec une liste contenant chaque lettre dans l'ordre inverse.

Pour terminer, nous pouvons utiliser la fonction join pour joindre les éléments de la liste ensemble et la fonction capitalize pour mettre une majuscule au début du mot :

    resultat_formate = "".join(resultat)
    print(resultat_formate.capitalize())
