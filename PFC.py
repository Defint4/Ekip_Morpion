import random
import webbrowser
import time
import os


def menu():
    jeu = int(input("\nChoissez le mode de jeu\n 1:Mode normal \n 2:Mode impossible (•̀ᴗ•́ )و ̑̑ \n 3:Quitter \n"))
    if jeu == 1:
        pfcnormal()
    if jeu == 2:
        impossible_mode()
    if jeu == 3:
        return
    else:
        print("\n\n\nCe mode est en cours de développement..../!\ \n")
        return menu()
def pfcnormal():
    points1 = 0
    points2 = 0
    cpt = 0
    choix=["Pierre","Feuille","Ciseaux"]
    print("Bienvenue dans le niveau normal \n Bonne chance !\n")
    manches = int(input("En combien de manches voulez vous jouer ?\n"))
    
    while cpt < manches:
        coup = input(str("Choisissez votre coup: Pierre,Feuille,Ciseaux \n"))
        coup2 = random.choice(choix)

        if cpt == manches-1 and points1 == points2 and manches >=5:
            os.system('clear')
            time.sleep(1.2)
            print("\n \n \n Trou noir \n \n \n")
            time.sleep(3)
            print("\n \n Allô.. ? Vous êtes toujours là ? \n \n")
            time.sleep(3)
            print("\n \n La partie a été aspirée par un énorme trou noir, impossible de la récupérer..")
            time.sleep(3)
            print("\n\n Je crois bien que vous avez perdu... Je vous renvoie au menu principal\n \n")
            menu()


        if coup == coup2:
            print("\n Egalité")
        if coup == "Puit" or coup =="Puits" or coup == "Pui" or coup =="Volcan" or coup == "puit":
            os.system('clear')
            print("\n \n Tu n'essayes quand même pas de tricher ?? \n")
            time.sleep(1.2)
            webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')
            print("\n Hop un  rick roll bien mérité\n")
            menu()

        if coup == "Pierre" and coup2 == "Feuille":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Pierre" and coup2 == "Ciseaux":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Feuille" and coup2 == "Pierre":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Feuille" and coup2 == "Ciseaux":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Ciseaux" and coup2 == "Pierre":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Ciseaux" and coup2 == "Feuille":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if points1 > points2:
            cpt = points1
        else:
            cpt = points2
    if points1 > points2:
        print("Bravo vous avez gagné !")
    else:
        print("Dommage vous avez perdu....")
    
    a = int(input("Voulez-vous rejouer ? \n 1:Oui \n 2:Non \n"))
    if a == 1:
        return pfcnormal()
    else:
        return


def impossible_mode():
    
    points1 = 0
    points2 = 0
    cpt = 0
    print("Bienvenue dans le mode impossible (•̀ᴗ•́ )و ̑̑ \n \nBon courage...\n")
    choix=["Pierre","Feuille","Ciseaux"]
    manches = int(input("En combien de manches voulez vous jouer ?\n"))
    
    while cpt < manches:
        coup = input(str("Choisissez votre coup: Pierre,Feuille,Ciseaux \n"))
        if coup == "Pierre":
            dico = ["Feuille","Feuille","Feuille","Pierre","Pierre","Ciseaux"]
            coup2 = random.choice(dico)
        if coup == "Feuille":
            dico = ["Ciseaux","Ciseaux","Ciseaux","Feuille","Feuille","Pierre"]
            coup2 = random.choice(dico)
        if coup == "Ciseaux":
            dico = ["Pierre","Pierre","Pierre","Ciseaux","Ciseaux","Feuille"]
            coup2 = random.choice(dico)
        if coup == coup2:
            print("\n Egalité")
        if coup == "Pierre" and coup2 == "Feuille":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Pierre" and coup2 == "Ciseaux":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Feuille" and coup2 == "Pierre":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Feuille" and coup2 == "Ciseaux":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Ciseaux" and coup2 == "Pierre":
            points2 = points2 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if coup == "Ciseaux" and coup2 == "Feuille":
            points1 = points1 + 1
            print("    ",coup,"     ",coup2)
            print("Joueur 1:   ",points1,"   Joueur 2:    ",points2)
        if points1 > points2:
            cpt = points1
        else:
            cpt = points2
    if points1 > points2:
        print("Bravo vous avez gagné !")
    else:
        print("Dommage vous avez perdu....")
    
    a = int(input("Voulez-vous réessayer (•̀ᴗ•́ )و ̑̑ ? \n 1:Oui \n 2:Non \n"))
    if a == 1:
        return impossible_mode()
    else:
        return



menu()
