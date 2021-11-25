#  --Importation des bibliothèques nécessaires
import pygame
import menu

#  --Initialisation de la bibliothèque Pygame
pygame.init()

#  --Création de la fenêtre
fenetre = pygame.display.set_mode((500, 720))
pygame.display.set_caption('Wind Master - CREDIT')

def contain():
# /* Image accompagnement */
    img1 = pygame.image.load("img/jaquette_WIND_MASTER.png").convert_alpha()
    img1 = pygame.transform.scale(img1, (200,200))
    fenetre.blit(img1, (240, 180))

# /*  Les membres de l'équipe :   */
    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 25)
    fontlink = pygame.font.Font(None, 18)
    color_txt = (15, 15, 35)
    text = font.render("Les crédits", 1, color_txt)
    text0 = font1.render("Game Designer : ", 1, color_txt)
    text1 = font1.render(" > Quentin C", 1, color_txt)
    text2 = font1.render("Développeurs Python: ", 1, color_txt)
    text3 = font1.render(" > Jerome G", 1, color_txt)
    text4 = font1.render(" > Loris M", 1, color_txt)
    text5 = font1.render(" > Rémy D", 1, color_txt)
    text6 = font1.render(" > Romain P", 1, color_txt)
    text7 = font1.render("BeatMaker : ", 1, color_txt)
    text8 = text4
    text9 = font1.render("Graphistes :", 1, color_txt)
    text10 = text3
    text11 = text6

# /*  Les ressources externes :   */

    text_ressources = font1.render("Ressources externes: ", 1, color_txt)
    text_images = font1.render("->Les images: ", 1, color_txt)
    text_imagePerso = font1.render(" > Image du personnage : https://cutt.ly/JrAvvnx", 1, color_txt)
    text_imageNuage = font1.render(" > Image du nuage : https://cutt.ly/7rAvCz2 ", 1, color_txt)
    text_imageVent  = font1.render(" > Image du vent : https://cutt.ly/LrAv5oL ", 1, color_txt)
    text_imageFireB = font1.render(" > Image de la boule de feu : https://cutt.ly/YrAby1L ", 1, color_txt)
    text_imageFiole = font1.render(" > Image de la fiole : https://cutt.ly/3rAbzA6 ", 1, color_txt)
    text_ApprendrePy = font1.render("->Les tutoriels sur Python :", 1, color_txt)

    text_ApprendrePylink = fontlink.render("https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python", 1, color_txt)
    text_ApprendrePylink2 = fontlink.render("https://cutt.ly/7rAnw0s", 1, color_txt)

#  --Les boutons / images
    btn_retour = pygame.image.load("img/menu/retour-min.png").convert_alpha()
    btn_retour = pygame.transform.scale(btn_retour, (70, 50))
    fenetre.blit(btn_retour, (215, 595))

# /*  L'affichage des textes  :   */
    pos_text_x = 30

    # les membres :
    fenetre.blit(text, (160, 30))
    fenetre.blit(text0, (pos_text_x, 80))
    fenetre.blit(text1, (pos_text_x+20, 100))
    fenetre.blit(text2, (pos_text_x, 140))
    fenetre.blit(text3, (pos_text_x+20, 160))
    fenetre.blit(text4, (pos_text_x+20, 180))
    fenetre.blit(text5, (pos_text_x+20, 200))
    fenetre.blit(text6, (pos_text_x+20, 220))
    fenetre.blit(text7, (pos_text_x, 260))
    fenetre.blit(text8, (pos_text_x+20, 280))
    fenetre.blit(text9, (pos_text_x, 320))
    fenetre.blit(text10, (pos_text_x+20, 340))
    fenetre.blit(text11, (pos_text_x+20, 360))

    # les ressources externes :
    fenetre.blit(text_ressources, (pos_text_x, 390))
    fenetre.blit(text_images, (pos_text_x, 410))
    fenetre.blit(text_imagePerso, (pos_text_x+20, 430))
    fenetre.blit(text_imageNuage, (pos_text_x+20, 450))
    fenetre.blit(text_imageVent, (pos_text_x+20, 470))
    fenetre.blit(text_imageFireB, (pos_text_x+20, 490))
    fenetre.blit(text_imageFiole, (pos_text_x+20, 510))
    fenetre.blit(text_ApprendrePy, (pos_text_x, 535))

    fenetre.blit(text_ApprendrePylink, (pos_text_x-20, 560))
    fenetre.blit(text_ApprendrePylink2, (pos_text_x-20, 580))


def open_Credit(volume_actif):
    fenetre = pygame.display.set_mode((500, 650))
    #  --set background color blue
    color = (119, 180, 254)
    #  --Variable qui continue la boucle si = 1, stoppe si = 0
    credit_encour = True

    fenetre.fill(color)
    contain()
    pygame.display.update()

    while (credit_encour):
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                credit_encour = False  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                #  --Sur image retour
                if (x > 210 and y > 600) and (x < 286 and y < 650):
                    #menu.start_menu(volume_actif)
                    credit_encour = False