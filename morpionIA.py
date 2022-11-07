#morpiont JvIA V2
from tkinter import * 
from tkinter import messagebox
import tkinter.font as font

window=Tk()
window.configure(bg="black")
window.resizable(height = False, width = False)

window.title("Morpion")
labelf=Label(window, text="Morpion by Ekip", bg="black",fg="orange",)
labels=font.Font(size=19)
labelf['font'] = labels
f=font.Font(size=110)
labelf.grid(row=0, column=2, pady=1, padx=1)
clicked=True
pierre=True
stylo=True
souris=True
bureau=True
papier=True
ciseau=True
compteur=0
## Désactiver tout les bouttons  

def disbld_buttons() : 
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

## Vérification si un joueur a gagné

def gagne() :
    check(b1,b2,b3)
    check(b4,b5,b6)
    check(b7,b8,b9)
    check(b1,b4,b7)
    check(b2,b5,b8)
    check(b3,b6,b9)
    check(b1,b5,b9)
    check(b3,b5,b7)

def check(A,B,C) :
    global compteur
    if A["text"] + B["text"] + C["text"] == "XXX" or A["text"] + B["text"] + C["text"] == "OOO" :
        A.config(bg="green")
        B.config(bg="green")
        C.config(bg="green")
 
        messagebox.showinfo(title=None, message="Fin du jeu ! Bravo, tu as gagné la partie !")
        disbld_buttons()
    else :
        compteur+=1
        if compteur==80:
            egalité()


## Clicks 
def auto1():
    bot(b2,b5,b8)    
def auto2():
    bot(b1,b2,b3)
def auto3():
    bot(b4,b5,b6)
def auto4():
    bot(b7,b8,b9)
def auto5():
    bot(b1,b4,b7)
def auto6():
    bot(b2,b5,b8)
def auto7():
    bot(b3,b6,b9)
def auto8():
    bot(b1,b5,b9)
def auto9():
    bot(b3,b5,b7)

def bot(A,B,C):
    global pierre, stylo, souris, bureau, papier

    if B["text"]==" "  and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        B["text"]="O"
        bureau=False
        pierre=False
    elif A["text"]==" "  and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        A["text"]="O"
        stylo=False
    elif C["text"]==" " and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        C["text"]="O"
        souris=False
def autocontre():
    botcontre(b1,b2,b3)
    botcontre(b4,b5,b6)
    botcontre(b7,b8,b9)
    botcontre(b1,b4,b7)
    botcontre(b2,b5,b8)
    botcontre(b3,b6,b9)
    botcontre(b1,b5,b9)
    botcontre(b3,b5,b7)

def botcontre(A,B,C):
    global ciseau
    if A["text"]+B["text"]+C["text"]=="XX " and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        C["text"]="O"
        ciseau=False
    if A["text"]+B["text"]+C["text"]==" XX" and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        A["text"]="O"
        ciseau=False
    if A["text"]+B["text"]+C["text"]=="X X" and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        B["text"]="O"
        ciseau=False
def autowin():
    botwin(b1,b2,b3)
    botwin(b4,b5,b6)
    botwin(b7,b8,b9)
    botwin(b1,b4,b7)
    botwin(b2,b5,b8)
    botwin(b3,b6,b9)
    botwin(b1,b5,b9)
    botwin(b3,b5,b7)
def botwin(A,B,C):
    global papier, ciseau
    if A["text"]+B["text"]+C["text"]=="OO "  and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        C["text"]="O"
        papier=False
    if A["text"]+B["text"]+C["text"]==" OO" and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        A["text"]="O"
        papier=False
    if A["text"]+B["text"]+C["text"]=="O O"  and not clicked and pierre and stylo and souris and bureau and papier and ciseau:
        B["text"]="O"
        papier=False
def click(b) : 
    global clicked, pierre, stylo, souris, bureau, papier, ciseau, compteur
    if b["text"] == " " and clicked == True : #b["text"] = récupèrer le texte du boutton et checker si == " "
        b["text"] = "X"  #nouveau text = "X"
        clicked=False
        gagne()
    if clicked==False: 
        autowin()
        autocontre()
        auto1()
        auto2()
        auto3()
        auto4()
        auto5()
        auto6()
        auto7()
        auto8()
        auto9()
        clicked=True
        pierre=True
        stylo=True
        souris=True
        bureau=True
        papier=True
        ciseau=True
        gagne()
    else : 
        messagebox.showerror("Morpion", "Cette case est déjà utilisée \nChoisis en une autre ...")
def egalité():
    messagebox.showerror("égalité", "Tu ne gagneras jamais :)")
## Création des boutons 

b1=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b1))   #click(b1) pour envoyer les info du boutton b1 à la fonction click()
b2=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b2))
b3=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b3))

b4=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b4))
b5=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b5))
b6=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b6))

b7=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b7))
b8=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b8))
b9=Button(window, text=" ", height=1, width=2, bg="slate gray", command=lambda : click(b9))


##Création de la grille 

b1.grid(row=1, column=1, pady=0.2, padx=0.2)
b2.grid(row=1, column=2, pady=0.2, padx=0.2)
b3.grid(row=1, column=3, pady=0.2, padx=0.2)

b4.grid(row=2, column=1, pady=0.2, padx=0.2)
b5.grid(row=2, column=2, pady=0.2, padx=0.2)
b6.grid(row=2, column=3, pady=0.2, padx=0.2)

b7.grid(row=3, column=1, pady=0.2, padx=0.2)
b8.grid(row=3, column=2, pady=0.2, padx=0.2)
b9.grid(row=3, column=3, pady=0.2, padx=0.2)



b1['font'] = f
b2['font'] = f
b3['font'] = f
b4['font'] = f
b5['font'] = f
b6['font'] = f
b7['font'] = f
b8['font'] = f
b9['font'] = f

window.mainloop()