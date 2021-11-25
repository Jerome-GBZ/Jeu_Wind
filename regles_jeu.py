#  /* --Importation des bibliothèques nécessaires */
import pygame
import menu

def open_regles(volume_actif):
    #  /* --Initialisation de la bibliothèque Pygame */
    pygame.init()
    pygame.display.set_caption('Wind Master - CONTROL')

    #  /* --Création de la fenêtre */
    fenetre = pygame.display.set_mode((505, 450))

    #  /* --set background color blue */
    color = (119, 180, 254)

    #  /* --Variable déterminante du lancement de la boucle principale */
    menu_lance = True

    #  /* -- Titre principal  */
    font = pygame.font.Font(None, 35)
    text = font.render("Les règles du jeu ", 1, (15, 15, 35))

    #  /* -- Gestion des images : */

    # touches directionnelles du clavier :
    touche_direct = pygame.image.load('img/menu/control.png').convert_alpha()
    touche_direct = pygame.transform.scale(touche_direct, (55, 55))  # taille de l'image (niveau d'étirement)

    # boules de feu :
    boule_feu = pygame.image.load('img/control/fireball.png').convert_alpha()
    boule_feu = pygame.transform.scale(boule_feu, (50, 55))

    # pouvoir du vent :
    pouvoir_vent = pygame.image.load('img/control/vent.png').convert_alpha()
    pouvoir_vent = pygame.transform.scale(pouvoir_vent, (50, 50))

    # jauge d'énergie :
    jauge_energie = pygame.image.load('img/control/jauge_complete.png').convert_alpha()
    jauge_energie = pygame.transform.scale(jauge_energie, (70, 18))

    # coeur de vie:
    coeur_vie = pygame.image.load('img/control/Coeur3.png').convert_alpha()
    coeur_vie = pygame.transform.scale(coeur_vie, (70, 20))

    # fiole d'énergie:
    fiole = pygame.image.load('img/control/fiole.png').convert_alpha()
    fiole = pygame.transform.scale(fiole, (40, 40))

    #  /* -- Gestion des textes explicatifs : */

    # touches directionnelles du clavier :
    font = pygame.font.Font(None, 20)
    couleur_texte = (15, 15, 35)
    fenetre.fill(color)

    explTouches1 = font.render("Déplacez le personnage avec les touches directionnelles.", 1, couleur_texte)
    explTouches2 = font.render("Utilisez la barre espace pour lancer votre pouvoir du vent.", 1, couleur_texte)

    # les boules de feu :

    explBoules1 = font.render("Différentes boules de feu apparaissent régulièrement à l'écran.", 1, couleur_texte)
    explBoules2 = font.render("Vous devez les éviter sinon, vous perdrez un point de vie !", 1, couleur_texte)
    explBoules3 = font.render("Plus la difficulté est élevée, plus les boules arriveront vite !", 1, couleur_texte)

    # le pouvoir du vent:

    explVent1 = font.render("Le pouvoir du vent permet de vous protéger des boules de feu.", 1, couleur_texte)
    explVent2 = font.render("Plus la barre d'énergie augmente, plus le pouvoir dure.", 1, couleur_texte)

    # jauge d'énergie:

    explJauge1 = font.render("La jauge d'énergie recharge votre pouvoir du vent.", 1, couleur_texte)
    explJauge2 = font.render("Si la jauge est au max, vous générerez un grand mur de vent.", 1, couleur_texte)

    # coeur de vie:

    explVie1 = font.render("Surveillez vos points de vie !", 1, couleur_texte)
    explVie2 = font.render("Vous perdez un coeur si vous êtes touché par une boule !", 1, couleur_texte)

    # fiole d'énergie:

    explFiole = font.render("Récupérez les fioles pour recharger votre barre d'énergie !", 1, couleur_texte)

    #  --Les boutons / images
    btn_retour = pygame.image.load("img/menu/retour-min.png").convert_alpha()
    btn_retour = pygame.transform.scale(btn_retour, (70, 50))
    fenetre.blit(btn_retour, (215, 395))



    # titre principal :
    fenetre.blit(text, (160, 10))  # x = 160 et y = 20

    # les contrôles au clavier :
    fenetre.blit(touche_direct, (15, 40))

    fenetre.blit(explTouches1, (100, 50))
    fenetre.blit(explTouches2, (100, 70))

    # les boules de feu:
    fenetre.blit(boule_feu, (15, 115))

    fenetre.blit(explBoules1, (100, 115))
    fenetre.blit(explBoules2, (100, 135))
    fenetre.blit(explBoules3, (100, 155))

    # le pouvoir du vent:
    fenetre.blit(pouvoir_vent, (15, 180))

    fenetre.blit(explVent1, (100, 190))
    fenetre.blit(explVent2, (100, 210))

    # jauge d'énergie :
    fenetre.blit(jauge_energie, (15, 250))

    fenetre.blit(explJauge1, (100, 248))
    fenetre.blit(explJauge2, (100, 268))

    # coeur de vie :
    fenetre.blit(coeur_vie, (15, 300))

    fenetre.blit(explVie1, (100, 300))
    fenetre.blit(explVie2, (100, 315))

    # fiole d'énergie :
    fenetre.blit(fiole, (25, 330))

    fenetre.blit(explFiole, (100, 345))

    #  --Boucle principale */
    while menu_lance:
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                menu_lance = False  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x,y = event.pos
                if (x > 215 and y > 395) and (x < 280 and y < 445):
                    menu_lance = False
        # fin du programme */
        pygame.display.update()
