import Fonctions_de_base
import Initialisation
import time
from shutil import get_terminal_size #pour fonction clear

import time

#!Section copiée/Collée de AlphaBetaMiniMax

''' 
Renvoie le meilleur play à faire suivant le state donné en considérant que l'adversaire va faire les plays optimum
mais ici on va élaguer des options afin de gagner en rapidité d'exécution

@ state     Une liste de liste au format d'un tabelau multi-dimensionnel avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ nb_jetons Nombre de jetons qui ont déjà été joué
@ return    Une action optimale à faire par le joueur
'''
def Alpha_Beta(state,joueur,max_Depth, joueur_Pourcentage, nb_jetons):
    if(joueur == 'X') : opposant = 'O'
    if(joueur == 'O') : opposant = 'X'
    resultat = Max_Value_Alpha_Beta(state,joueur,opposant, -10000000000, 10000000000, 0, max_Depth, joueur_Pourcentage, nb_jetons)
    return resultat


"""
Reflexion pour le tour de l'opposant, qui va prendre l'action qui a le gain minimum pour le joueur avec la méthode alpha beta (plus opti)

@ state     Une liste de liste au format d'un tabelau multi-dimensionnel avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ alpha     La valeur max déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure alpha
@ beta      La valeur min déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure beta
@ prof_act  La profondeur actuelle
@ prof_max  La profondeur max a laquelle on descend   
@ nb_jetons Nombre de jetons qui ont déjà été joué
@ return    La valeur de l'utility d'un état
"""

def Min_Value_Alpha_Beta(state,joueur,opposant,alpha,beta,prof_act,prof_max,pourcentage_amplitude,nb_jetons):
    if(Fonctions_de_base.Terminal_Test(state,nb_jetons) or prof_act==prof_max) : return Fonctions_de_base.Utility_Vincent_Remi(state,joueur,opposant)
    prof_act+=1
    nb_jetons+=1
    #valeur infiniment haute
    v = 10000000000
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour

    #! Diminution de l'amplitude de l'arbre

    liste_value=[]
    liste_action = []
    for a in Fonctions_de_base.Action(state):
        value = Fonctions_de_base.Utility_Vincent_Remi(Fonctions_de_base.Result(state,a,opposant), joueur, opposant)
        liste_value.append(value)
        liste_action.append(a)

    # * ON PEUT MODIFIER LE POURCENTAGE
    # * ON PREND LES % PIRES PLAYS CAR C'EST L'ADVERSAIRE QUI JOUE
    # * ON GAGNE AINSI DU TEMPS ET ON NE REGARDE PAS LES PLAYS ININTERESSANTS

    liste_action_conservees = []
    for i in range(int(len(liste_value)*pourcentage_amplitude)):
        index_value_min = liste_value.index(min(liste_value))
        liste_action_conservees.append(liste_action[index_value_min])
        del liste_value[index_value_min]
        del liste_action[index_value_min]

    #! FIN Diminution de l'amplitude de l'arbre

    for a in liste_action_conservees:
        v = min(v,Max_Value_Alpha_Beta(Fonctions_de_base.Result(state,a,opposant),joueur,opposant,alpha,beta,prof_act,prof_max,pourcentage_amplitude, nb_jetons))
        if (v <= alpha) : return v
        beta = min(beta,v)
    return v


'''
Reflexion pour le tour du joueur, qui va prendre l'action qui a le gain maximum pour lui avec la méthode alpha beta (plus opti)

@ state     Une liste de liste au format d'un tabelau multi-dimensionnel avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ alpha     La valeur max déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure alpha
@ beta      La valeur min déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure beta
@ prof_act  La profondeur actuelle
@ prof_max  La profondeur max a laquelle on descend  
@ nb_jetons Nombre de jetons qui ont déjà été joué
@ return            La valeur de l'utility d'un état (+ l'action associée)
'''


def Max_Value_Alpha_Beta(state,joueur,opposant,alpha,beta, prof_act,prof_max, pourcentage_amplitude, nb_jetons):
    if(Fonctions_de_base.Terminal_Test(state,nb_jetons) or prof_act==prof_max ) : return Fonctions_de_base.Utility_Vincent_Remi(state,joueur,opposant)
    prof_act+=1
    nb_jetons+=1
    #valeur infiniment basse
    v = -1000000000000
    if(prof_act==1):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour

        #! Diminution de l'amplitude de l'arbre

        liste_value=[]
        liste_action = []
        for a in Fonctions_de_base.Action(state):
            value = Fonctions_de_base.Utility_Vincent_Remi(Fonctions_de_base.Result(state,a,joueur), joueur, opposant)
            liste_value.append(value)
            liste_action.append(a)

        # * ON PEUT MODIFIER LE POURCENTAGE
        # * ON PREND LES % MEILLEURS PLAYS CAR C'EST L'IA QUI JOUE
        # * ON GAGNE AINSI DU TEMPS ET ON NE REGARDE PAS LES PLAYS ININTERESSANTS
        liste_action_conservees = []
        for i in range(int(len(liste_value)* pourcentage_amplitude )):
            index_value_min = liste_value.index(max(liste_value))
            liste_action_conservees.append(liste_action[index_value_min])
            del liste_value[index_value_min]
            del liste_action[index_value_min]

        #! FIN Diminution de l'amplitude de l'arbre

        for a in liste_action_conservees:
            ancien_v = v
            v = max(v,Min_Value_Alpha_Beta(Fonctions_de_base.Result(state,a,joueur),joueur,opposant,alpha,beta,prof_act,prof_max,pourcentage_amplitude, nb_jetons))
            if(ancien_v < v): sauvegarde_action=a
            if (v >= beta) : return [v,sauvegarde_action]
            alpha = max(alpha,v)
        return [v,sauvegarde_action]
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour

    #! Diminution de l'amplitude de l'arbre

    liste_value=[]
    liste_action = []
    for a in Fonctions_de_base.Action(state):
        value = Fonctions_de_base.Utility_Vincent_Remi(Fonctions_de_base.Result(state,a,joueur), joueur, opposant)
        liste_value.append(value)
        liste_action.append(a)

    # * ON PEUT MODIFIER LE POURCENTAGE
    # * ON PREND LES % MEILLEURS PLAYS CAR C'EST L'IA QUI JOUE
    # * ON GAGNE AINSI DU TEMPS ET ON NE REGARDE PAS LES PLAYS ININTERESSANTS

    liste_action_conservees = []
    for i in range(int(len(liste_value)*pourcentage_amplitude)):
        index_value_min = liste_value.index(max(liste_value))
        liste_action_conservees.append(liste_action[index_value_min])
        del liste_value[index_value_min]
        del liste_action[index_value_min]
    
    #! FIN Diminution de l'amplitude de l'arbre

    for a in liste_action_conservees:
        v = max(v,Min_Value_Alpha_Beta(Fonctions_de_base.Result(state,a,joueur),joueur,opposant,alpha,beta,prof_act,prof_max,pourcentage_amplitude, nb_jetons))
        if (v >= beta) : return v
        alpha = max(alpha,v)
    return v


#!Section Copiée/Collée de Puissance4
'''
fonction clear -> #? pratique car ça nous laisse la possibilité de voir l'historique des coups joués
'''
def clear():
    print("\n" * get_terminal_size().lines, end='')

'''
fonction pour définir la valeur d'action --> évite les erreurs de types ou valeur impossible
#* uniquement destiné à rendre le main plus lisible et épuré
'''
def Selection_colonne(phrase):
    action=-1
    dim_Colonne = 12
    while True:
        try:
            action = int(input(phrase))
            if (action >= 0 and action <= dim_Colonne) : break
        except ValueError:
            print("Erreur : type de l'input")
    return action


#! SECTION MAIN

if __name__ == '__main__': 
    #! PARAMETRISATION
    humain_prof_max = 7
    ia_prof_max = 4
    humain_pourcentage = 0.4
    ia_pourcentage = 0.6

    win_IA = 0
    win_Humain = 0
    nb_jetons = 0

    #Choix symbole
    humain = 'X' #! IA qui COMMENCE
    ia = 'O' #! IA qui joue en DEUXIEME

    #Choix commencement
    first = 'X'

    #Calcul trop long : disqualification
    discalifie = ""
    temps_Max_Calcul = 8
   
    #! Début du code
    print('Début de la nouvelle partie !')

    plateau = Initialisation.Plateau()
    check_partie_fini = False
    while(not check_partie_fini):

        if(first == humain): #Si l'humain joue en premier
            
            montemps=time.time() #Temps de reference pr le chronometre en seconde
            #number of seconds passed since epoch (January 1, 1970, 00:00:00 at UTC = the point where time begins)
            action = Alpha_Beta(plateau, humain, humain_prof_max, humain_pourcentage, nb_jetons)
            nv_Temps = time.time()
            if(nv_Temps - montemps >= temps_Max_Calcul):
                discalifie = humain
                break

            plateau = Fonctions_de_base.Result(plateau,action[1],humain)        
            nb_jetons+=1
            #!Si la partie est finie, l'IA ne joue pas
            check_partie_fini = Fonctions_de_base.Terminal_Test(plateau, nb_jetons)
            if(check_partie_fini) : break

        #! L'IA détermine son play ici
        montemps=time.time()
        action=Alpha_Beta(plateau,ia, ia_prof_max, ia_pourcentage, nb_jetons)
        nv_Temps = time.time()
        if(nv_Temps - montemps >= temps_Max_Calcul):
            discalifie = ia
            break
        
        #action contient la value et l'action associée

        plateau = Fonctions_de_base.Result(plateau,action[1],ia)
        nb_jetons+=1
        #!Si la partie est finie, l'humain ne joue pas
        check_partie_fini = Fonctions_de_base.Terminal_Test(plateau, nb_jetons)
        if(check_partie_fini) : break

        if(first == ia): #Si l'IA joue en premier maintenant c'est le tour de l'Humain
            montemps=time.time()
            action = Alpha_Beta(plateau, humain, humain_prof_max, humain_pourcentage, nb_jetons)
            nv_Temps = time.time()
            if(nv_Temps - montemps >= temps_Max_Calcul):
                discalifie = humain
                break
            
            plateau = Fonctions_de_base.Result(plateau,action[1],humain)
            nb_jetons+=1
            #!Si la partie est finie, l'IA ne joue pas
            check_partie_fini = Fonctions_de_base.Terminal_Test(plateau, nb_jetons)
            if(check_partie_fini) : break

    print(plateau)
    print('La partie est terminée, bien joué à vous deux !')
    print("Le maximum de jetons authorisés pour cette partie était de", Fonctions_de_base.nb_jetons_max)
    winner = Fonctions_de_base.Win_Lose(plateau, ia, humain)
    if(winner == ia or discalifie == humain):            
        win_IA += 1
        print("--IA gagne la partie--")
        if(discalifie == humain):
            discalifie = "*"
            print("DISCALIFICATION de Humain car trop lent (Temps max = %d sec)" %temps_Max_Calcul)
    elif(winner == humain or discalifie == ia):
        win_Humain += 1
        print("--HUMAIN gagne la partie--")
        if(discalifie == ia):
            discalifie = "*"
            print("DISCALIFIACTION de IA car trop lent (Temps max = %d sec)" %temps_Max_Calcul)
    else:
        print("--EGALITE entre IA et Humain à la partie--")
    print("\n")
    
    #La partie est finie ou une IA c'est demarquee
    if(first == humain):
        print("HUMAIN jouait en PREMIER")
    if(first == ia):
        print("IA jouait en PREMIER")
    
    print()
    print("L'IA : HUMAIN de paramètres :",
        "\npoucentage largeur = ", humain_pourcentage,
        "\nprofondeur max = ", humain_prof_max,
        "\nTotal Victoire = ", win_Humain)
    
    print("\nL'IA : IA de paramètres :",
        "\npoucentage largeur = ", ia_pourcentage,
        "\nprofondeur max = ", ia_prof_max,
        "\nTotal Victoire = ", win_IA)
