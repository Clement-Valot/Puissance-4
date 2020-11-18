import numpy as np
import colorama

class Plateau:
    """
    Initialise le plateau de jeu : Une matrice =  Tableau multi-dimensionnel
    """
    def __init__(self):
        #Lien web utilisé : cours OpenclassRoom 
        #https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/4740941-plongez-en-detail-dans-la-librairie-numpy

        """
        Une liste de listes est transformée en un tableau multi-dimensionnel     
        """
        self.size_Ligne = 6
        self.size_Colonne = 12
        self.myMat = np.full((self.size_Ligne, self.size_Colonne), ".", dtype=str)
        #print(type(myMat[0,0])) #Pour s'assurer du type des valeurs dans la matrice
        #ligne, colonne = np.shape(self.myMat) #Récupère les dimensions de la matrice avec numpy
        #print("Nb de ligne de myMat = %d && Nb de colonne = %d" %(ligne,colonne)) #Afficher ces dimensions en précisant des valeurs décimales
        """
        np.full((size_Ligne, size_Colonne), ".", dtype=str)
        *Crée un tableau 6x12 rempli du caratère "." 6 Lignes et 12 colonnes
        *dtype = str : On force le type de donnée en précisant que l'on veut un string
        *np.full((n,p), 5) : Va créer un tableau multi-dimensionnel de dimension n lignes et p colonnes et va remplir chaque case par la valeur 5 qui par défaut est un int
        """

    """
    Affichage de la matrice = Grille de jeu       
    #! SENS D'AFFICHAGE : Du haut vers le bas, gauche à droite => Matrice affichée dans le sens commun donc remplir d'abord le bas de la matrice
    Infos données par les valeurs sur le côté de la matrice : indices de la matrice ligne (vertical) et colonne(horizontal)
    *Lien Web:
        * Actuel : https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
        * Autre possiblité : Tkinter : http://softdmi.free.fr/tuto_python/tuto-python.php?chapitre=2&page=2 
    """
    def __str__(self):
        
        for j in range(0,self.size_Colonne):
            print(("  "+ str(j+1) + " ") if(j<10)else (" " + str(j+1) + " " ), end="") #Num des colonnes (commençant à 1 pr les humains, 0 pr le programme)
            #Léger bricolage : Amélioration possible avec un autre affichage : Tkinter / GUI
        print()
        colorama.init()
        for i in range(0,self.size_Ligne):
            for j in range(0,self.size_Colonne):
                print(colorama.Fore.RESET + "|", end = " ")
                if (self.myMat[i,j] == 'X'):
                    print (colorama.Fore.RED + 'X', sep="",end=" ")
                if (self.myMat[i,j] == 'O'):
                    print (colorama.Fore.YELLOW + 'O', sep="",end=" ")
                if (self.myMat[i,j] == '.'):
                    print ('.', sep="",end=" ")
                #print (self.myMat[i,j], sep="",end=" ") #-> print de base
            print(colorama.Fore.RESET + "|", end = " ")
            #print("| " + str(i), end = " ")       
            print("")
        colorama.deinit()
        for j in range(0,self.size_Colonne*4+1):
            print("-", end="")

        return ''
        
    '''
    #! Surcharge de la fonction setitem, permet de fixer manuellement la valeur d'une case

    @ tuple     tupl    Contient les coordonnées du point auquel on veut attribuer une value
    @ string    value   La value qu'on veut attribuer à la case
    @ None      return
    '''
    def __setitem__(self,tupl,value):
        x,y = tupl
        self.myMat[x,y] = value
        return
    '''
    #! Surcharge de la fonction getitem, permet d'obtenir manuellement la valeur d'une case

    @ tuple     tupl    Contient les coordonnées du point duquel on veut voir la value
    @ string    return  La value contenue dans la case choisie
    '''
    def __getitem__(self,tupl):
        x,y = tupl
        return self.myMat[x,y]


if __name__ == '__main__':
    # Quelques tests
    mat = Plateau()
    #mat[0,0]='X'
    #mat[3,0]='X'
    #print(mat)
    #print(mat[3,0])
    colorama.init()
    print(colorama.Fore.YELLOW + 'ce texte est rouge')
    colorama.deinit()