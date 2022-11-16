# On importe la fonction randInt de la library random
from random import randint
# On definit une fonction choixOrdi
def choixOrdi():
    # On genere un int entre 0 et 2 compris
    randomChoix = randint(0,2)
    # Si randomChoix est egal a 0
    if randomChoix == 0:
        # Alors on definit randomChoix en "pierre"
        randomChoix = "pierre"
    # Si randomChoix est egal a 1
    elif randomChoix == 1:
        # Alors on definit randomChoix en "feuille"
        randomChoix = "feuille"
    # Si randomChoix est egal a 2
    elif randomChoix == 2:
        # Alors on definit randomChoix en "ciseaux"
        randomChoix = "ciseaux"
    return randomChoix

# On definit playRPS qui prend comme argument le nombre de rounds
def playRPS(nombreRounds):
    # On setup roundLost et roundWon a 0
    roundLost = 0
    roundWon = 0
    # Tant que roundLost et roundWon ne sont pas egaux aux nombre de rounds definit plus tot 
    while roundLost != nombreRounds and roundWon != nombreRounds:
        # Attribuer choixOrdi() a randomChoix
        randomChoix = choixOrdi()
        # Demander un input au joueur
        choixJoueur = input("pierre, feuille, ou ciseaux? (caps sensitive)")
        # Tant que l'input est incorrect (input n'est n'y pierre, n'y feuille et n'y ciseaux)
        while choixJoueur not in ["pierre", "feuille", "ciseaux"]:
            # Redemander un input
            choixJoueur = input("Mon frerot fait un effort, pierre, feuille ou ciseaux")
        
        # On fait toute les conditions de defaites de round
        if (choixJoueur == "pierre" and randomChoix == "feuille") or (choixJoueur == "ciseaux" and randomChoix == "pierre") or (choixJoueur == "feuille" and randomChoix == "ciseaux"):
            print("RIP BOZO T'AS PERDU EZ NOOB, REESSAYE")
            roundLost = roundLost + 1
        # On fait toute les conditions de victoire de round
        if (choixJoueur == "ciseaux" and randomChoix == "feuille") or (choixJoueur == "pierre" and randomChoix == "ciseaux") or (choixJoueur == "feuille" and randomChoix == "pierre"):
            print("WAAA TA GANGER!!! ENCORE UN ROUND!!")
            roundWon = roundWon + 1
        # On fait la condition d'egalite
        if choixJoueur == randomChoix:
            print("Egalité, rejoue")
        # On fait la condition de defaite de match
        if nombreRounds == roundLost:
            print("T'as perdu RIP BOZO EZ, mais tu as quand meme gagné", roundWon, "rounds!")
        # On fait la condition de victoire de match
        if nombreRounds == roundWon:
            print("GG! Tu as perdu", roundLost, "rounds, mais tu t'en sort giga bien")    

playRPS(5)