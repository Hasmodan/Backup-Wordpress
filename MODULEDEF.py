import os
import shutil


def copywordpress():
    try:
        os.mkdir('/Users/kaillros/Desktop/LEBACKUP')
        shutil.make_archive('/Users/kaillros/Desktop/LEBACKUP/BACKUPWORDPRESS', 'zip', 'C:\\wordpress')
        print("Fichier copié avec succès!!! jette un oeil sur ton bureau, ton backup est là ;) ")
    except shutil.SameFileError:
        print("La source et la destination représentent le même fichier")
    except PermissionError:
        print("Permission refusée problème de droit?")
    except:
        print("Tu possède déjà une copie sur ton bureau ;)")


def restitution():
    try:
        shutil.unpack_archive('/Users/kaillros/Desktop/LEBACKUP/BACKUPWORDPRESS.zip', 'C:\\wordpress', "zip")
        print("La restitution est ok!!! -> C:\wordpress")
    except shutil.SameFileError:
        print("La source et la destination représentent le même fichier")
    except PermissionError:
        print("Permission refusée problème de droits?")
    except:
        print("Une erreur s'est produite durant la restitution")

def supprimerlebackup():
    try:
        shutil.rmtree('/Users/kaillros/Desktop/LEBACKUP/')
        print("Il fallait le supprimer pour le bien du peuple il avait la rage =D ")
    except:
        print("Hmm compliquer de supprimer quelque chose qui n'existe plus ;)")

def byebye():
    print("Le problème ce n'est pas toi mais moi j'ai besoin d'espace entre nous, cela dit tu m'donne le num de ta cousine ")
    exit()

