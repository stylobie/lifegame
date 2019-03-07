def creerLigneGrille(nombreColonnes) :
    return [0 for i in range(nombreColonnes)]

    
def creerGrille(nombreLignes, nombreColonnes) :
    return [ creerLigneGrille(nombreColonnes) for i in range(nombreLignes)]


def donneNombreColonnes(grille) :
    ligne = grille[0];
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
        raise IndexError('coordonnées invalides')
    
    
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









m = creerGrille(10, 10)
creerCellule(m, 2, 3) ;
creerCellule(m, 2, 4)
creerCellule(m, 2, 5) ;
creerCellule(m, 2, 5)
pg(m)
print(compterLesVoisins(m, 1, 4))
m = donneGenerationSuivante(m)
pg(m)
m = donneGenerationSuivante(m)
pg(m)
m = donneGenerationSuivante(m)
pg(m)
m = donneGenerationSuivante(m)
pg(m)
m = donneGenerationSuivante(m)
pg(m)
m = donneGenerationSuivante(m)
pg(m)