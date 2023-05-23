import random
import string
liste_mot = "mots_pendu.txt" # On utilise le fichier donné en exemple pour faire fonctionner le jeu
def choisir_mot(liste_mot):
    # Ouvre le fichier en mode lecture
    with open(liste_mot, 'r') as f:
        mots = f.readlines() #On fait une liste des mots
    return random.choice(mots).strip() # On choisi de façon random un mots de la liste à deviner
mot_choisi = choisir_mot(liste_mot) # On chosit le mot pour le jeu
def jeu_du_pendu(mot):
    lettres_trouvees = []  # Liste pour stocker les lettres trouvées par le joueur
    lettres_proposees_fausses=[] #Liste pour stocker les lettres proposées mais fausses par le joueur
    nombre_de_vie = 6  # Nombre de vies restantes
    print("Ceci est le jeu du pendu, il faut trouver un mot en moins de 6 essais")
    while nombre_de_vie > 0:
        mot_a_deviner = ''.join([lettre if lettre in lettres_trouvees else '_' for lettre in mot]) # On affiche le mot à deviner avec les lettres trouvées et des underscores pour les lettres non trouvées
        print("Mot à deviner :", mot_a_deviner)

        if mot_a_deviner == mot: # Si le mot est entièrement deviné, affiche un message de victoire et termine la fonction
            print("Vous avez trouvé le mot en :", mot)
            return

        lettre = input("Entrez une lettre : ")
        if len(lettre)!=1:# Si on donne plus d'une lettre, on affiche une erreur
            print("Il faut donner une seule lettre à la fois")
            continue
        if lettre not in string.ascii_lowercase:# Si on donne autre chose qu'une lettre minuscule, on affiche une erreur
            print("Il faut donner une lettre en minuscule")
            continue

        if lettre in lettres_trouvees:
            # Si la lettre a déjà été trouvée,
            print("Vous avez déjà trouvé cette lettre.")
        if lettre in mot: # Si la lettre est dans le mot à deviner, l'ajoute à la liste des lettres trouvées
            lettres_trouvees.append(lettre)
        elif lettre in lettres_proposees_fausses : # Si la lettre a déjà été proposée,
            print("Vous avez déjà proposé cette lettre qui n'est pas dans le mot. Proposezs une autre lettre")
        else: # Sinon, réduit le nombre de vie restantes et ajoute la lettre à la liste des lettres proposées
            nombre_de_vie =nombre_de_vie-1
            lettres_proposees_fausses.append(lettre)
            print("Lettre incorrecte ! Vous avez", nombre_de_vie, "vies restantes.")

    print("Il vous reste 0 vies. Vous avez perdu. Le mot était :", mot) #Si il y a 0 vies, on perds et affiche le mot





jeu_du_pendu(mot_choisi)
