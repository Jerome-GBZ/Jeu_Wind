#  --Importation des bibliothèques nécessaires
import pygame
import menu

def open_Skin(volume_actif):
    #  --Initialisation de la bibliothèque Pygame
    pygame.init()

    #  --Création de la fenêtre
    fenetre = pygame.display.set_mode((500, 380))
    pygame.display.set_caption('Wind Master - SKIN')

    #  --set background color blue
    color = (119, 180, 254)
    #  --Variable qui continue la boucle si = 1, stoppe si = 0
    credit_encour = True
    fenetre.fill(color)

    #  --Nom de la fenetre
    font = pygame.font.Font(None, 50)
    text = font.render("Choisis ton skin", 1, (15, 15, 35))

    #  --Les boutons / images
    size_skin = (80,100)
    btn_skin_1 = pygame.image.load("img/personnage/superman_bleu.png").convert_alpha()
    btn_skin_1 = pygame.transform.scale(btn_skin_1, size_skin)

    btn_skin_2 = pygame.image.load("img/personnage/superman_magenta.png").convert_alpha()
    btn_skin_2 = pygame.transform.scale(btn_skin_2, size_skin)

    btn_skin_3 = pygame.image.load("img/personnage/superman_jaune.png").convert_alpha()
    btn_skin_3 = pygame.transform.scale(btn_skin_3, size_skin)

    btn_skin_4 = pygame.image.load("img/personnage/superman_noir.png").convert_alpha()
    btn_skin_4 = pygame.transform.scale(btn_skin_4, size_skin)

    btn_skin_5 = pygame.image.load("img/personnage/superman_rose.png").convert_alpha()
    btn_skin_5 = pygame.transform.scale(btn_skin_5, size_skin)

    btn_skin_6 = pygame.image.load("img/personnage/superman_vert.png").convert_alpha()
    btn_skin_6 = pygame.transform.scale(btn_skin_6, size_skin)

    btn_skin_7 = pygame.image.load("img/personnage/superman_arc_en_ciel.png").convert_alpha()
    btn_skin_7 = pygame.transform.scale(btn_skin_7, size_skin)

    btn_skin_8 = pygame.image.load("img/personnage/superman_blanc.png").convert_alpha()
    btn_skin_8 = pygame.transform.scale(btn_skin_8, size_skin)

    #  --Les boutons / images
    btn_retour = pygame.image.load("img/menu/retour-min.png").convert_alpha()
    btn_retour = pygame.transform.scale(btn_retour, (70, 50))

    skin_selec = 'superman_bleu'

    #   -- Dessiner rectangle
    color_rect_jaune = (255, 215, 0)
    def draw_rect(valeur_rect_x, valeur_rect_y):
        width = 4
        fenetre.fill(color)
        pygame.draw.rect(fenetre, color_rect_jaune, [valeur_rect_x, valeur_rect_y, 85, 85], width) 

    while (credit_encour):
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                credit_encour = False  # On arrête la boucle

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                #  --Sur image default
                if (x > 50 and y > 110) and (x < 135 and y < 185):
                    draw_rect(55, 108)
                    skin_selec = 'superman_bleu'
                #  --Sur image magenta
                if (x > 150 and y > 110) and (x < 235 and y < 185):
                    draw_rect(155, 108)
                    skin_selec = 'superman_magenta'
                #  --Sur image jaune
                if (x > 250 and y > 110) and (x < 335 and y < 185):
                    draw_rect(255, 108)
                    skin_selec = ('superman_jaune')
                #  --Sur image noir
                if (x > 350 and y > 110) and (x < 435 and y < 185):
                    draw_rect(355, 108)
                    skin_selec = ('superman_noir')
                #  --Sur image rose
                if (x > 50 and y > 235) and (x < 135 and y < 305):
                    draw_rect(55, 228)
                    skin_selec = ('superman_rose')
                #  --Sur image vert
                if (x > 150 and y > 235) and (x < 235 and y < 305):
                    draw_rect(155, 228)
                    skin_selec = ('superman_vert')
                #  --Sur image arc en ciel
                if (x > 250 and y > 235) and (x < 335 and y < 305):
                    draw_rect(255, 228)
                    skin_selec = ('superman_arc_en_ciel')
                #  --Sur image arc en blanc
                if (x > 350 and y > 230) and (x < 440 and y < 305):
                    draw_rect(355, 228)
                    skin_selec = ('superman_blanc')

                if (x > 215 and y > 320) and (x < 285 and y < 370):
                    return skin_selec
                    credit_encour = False
                    menu.start_menu(volume_actif)

        fenetre.blit(btn_retour, (215, 325))

        fenetre.blit(text, (120, 30))

        fenetre.blit(btn_skin_1, (60, 100))
        fenetre.blit(btn_skin_2, (160, 100))
        fenetre.blit(btn_skin_3, (260, 100))
        fenetre.blit(btn_skin_4, (360, 100))
        fenetre.blit(btn_skin_5, (60, 220))
        fenetre.blit(btn_skin_6, (160, 220))
        fenetre.blit(btn_skin_7, (260, 220))
        fenetre.blit(btn_skin_8, (360, 220))

        pygame.display.update()
