import AlphaBetaMiniMax
import Fonctions_de_base
import Initialisation
import time
from shutil import get_terminal_size #pour fonction clear
import random #Pour choisir les textes à afficher

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

#Partie du Lore car c'est inutile mais absolument indispensable
'''Lore pour introduire le jeu
'''
def Intro():
    print("Bienvenue à toi Champion !",
    "\nSache que toute entrevue avec Athéna nécessite un Test.",
    "\nProuve nous ton sens de la stratégie et fais honneur à notre Déesse !",
    "\n\nTu devras affronter notre champion !!!"
    "\n\nCelui-là même qui sera créé par ton espèce dans un futur lointain !",
    "\nSi tu l'emportes face à Skynet, Athéna t'écoutera !\n\n")
'''
Reactions utilisées à chaque coups de l'adversaire
'''
def Reaction():
    a = "Voilà un coup intéressant ! \nMais il en faudra plus pour me surprendre !"
    b = "N'oublie pas ! La vitesse est une chose mais la précipitation en est une autre."
    c = "Cela faisait plus d'un siècle que je ne m'étais pas amusé de la sorte !\nContinue de me divertir !"
    d = "Hmmmm\nJe ne distingue plus ton futur ..."
    e = "Le fin joueur ne joue pas la carte qu'attend son adversaire, encore moins celle qu'il désire"
    f = "Connaître exactement le jeu de ses adversaires, c'est leur avoir déjà à moitié gagné la partie."
    return (random.choice([a,b,c,d,e,f]))#Sélection aléatoire d'une citation


if __name__ == '__main__': 
    #! Début du code
    clear()
    #Intro()
    print('Début de la nouvelle partie !')

    #Choix symbole
    while True: #*on répète jusqu'à ce qu'un des deux symbole soit choisi
        humain = input('Choisissez votre symbole (X/O) \n')
        if(humain == 'X') : 
            ia = 'O'
            break
        if(humain == 'O') : 
            ia = 'X'
            break
        clear()

    #Choix commencement
    while True: #*on répète jusqu'à ce qu'un des deux symbole soit choisi
        first = input('Choisir qui commence (X/O) \n')
        if(first == 'X') : break
        if(first == 'O') : break
        clear()

    plateau = Initialisation.Plateau()
    nb_jetons = 0
    check_partie_fini = False
    while(not check_partie_fini):

        if(first == humain): #Si l'humain joue en premier
            print(plateau)
            list_Actions = Fonctions_de_base.Action(plateau) #On recupere toutes les actions possibles
            for i in range(len(list_Actions)):
                list_Actions[i] += 1
            print("Action(s) possible(s) : ", list_Actions)
        #    print("\n" + Reaction())#Pour rendre le jeu plus vivant
            action = ""
            action_Autorise = False #Verification que ce coup est autorise
            while(action_Autorise == False): 
                action = Selection_colonne('\nHumain, indique la colonne dans laquelle tu veux placer ton pion (1-12) \n')
                if(action in list_Actions):
                    action_Autorise = True
            plateau = Fonctions_de_base.Result(plateau, action-1, humain) #action-1 car si on rentre 1 alors c'est l'index 0 de la colonne
            nb_jetons+=1
            #!Si la partie est finie, l'IA ne joue pas
            check_partie_fini = Fonctions_de_base.Terminal_Test(plateau, nb_jetons)
            if(check_partie_fini) : break
            

        #! L'IA détermine son play ici
        print()
        print(plateau)
        list_Actions = Fonctions_de_base.Action(plateau) #On recupere toutes les actions possibles
        for i in range(len(list_Actions)):
                list_Actions[i] += 1
        print("Action(s) possible(s) pour l'IA : ", list_Actions)      

        tps_IA=time.time() #Temps de reference pr le chronometre en seconde
        action=AlphaBetaMiniMax.Alpha_Beta(plateau,ia,nb_jetons)
        nv_Temps = time.time()
        
        #action contient la value et l'action associée
        clear()
        print("L'IA joue : "+ str(action[1] + 1))#On rajoute +1 pr etre dans le referenciel humain (commence a 1, fini a 12)
        print("L'IA joue en %.2f sec" %(nv_Temps - tps_IA))
        print()
        plateau = Fonctions_de_base.Result(plateau,action[1],ia)
        nb_jetons+=1
        #!Si la partie est finie, l'humain ne joue pas
        check_partie_fini = Fonctions_de_base.Terminal_Test(plateau,nb_jetons)
        if(check_partie_fini) : break

        if(first == ia): #Si l'IA joue en premier maintenant c'est le tour de l'Humain
            print(plateau)
            list_Actions = Fonctions_de_base.Action(plateau) #On recupere toutes les actions possibles
            for i in range(len(list_Actions)):
                list_Actions[i] += 1
            print("Action(s) possible(s) : ", list_Actions)
      #      print("\n" + Reaction())#Pour rendre le jeu plus vivant
            action = ""
            action_Autorise = False #Verification que ce coup est autorise
            while(action_Autorise == False): 
                action = Selection_colonne('\nHumain, indique la colonne dans laquelle tu veux placer ton pion (1-12) \n')
                if(action in list_Actions):
                    action_Autorise = True
            clear()
            plateau = Fonctions_de_base.Result(plateau, action-1, humain) #action-1 car si on rentre 1 alors c'est l'index 0 de la colonne
            nb_jetons+=1
            #!Si la partie est finie, l'IA ne joue pas
            check_partie_fini = Fonctions_de_base.Terminal_Test(plateau,nb_jetons)
            if(check_partie_fini) : break

    print(plateau)
    print('La partie est terminée, bien joué à vous deux !\n\n')
    winner = Fonctions_de_base.Win_Lose(plateau, ia, humain)
    if(winner == ia):
        print("Malheureusement c'en est fini de ce petit jeu !!!\nTu n'es pas digne de rencontrer ma Déesse !")
    elif(winner == humain):
        print("CHAMPION ! Tu as mon plus grand respect !!!\nAprès ton entrevue avec Athéna tu prendras ma place !",
            "\n\nMille mercis ! Je peux enfin prendre des vacances !")
    else:
        print("Limite de %d jetons atteinte" %Fonctions_de_base.nb_jetons_max)
        print("Ce combat fut des plus rudes !\nVa brave guerrier ! Nous croiserons de nouveau nos pions !")



