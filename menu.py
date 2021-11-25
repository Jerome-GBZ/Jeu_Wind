#  --Importation des bibliothèques nécessaires
import pygame
import credit
import regles_jeu
import skin
import fichier
import jeu


def start_menu(vol):
    #  --set background color blue
    color = (119, 180, 254)

    #  --Initialisation de la bibliothèque Pygame
    pygame.init()
    pygame.display.set_caption('Wind Master')

    #  --Création de la fenêtre
    fenetre = pygame.display.set_mode((500, 380))


    # variable de choix de skin
    skin_selec = 'superman_bleu'

    #  --Variable qui continue la boucle si = 1, stoppe si = 0
    menu_encour = True

    son = pygame.mixer.Sound("music/menu.wav")

    #  --Nom du jeu
    font = pygame.font.Font(None, 50)
    text = font.render("Wind Master", 1, (15, 15, 35))

    #  --Les boutons / images
    btn_play = pygame.image.load("img/menu/play.png").convert_alpha()
    btn_play = pygame.transform.scale(btn_play, (195, 160))

    btn_credit = pygame.image.load("img/menu/credit.png").convert_alpha()
    btn_credit = pygame.transform.scale(btn_credit, (100, 30))

    btn_control = pygame.image.load("img/menu/control_final.png").convert_alpha()
    btn_control = pygame.transform.scale(btn_control, (100, 30))

    btn_skin = pygame.image.load("img/menu/skin.png").convert_alpha()
    btn_skin = pygame.transform.scale(btn_skin, (100, 30))

    btn_score = pygame.image.load("img/menu/score.png").convert_alpha()
    btn_score = pygame.transform.scale(btn_score, (60, 35))

    #   -- VOLULME
    # volume_actif = True
    volume_actif = vol

    btn_volume = pygame.image.load("img/menu/volume.png").convert_alpha()
    btn_volume = pygame.transform.scale(btn_volume, (26, 25))

    btn_no_volume = pygame.image.load("img/menu/no_volume.png").convert_alpha()
    btn_no_volume = pygame.transform.scale(btn_no_volume, (26, 25))

    btn_volume_actu = btn_volume

    #  --les nuages :
    nuage = pygame.image.load('img/menu/nuage.png').convert_alpha()
    nuage = pygame.transform.scale(nuage, (50, 33))
    nuage1 = pygame.transform.scale(nuage, (100, 76))
    nuage2 = nuage
    nuage3 = nuage
    nuage4 = nuage

    #  -- coordonées des nuages :
    nx = 50
    ny = 50

    n1x = 285
    n1y = 200

    n2x = 100
    n2y = 100

    n3x = 180

    n4x = 0
    n4y = 310

    #  --Création de la fenêtre
    fenetre = pygame.display.set_mode((500, 380))

    #  --Affichage d'une image :
    def spone(x, y, image):
        fenetre.blit(image, (x, y))

    #  --Boucle infinie
    while (menu_encour):
        fenetre = pygame.display.set_mode((500, 380))
        if volume_actif == True :
            son.play()

        fenetre.fill(color)

        spone(nx, ny, nuage)
        spone(n1x, n1y, nuage1)
        spone(n2x, n2y, nuage2)
        spone(n3x, n3x, nuage3)
        spone(n4x, n4y, nuage4)

        spone(152, 110, btn_play)
        spone(200, 348, btn_skin)
        spone(2, 348, btn_credit)
        spone(398, 348, btn_control)
        spone(435, 5, btn_score)

        spone(150, 30, text)

        fenetre.blit(btn_volume_actu, (5, 5))

        # --- Contraintes de déplacement des nuages --- :
        # --- NUAGE 1
        if nx > 535:
            nx = -35
        else:
            nx += 0.01
        # --- NUAGE 2
        if n2x > 535 :
            n2x = -35
        else :
            n2x += 0.025
        # --- NUAGE 3
        if n3x < -35 :
            n3x = 535
        else :
            n3x -= 0.022
        # --- NUAGE 4
        # pas d'animation
        # --- NUAGE 5
        if n4x < -35:
            n4x = 535
        else:
            n4x -= 0.02

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                son.stop()
                menu_encour = False  # On arrête la boucle

            #  --Detecter click souris
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                #  --Sur image play
                if (x > 165 and y > 125) and (x < 330 and y < 240) :
                    son.stop()
                    jeu.vrai_start(skin_selec, volume_actif)
                    #menu_encour = False

                #  --Sur image credit
                if (x > 0 and y > 350) and (x < 100 and y < 380) :
                    credit.open_Credit(volume_actif)
                    #menu_encour = False

                #  --Sur image Control
                if (x > 400 and y > 350) and (x < 500 and y < 380):
                    regles_jeu.open_regles(volume_actif)
                    # menu_encour = False

                #  --Sur image Skin
                if (x > 202 and y > 350) and (x < 300 and y < 380):
                    skin_selec = skin.open_Skin(volume_actif)

                #  --Sur image Score
                if (x > 435 and y > 4) and (x < 495 and y < 40):
                    fichier.start_fichier(0, volume_actif, skin_selec)
                    # menu_encour = False

                if (x > 0 and y > 0) and (x < 30 and y < 30) :
                    if (volume_actif == True):
                        volume_actif = False
                        btn_volume_actu = btn_no_volume
                        son.stop()
                    elif (volume_actif == False):
                        volume_actif = True
                        btn_volume_actu = btn_volume
                        son.stop()
                        son.play()
        pygame.display.update()
