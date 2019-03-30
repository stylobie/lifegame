# coding=utf-8

import tkinter as tk


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def estEgale(self, autrePosition):
        return (self.x == autrePosition.x and self.y == autrePosition.y)

    def estContenue(self, liste):
        for p in liste:
            if p.estEgale(self):
                return True
        return False


class Grille:
    def __init__(self, nombreLignes, nombreColonnes):
        self.nombreLignes = nombreLignes
        self.nombreColonnes = nombreColonnes
        self.cellules = []

    def __repr__(self):
        return self.cellules.__repr__()

    def ajouterCellule(self, position):
        if not (self.estCelluleVivante(position)):
            self.cellules.append(position)

    def ajouterCellules(self, positions):
        for p in positions:
            self.ajouterCellule(p)

    def supprimerCellule(self, position):
        if self.estCelluleVivante(position):
            self.cellules.remove(position)

    def estCelluleVivante(self, position):
        return position.estContenue(self.cellules)

    def compterLesVoisins(self, position):
        compteur = 0
        for ligne in range(position.x - 1, position.x + 2):
            for colonne in range(position.y - 1, position.y + 2):
                if not(ligne == position.x and colonne == position.y):
                    positionVoisine = Position(ligne, colonne)
                    if self.estCelluleVivante(positionVoisine):
                        compteur += 1
        return compteur

    def donnerGenerationSuivante(self):
        generationSuivante = Grille(self.nombreLignes, self.nombreColonnes)
        positionsInteressantes = []
        for position in self.cellules:
            for ligne in range(position.x - 1, position.x + 2):
                for colonne in range(position.y - 1, position.y + 2):
                    positionInteresante = Position(ligne, colonne)
                    if not(positionInteresante.estContenue(positionsInteressantes)):
                        positionsInteressantes += [positionInteresante]

        for position in positionsInteressantes:
            nombreCellulesVivantesVoisines = self.compterLesVoisins(position)
            if nombreCellulesVivantesVoisines < 2 or nombreCellulesVivantesVoisines > 3:
                # rien à faire car la nouvelle grille est vide au départ
                pass
            elif nombreCellulesVivantesVoisines == 3:
                generationSuivante.ajouterCellule(position)
            elif self.estCelluleVivante(position):
                generationSuivante.ajouterCellule(position)
        return generationSuivante


# def play(grila):
#     while True :
#         deseneaza(grila)
#         grila = grila.donnerGenerationSuivante()
#         if stopRequested:
#             break
count = 5
c = Position(2, 2)
d = Position(2, 3)
e = Position(2, 4)

g = Grille(10, 10)
g.ajouterCellule(c)
g.ajouterCellules([d, e])

base = tk.Tk()
fenetre = tk.Frame(base)
marge = 0
margeGrille = 0
largeurGrille = 500
hauteurGrille = 500
grosseurTrait = 1
fenetre.pack(side="top", fill="both", expand=True, padx=marge, pady=marge)
canvas = tk.Canvas(fenetre, width=largeurGrille + margeGrille + grosseurTrait,
                   height=hauteurGrille + margeGrille + grosseurTrait, background="white")
canvas.pack(side="top", anchor="c")

arretDemande = False


def dessiner(grille, canvas, largeurGrille, hauteurGrille, grosseurTrait):
    nombreColonnes = grille.nombreColonnes
    nombreLignes = grille.nombreLignes
    grosseurTrait = 1
    canvas.delete("cellule")
    for ligne in range(nombreLignes):
        for colonne in range(nombreColonnes):
            position = Position(ligne, colonne)
            if grille.estCelluleVivante(position):
                canvas.create_rectangle((ligne*largeurGrille)/nombreColonnes + grosseurTrait, (colonne*hauteurGrille)/nombreLignes + grosseurTrait, ((
                    ligne + 1)*largeurGrille)/nombreColonnes + 1, ((colonne + 1)*hauteurGrille)/nombreLignes + 1, fill="black", tags="cellule")


def lancer():
    global arretDemande
    arretDemande = False
    while True:
        global g
        g = g.donnerGenerationSuivante()
        dessiner(g, canvas, largeurGrille, hauteurGrille, grosseurTrait)
        # if arretDemande:
        break


def arreter():
    global arretDemande
    arretDemande = True


b = tk.Button(fenetre, text="Lancer", command=lancer)
b.pack(side="top", anchor="c")
b = tk.Button(fenetre, text="Arrêter", command=arreter)
b.pack(side="top", anchor="c")
nombreColonnes = g.nombreColonnes
nombreLignes = g.nombreLignes
for i in range(nombreColonnes + 1):
    xLigne = (i * largeurGrille) / nombreColonnes + grosseurTrait + 1
    canvas.create_line(xLigne, 0, xLigne, hauteurGrille +
                       grosseurTrait, width=grosseurTrait, fill="black")
for i in range(nombreLignes + 1):
    yLigne = (i * hauteurGrille) / nombreLignes + grosseurTrait + 1
    canvas.create_line(0, yLigne, largeurGrille + grosseurTrait,
                       yLigne, width=grosseurTrait, fill="black")
    dessiner(g, canvas, largeurGrille, hauteurGrille, grosseurTrait)

base.mainloop()


"""def creerLigneGrille(nombreColonnes) :
    return [0 for i in range(nombreColonnes)]

    
def creerGrille(nombreLignes, nombreColonnes) :
    return [ creerLigneGrille(nombreColonnes) for i in range(nombreLignes)]


def donneNombreColonnes(grille) :
    ligne = grille[0]
    return len(ligne) 


def donneNombreLignes(grille) :
    return len(grille)


def estDansLaGrille(grille, x, y) :
    nombreColonnes= donneNombreColonnes(grille)
    nombreLignes = donneNombreLignes(grille)
    return x < nombreLignes and y < nombreColonnes and x >= 0 and y >= 0


def setValeur(grille, x, y, valeur) :
    if estDansLaGrille(grille, x, y) :
        grille[x][y] = valeur
    else :
        raise IndexError('coordonn�es invalides')
    
    
def creerCellule(grille, x, y) :
    setValeur(grille, x, y, 1)


def detruireCellule(grille, x, y) :
    setValeur(grille, x, y, 0) 

def estCelluleVivante(grille, x, y) :
    return estDansLaGrille(grille, x, y) and (grille[x][y] == 1)


def compterLesVoisins(grille, x, y) :
    compteur = 0
    for ligne in range(x - 1, x + 2):
        for colonne in range(y - 1, y + 2) :
            if ((x != ligne) or (y != colonne)) and estDansLaGrille(grille, ligne, colonne) and estCelluleVivante(grille, ligne, colonne) :
                compteur += 1
    return compteur 
                
def donneGenerationSuivante(grille) :
    nombreColonnes= donneNombreColonnes(grille)
    nombreLignes = donneNombreLignes(grille)
    nouvelleGeneration = creerGrille(nombreLignes, nombreColonnes)
    for ligne in range(nombreLignes) :
        for colonne in range(nombreColonnes) :
            nombreCellulesVivantesVoisines = compterLesVoisins(grille, ligne, colonne)
            if nombreCellulesVivantesVoisines < 2 or nombreCellulesVivantesVoisines > 3 :
                detruireCellule(nouvelleGeneration, ligne, colonne)
            elif nombreCellulesVivantesVoisines  == 3 :
                creerCellule(nouvelleGeneration, ligne, colonne)
            else :
                nouvelleValeur = grille[ligne][colonne]
                setValeur(nouvelleGeneration, ligne, colonne, nouvelleValeur)
    return nouvelleGeneration
            

def pg(grille) :
    nombreColonnes= donneNombreColonnes(grille)
    nombreLignes = donneNombreLignes(grille)
    nouvelleGeneration = creerGrille(nombreLignes, nombreColonnes)
    for ligne in range(nombreLignes) :
        s = ''
        for colonne in range(nombreColonnes) :    
            if grille[ligne][colonne] == 1 :
                s += 'x   '
            else :
                s += '.   '
        s= s + '\n' 
        print(s)

def initialiserGrille(grille) :
    nombreColonnes= donneNombreColonnes(grille)
    nombreLignes = donneNombreLignes(grille)
    base = tk.Tk()
    fenetre = tk.Frame(base)
    marge = 0
    margeGrille = 0
    largeurGrille = 500 
    hauteurGrille = 500
    grosseurTrait = 1
    fenetre.pack(side="top", fill="both", expand=True, padx=marge, pady = marge)
    canvas = tk.Canvas(fenetre, width=largeurGrille + margeGrille + grosseurTrait,
                                height=hauteurGrille + margeGrille + grosseurTrait, background="white")
    canvas.pack(side="top", anchor="c")
    for i in range(nombreColonnes + 1) :
        xLigne = (i * largeurGrille) / nombreColonnes + grosseurTrait + 1
        canvas.create_line(xLigne, 0, xLigne, hauteurGrille + grosseurTrait, width = grosseurTrait, fill="black")
    for i in range(nombreLignes + 1) :
        yLigne = (i * hauteurGrille) / nombreLignes + grosseurTrait + 1
        canvas.create_line(0, yLigne, largeurGrille + grosseurTrait, yLigne, width = grosseurTrait, fill="black")
    for ligne in range(nombreLignes) :
        for colonne in range(nombreColonnes) :
            if grille[ligne][colonne] == 1 :
                canvas.create_rectangle((ligne*largeurGrille)/nombreColonnes + grosseurTrait, (colonne*hauteurGrille)/nombreLignes + grosseurTrait, ((ligne +1)*largeurGrille)/nombreColonnes + 1, ((colonne + 1)*hauteurGrille)/nombreLignes + 1, fill="black", tags="square")
        
    base.mainloop()

m = creerGrille(10, 10)
creerCellule(m, 2, 3) 
creerCellule(m, 2, 4)
creerCellule(m, 2, 5)
# initialiserGrille(m)"""


"""m = creerGrille(10, 10)
creerCellule(m, 2, 3) ;
creerCellule(m, 2, 4)
creerCellule(m, 2, 5) ;
creerCellule(m, 2, 5)
m = donneGenerationSuivante(m)
pg(m)"""
