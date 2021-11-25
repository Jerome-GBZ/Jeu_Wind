import pygame
import menu
import jeu

def start_fichier(chrono, volume_actif, skin_selec):
    # --- Parametrage de la fenêtre --- :
    pygame.init()

    son_menu = pygame.mixer.Sound("music/menu.wav")

    blue = (119, 181, 254)
    blue_marine = (15,15,35)
    jaune = (255, 215, 0)
    surfaceW = 500
    surfaceH = 380

    surface = pygame.display.set_mode((surfaceW, surfaceH))
    pygame.display.set_caption("Wind Master - SCORE")

    #   -- IMAGE BOUTON
    btn_play = pygame.image.load("img/menu/play_f.png").convert_alpha()
    btn_play = pygame.transform.scale(btn_play, (150, 45))

    btn_menu = pygame.image.load("img/menu/menu_f.png").convert_alpha()
    btn_menu = pygame.transform.scale(btn_menu, (150, 45))

    #   -- IMAGE COUPE WIN
    coupe_1 = pygame.image.load("img/coupe/number_1.png").convert_alpha()
    coupe_1 = pygame.transform.scale(coupe_1, (50, 50))

    coupe_2 = pygame.image.load("img/coupe/number_2.png").convert_alpha()
    coupe_2 = pygame.transform.scale(coupe_2, (50, 50))

    coupe_3 = pygame.image.load("img/coupe/number_3.png").convert_alpha()
    coupe_3 = pygame.transform.scale(coupe_3, (50, 50))

    #  --Les boutons / images
    btn_retour = pygame.image.load("img/menu/retour-min.png").convert_alpha()
    btn_retour = pygame.transform.scale(btn_retour, (70, 50))


    #  --Affichage d'une image :
    def spone(x, y, image):
        surface.blit(image, (x, y))


    # --le fichier score :
    deja_rentre = False

    fichier_score = open("scores", "r")
    font_titre = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 30)

    nom_1 = fichier_score.readline()
    nom_1 = nom_1[0:12]
    nom_1 = nom_1.rstrip()
    score_1 = fichier_score.readline()
    score_1 = score_1.rstrip()

    nom_2 = fichier_score.readline()
    nom_2 = nom_2[0:12]
    nom_2 = nom_2.rstrip()
    score_2 = fichier_score.readline()
    score_2 = score_2.rstrip()

    nom_3 = fichier_score.readline()
    nom_3 = nom_3[0:12]
    nom_3 = nom_3.rstrip()
    score_3 = fichier_score.readline()
    score_3 = score_3.rstrip()

    nom1 = font.render(nom_1, 1, blue_marine)
    nom2 = font.render(nom_2, 1, blue_marine)
    nom3 = font.render(nom_3, 1, blue_marine)

    score1 = font.render(score_1, 1, blue_marine)
    score2 = font.render(score_2, 1, blue_marine)
    score3 = font.render(score_3, 1, blue_marine)

    score_affiche = font.render(str(chrono), 1, jaune)


    phrase1 = font_titre.render("Meilleurs Joueurs",1, blue_marine)
    phrase_loose = font.render("Essaye encore !",1, blue_marine)
    phrase_chrono = font.render("Tu as fait un score de ",1, blue_marine)
    fichier_score.close()

    phrase2 = font.render("Entre ton nom : ",1, blue_marine)

    color_inactive = (255, 255, 255)
    color_active = jaune
    color = color_inactive

    champ_saisie = pygame.Rect(240, 276, 140, 32)
    active = False
    text = ''
    nom_victoire = " "
    nom_rentre = False
    done = False

    while not done:
        nouveau_fichier_score = open("scores", "r")
        nom_1 = nouveau_fichier_score.readline()
        nom_1 = nom_1[0:12]
        nom_1 = nom_1.rstrip()
        score_1 = nouveau_fichier_score.readline()
        score_1 = score_1.rstrip()

        nom_2 = nouveau_fichier_score.readline()
        nom_2 = nom_2[0:12]
        nom_2 = nom_2.rstrip()
        score_2 = nouveau_fichier_score.readline()
        score_2 = score_2.rstrip()

        nom_3 = nouveau_fichier_score.readline()
        nom_3 = nom_3[0:12]
        nom_3 = nom_3.rstrip()
        score_3 = nouveau_fichier_score.readline()
        score_3 = score_3.rstrip()

        nom1 = font.render(nom_1, 1, blue_marine)
        nom2 = font.render(nom_2, 1, blue_marine)
        nom3 = font.render(nom_3, 1, blue_marine)

        score1 = font.render(score_1, 1, blue_marine)
        score2 = font.render(score_2, 1, blue_marine)
        score3 = font.render(score_3, 1, blue_marine)
        nouveau_fichier_score.close()
        
        if volume_actif == True :
            son_menu.play()
        else :
            son_menu.stop()

        surface.fill(blue)
        if chrono > 0:
            spone(310, 328, btn_play)
            spone(40, 328, btn_menu)

        spone(120, 70, coupe_1)
        spone(120, 120, coupe_2)
        spone(120, 170, coupe_3)

        if chrono < 1 :
            spone(215, 328, btn_retour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                son_menu.stop()
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
               if champ_saisie.collidepoint(event.pos):
                   active = not active
               else:
                   active = False
            color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if not deja_rentre:
                            nom_victoire = text
                            nom_rentre = True
                            text = ''
                            deja_rentre = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            #  --Detecter click souris
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                #  --Sur image Menu
                if (x > 30 and y > 325) and (x < 190 and y < 370):
                    son_menu.stop()
                    done = True
                    #menu.start_menu(volume_actif)

                #  --Sur image Play
                if (x > 300 and y > 325) and (x < 460 and y < 370):
                    son_menu.stop()
                    done = True
                    jeu.vrai_start(skin_selec, volume_actif)

                if (x > 215 and y > 328) and (x < 280 and y < 380):
                    son_menu.stop()
                    done = True
                    #menu.start_menu(volume_actif)

        surface.blit(phrase1,(100,25)) # titre

        #   -- HIGH SCORE TOP
        surface.blit(nom1, (165, 90))
        surface.blit(score1, (315, 90))

        surface.blit(nom2, (165, 140))
        surface.blit(score2, (315, 140))

        surface.blit(nom3, (165, 190))
        surface.blit(score3, (315, 190))

        #   -- SCORE ACTUELLE / COURRANT
        if chrono > 0:
            surface.blit(phrase_chrono, (115, 246))
            surface.blit(score_affiche, (330, 246))

        if chrono>int(score_3):
            surface.blit(phrase2, (60, 282))  # texte
            saisie = font.render(text, True, color)
            width = max(200, saisie.get_width() + 10)
            champ_saisie.w = width
            surface.blit(saisie, (champ_saisie.x+5, champ_saisie.y+5))
            pygame.draw.rect(surface,color,champ_saisie,2)

            if nom_rentre:
                nouveau_fichier = open("scores", "w")
                if chrono>=int(score_1):
                    nouveau_fichier.write(nom_victoire)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(str(chrono))
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_2)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_2)

                elif chrono>=int(score_2) and chrono<int(score_1):
                    nouveau_fichier.write(nom_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_victoire)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(str(chrono))
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_2)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_2)

                elif chrono>int(score_3) and chrono<int(score_2):
                    nouveau_fichier.write(nom_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_1)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_2)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(score_2)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(nom_victoire)
                    nouveau_fichier.write("\n")
                    nouveau_fichier.write(str(chrono))

                nouveau_fichier.close()
                nom_rentre = False

        else:
            if chrono > 0:
                surface.blit(phrase_loose,(160,282))

        pygame.display.update()
