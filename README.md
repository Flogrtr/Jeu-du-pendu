# Jeu du pendu
 Rendu du jeu du pendu

Pour faire fonctionner le jeu il faut lancer le programme dans le dossier ou se situe le fichier mots_pendu.txt

Fonctionnement du programme : On importe les bibliothèque random et string dont on va avoir besoin dans le programme

Le programme est constitué de deux fonction choisir_mot(liste_mot) qui choisit un mot et le retourne dans la liste de mots contenue dans le fichier mots_pendu.txt qu'il a pris en entrée. et jeu_du_pendu(mot) qui prend en entrée ce mot et demande au joueur de proposer des lettres pour trouver ce mot. Cette fonction verifie si les propositions sont bien des lettres uniques minuscules et si elles ont déjà été proposées (de façon correctes ou incorrectes). Le jeu s'arrête si on a trouvé le mot ou si le joueur a fait 6 erreurs. 
