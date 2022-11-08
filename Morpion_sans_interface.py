import random

def init():
    tab = [' '] * 9
    liste = [0,1,2,3,4,5,6,7,8]
    print('[',tab[0],',',tab[1],',',tab[2],']\n[',tab[3],',',tab[4],',',tab[5],']\n[',tab[6],',',tab[7],',',tab[8],']\n')
    return tab,liste

def player1(tab,liste):
    a = int(input("Choisissez la case entre 1 et 9\n"))
    if tab[a-1] == ' ':
        tab[a-1] = '0'
        liste.remove(a-1)

    else:

        print('Cette case est déjà utilisée, veuillez recommencer')
        return player1(tab)

    print('[',tab[0],',',tab[1],',',tab[2],']\n[',tab[3],',',tab[4],',',tab[5],']\n[',tab[6],',',tab[7],',',tab[8],']\n')
    return tab,liste

def player2(tab,liste):
    b = int(input("Choisissez la case entre 1 et 9\n"))
    if tab[b-1] == ' ':
        tab[b-1] = 'X'
        liste.remove(b-1)
    else:
        print('Cette case est déjà utilisée, veuillez recommencer')
        return player2(tab)
        
    print('[',tab[0],',',tab[1],',',tab[2],']\n[',tab[3],',',tab[4],',',tab[5],']\n[',tab[6],',',tab[7],',',tab[8],']\n')
    return tab,liste





def morpion():
    print("\nNouvelle partie !\n")
    tab,liste = init()
    coups = 0
    win1 = False
    win2 = False
    while win1 == False and win2 == False and coups < 9:
        player1(tab,liste)
        coups = coups + 1
        win1 = gagnant1(tab)
        if win1 == True:
            print('\nLe joueur 1 a gagné !\n')
            break
        if coups == 9:
            print('\nEgalité')
            break
        player2(tab,liste)
        coups = coups + 1
        win2 = gagnant2(tab)
        if win2 == True:
            print('\nLe joueur 2 a gagné !\n')
            break
            
    r = int(input('Voulez-vous rejouer ? \n1:Oui \n2:Non\n'))
    if r == 1:
        morpion()
    else:
        return

def gagnant1(tab):
    win = False
    if (tab[0] == tab[1] == tab[2] == '0') or (tab[3] == tab[4] == tab[5] == '0') or (tab[6] == tab[7] == tab[8] == '0') or (tab[0] == tab[3] == tab[6] == '0') or (tab[1] == tab[4] == tab[7] == '0') or (tab[2] == tab[5] == tab[8] == '0') or (tab[0] == tab[4] == tab[8] == '0') or (tab[2] == tab[4] == tab[6] == '0'):
        win = True
    return win

def gagnant2(tab):
    win = False
    if (tab[0] == tab[1] == tab[2] == 'X') or (tab[3] == tab[4] == tab[5] == 'X') or (tab[6] == tab[7] == tab[8] == 'X') or (tab[0] == tab[3] == tab[6] == 'X') or (tab[1] == tab[4] == tab[7] == 'X') or (tab[2] == tab[5] == tab[8] == 'X') or (tab[0] == tab[4] == tab[8] == 'X') or (tab[2] == tab[4] == tab[6] == 'X'):
        win = True
    return win

morpion()