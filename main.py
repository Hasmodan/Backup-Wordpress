import os
from MODULEMENU import monmenustyle
from MODULEDEF import copywordpress, restitution, supprimerlebackup,byebye


L1 = ["Sauvegarde du site web", "Restauration du site", "Supprimer le backup","Quitter le script"]
# j ai ajoute la ligne suivante
continu = 'm'


# j ai ajoute le while a la ligne suivante
while continu == 'm':
    nbr = 1
    os.system('cls')
    monmenustyle()
    for decision in L1:
        print(nbr, "-> ", decision, )
        nbr += 1

    print("\n" "Quels est ton choix""\n")
    choix: int = int(input("choix : "))

    if choix > 0 and choix <= len(L1):
        print("Vous avez choisi : ", L1[choix - 1])
        if choix == 1:
            copywordpress()
        if choix == 2:
            restitution()
        if choix == 3:
            supprimerlebackup()
        if choix == 4:
            byebye()

    else:
        print("Ce choix là est IMPOSSIBLE")
    # j ai ajoute la ligne ci-dessous
    continu = input("\nVoulez-vous revenir sur le menu principal (M = Menu , p = partir) ?")
