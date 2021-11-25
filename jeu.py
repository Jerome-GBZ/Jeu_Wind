import pygame
from random import shuffle, random, randint
import time
import fichier

chrono_generale_final = 1

def start(urls_perso, volume_actif):
    pygame.init()

    #   -- gestion des sons
    son_basique = pygame.mixer.Sound("music/basique.wav")

    son_moyen = pygame.mixer.Sound("music/moyen.wav")

    son_rapide = pygame.mixer.Sound("music/rapide.wav")

    son_vent = pygame.mixer.Sound("music/vent.wav")

    son_aoutch = pygame.mixer.Sound("music/aoutch.wav")

    son_courant = son_basique


    # --- Parametrage de la fenêtre --- :
    blue = (119, 181, 254)
    surfaceW = 1024
    surfaceH = 768

    fenetre = pygame.display.set_mode((surfaceW,surfaceH))
    pygame.display.set_caption("WindMaster")



    p = pygame.image.load("img/control/fireball.png").convert_alpha()

    #________________________________________________________________________________________________________#



    #  --les nuages :

    nuage = pygame.image.load('img/menu/nuage.png').convert_alpha()
    nuage = pygame.transform.scale(nuage,(150,100))

    nuage1 = pygame.transform.scale(nuage,(180,120))

    nuage2 = pygame.transform.scale(nuage,(600,400))

    #  --la jauge :

    jauge = pygame.image.load('img/control/jauge.png').convert_alpha()
    jauge = pygame.transform.scale(jauge,(150,50))
    contour_jauge = pygame.image.load('img/control/jauge_contour.png').convert_alpha()
    contour_jauge = pygame.transform.scale(contour_jauge,(300,20))

    #  --la fiole :

    redBull = pygame.image.load('img/control/fiole.png').convert_alpha()
    redBull = pygame.transform.scale(redBull,(45,45))

    #  --la vie :

    vie = pygame.image.load('img/control/vie.png').convert_alpha()
    vie = pygame.transform.scale(vie,(45,45))

    #  --le vent :

    vent = pygame.image.load('img/control/vent.png').convert_alpha()
    vent = pygame.transform.scale(vent,(100,110))

    # --- Les fonctions --- :

    #  --Affichage d'une image :
    def spone(x,y,image):
        fenetre.blit(image,(x,y))

    #  -- Affichage de la jauge :
    def jaugePouvoir(jauge,jauge_x,jauge_y,jauge_width):
        jauge = pygame.transform.scale(jauge, (int(jauge_width), 50))
        spone(jauge_x, jauge_y, jauge)

    #  -- Affichage des fioles :
    def fiole(redBull,fiole_x,fiole_y):
        spone(fiole_x, fiole_y, redBull)


    def actuvie(nb_vie):
        #  -- coordonées des vies :
        vie1_x = 45
        vie2_x = 95
        vie3_x = 145
        vie_y = 660

        if (nb_vie == 3):
            spone(vie1_x, vie_y, vie)
            spone(vie2_x, vie_y, vie)
            spone(vie3_x, vie_y, vie)
        elif(nb_vie == 2):
            spone(vie1_x, vie_y, vie)
            spone(vie2_x, vie_y, vie)
            spone(-100, vie_y, vie)
        elif(nb_vie == 1):
            spone(vie1_x, vie_y, vie)
            spone(-100, vie_y, vie)
            spone(-100, vie_y, vie)
        elif(nb_vie <= 0):
            spone(-100, vie_y, vie)
            spone(-100, vie_y, vie)
            spone(-100, vie_y, vie)

    perso_normal = pygame.image.load('img/personnage/' + urls_perso + '.png').convert_alpha()
    perso_normal = pygame.transform.scale(perso_normal, (75, 100))
    perso = perso_normal

    persomalade = pygame.image.load('img/personnage/superman_malade.png').convert_alpha()
    persomalade = pygame.transform.scale(persomalade, (75, 100))
    type_skin_perso = False

    # --- Initialisation des caothique --- :

    p1 = pygame.transform.scale(p, (70, 105))
    projectile1_y = -200
    fenetre.blit(p1, (0, projectile1_y))

    p2 = pygame.transform.scale(p, (70, 105))
    projectile2_y = -200
    fenetre.blit(p2, (100, projectile2_y))

    p3 = pygame.transform.scale(p, (70, 105))
    projectile3_y = -200
    fenetre.blit(p3, (200, projectile3_y))

    p4 = pygame.transform.scale(p, (70, 105))
    projectile4_y = -200
    fenetre.blit(p4, (300, projectile4_y))

    p5 = pygame.transform.scale(p, (70, 105))
    projectile5_y = -200
    fenetre.blit(p5, (300, projectile5_y))

    p6 = pygame.transform.scale(p, (70, 105))
    projectile6_y = -200
    fenetre.blit(p6, (300, projectile6_y))

    p7 = pygame.transform.scale(p, (70, 105))
    projectile7_y = -200
    fenetre.blit(p7, (300, projectile7_y))

    p8 = pygame.transform.scale(p, (70, 105))
    projectile8_y = -200
    fenetre.blit(p8, (300, projectile8_y))

    p9 = pygame.transform.scale(p, (70, 105))
    projectile9_y = -200
    fenetre.blit(p9, (300, projectile9_y))

    p10 = pygame.transform.scale(p, (70, 105))
    projectile10_y = -200
    fenetre.blit(p10, (300, projectile10_y))

    p11 = pygame.transform.scale(p, (70, 105))
    projectile11_y = -200
    fenetre.blit(p11, (300, projectile11_y))

    p12 = pygame.transform.scale(p, (70, 105))
    projectile12_y = -200
    fenetre.blit(p12, (300, projectile12_y))

    p13 = pygame.transform.scale(p, (70, 105))
    projectile13_y = -200
    fenetre.blit(p13, (300, projectile13_y))

    p14 = pygame.transform.scale(p, (70, 105))
    projectile14_y = -200
    fenetre.blit(p14, (300, projectile14_y))

    p15 = pygame.transform.scale(p, (70, 105))
    projectile15_y = -200
    fenetre.blit(p15, (300, projectile15_y))

    p16 = pygame.transform.scale(p, (70, 105))
    projectile16_y = -200
    fenetre.blit(p16, (300, projectile16_y))

    p17 = pygame.transform.scale(p, (70, 105))
    projectile17_y = -200
    fenetre.blit(p17, (300, projectile17_y))

    p18 = pygame.transform.scale(p, (70, 105))
    projectile18_y = -200
    fenetre.blit(p18, (300, projectile18_y))

    p19 = pygame.transform.scale(p, (70, 105))
    projectile19_y = -200
    fenetre.blit(p19, (300, projectile19_y))

    p20 = pygame.transform.scale(p, (70, 105))
    projectile20_y = -200
    fenetre.blit(p20, (300, projectile20_y))

    p21 = pygame.transform.scale(p, (70, 105))
    projectile21_y = -200
    fenetre.blit(p21, (300, projectile21_y))

    pat_playing = False
    num_patern = 0
    lis_patern = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
    cmpt = 0

    # Pour la grosse FIRE BALL
    lis_pos = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]

    lis_pos2 = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 375]

    difficulte = 0  # =0 patern normale / >=1 mode fast_turbo aléatoire --> toutes augmentation de dificulté augmentera les chance de fast_turbo et l'appartion de paterne difficile et vitesse
    fast_turbo = 0

    start_time_chrono = time.time()

    # --- Initialisation des variables --- :
    perso_x = 512
    perso_y = 500

    v = 0.80  # vitesse de déplacement du perso

    perso_x_move = 0
    perso_y_move = 0

    #  -- coordonées des nuages :
    nx = -200
    ny = 400

    n1x = 1100
    n1y = 200

    n2x = 1300
    n2y = 225

    #  -- coordonées de la jauge :
    jauge_x = 35
    jauge_y = 700
    jauge_width = 0

    #  -- coordonées de la fiole :
    fiole_x = 1100
    fiole_y = 800
    fiole_lancee = True
    fiole_depart = 0
    limit_x1 = randint(-4000, -200)
    limit_x2 = randint(1200, 4000)

    # nb vie
    nb_vie = 3

    invincible = False

    #  -- coordonées du vent :
    vent_x = 1500
    vent_y = -500
    pouvoir_active = False
    start_time = time.time()
    puissance = 1
    #  -- mur de vent :
    murDeVent = False
    y_defini = False
    vent1_x = 1500
    vent2_x = 1500
    vent3_x = 1500
    vent4_x = 1500
    vent5_x = 1500
    vent6_x = 1500
    vent7_x = 1500
    vent8_x = 1500
    vent_mur_y = -500

    game_over = False
    coeff_invers = 1
    coeff_invers2 = 1
    coeff_invers3 = 1
    coeff_invers4 = 1
    coeff_invers5 = 1
    coeff_invers6 = 1
    coeff_invers7 = 1
    coeff_invers8 = 1
    coeff_invers9 = 1
    coeff_invers10 = 1
    coeff_invers11 = 1
    coeff_invers12 = 1
    coeff_invers13 = 1
    coeff_invers14 = 1
    coeff_invers15 = 1
    coeff_invers16 = 1
    coeff_invers17 = 1
    coeff_invers18 = 1
    coeff_invers19 = 1
    coeff_invers20 = 1
    coeff_invers21 = 1

    chrono_invincible_debut = 0
    # --- Boucle principale du jeu  --- :

    while not (game_over):
        if (nb_vie <= 0):
            game_over = True
            chrono = int(actual_time_chrono - start_time_chrono)
            #if volume_actif == True:
            #    son_courant.stop()
            #    son_vent.stop()
            son_basique.stop()
            son_moyen.stop()
            son_rapide.stop()
            
            son_courant.stop()
            son_vent.stop()

            #  /* -- Titre principal  */
            font = pygame.font.Font(None, 75)
            text = font.render("GAME OVER ! ", 1, (15, 15, 35))

            #  /* -- Gestion du son  */
            son = pygame.mixer.music.load("music/gameOver.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

            # titre principal :
            fenetre.blit(text, (350, 364))
            pygame.display.update()
            time.sleep(2)
            
            return chrono

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chrono_generale_final = 0
                game_over = True
                if volume_actif == True:
                    son_basique.stop()
                    son_moyen.stop()
                    son_rapide.stop()
                return False

            # --- Déplacement du personnage (touches du clavier)  --- :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    perso_y_move = -v
                if event.key == pygame.K_DOWN:
                    perso_y_move = v
                if event.key == pygame.K_RIGHT:
                    perso_x_move = v
                if event.key == pygame.K_LEFT:
                    perso_x_move = -v
                # --- Mise à 0 de la jauge (utilisation pouvoir) --- :
                if event.key == pygame.K_SPACE:
                    if jauge_width < 100:
                        puissance = 0
                    if jauge_width >= 100 and jauge_width < 200:
                        puissance = 1.5
                    if jauge_width >= 200:
                        puissance = 2.5
                    if jauge_width == 300:
                        puissance = 1.5
                        murDeVent = True
                        y_defini = False
                    if jauge_width >= 100:
                        jauge_width = 0
                    pouvoir_active = True
                    start_time = time.time()
            # --- fin ---
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    perso_y_move = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    perso_x_move = 0

        # --- Contraintes de déplacement du personnage --- :

        # -- Le perso ne dépasse pas la zone de l'écran -- :
        if perso_y >= 0 and perso_y <= surfaceH:
            perso_y += perso_y_move

        if perso_x >= 0 and perso_x <= surfaceW:
            perso_x += perso_x_move

        if perso_y < 0:
            perso_y = 0
        if perso_y > surfaceH - 100:
            perso_y = surfaceH - 100

        if perso_x < 0:
            perso_x = 0
        if perso_x > surfaceW - 70:
            perso_x = surfaceW - 70

        # --- Affichage des images + fond --- :

        fenetre.fill(blue)

        spone(n2x, n2y, nuage2)
        spone(nx, ny, nuage)
        spone(n1x, n1y, nuage1)

        # --- Contraintes de déplacement des nuages --- :
        if nx > 1100:
            nx = -150
        else:
            nx += 0.3

        if n1x < -200:
            n1x = 1100
        else:
            n1x -= 0.15

        if n2x < -700:
            n2x = 1100
        else:
            n2x -= 0.1

        spone(perso_x, perso_y, perso)  # le personnage doit être visible (par dessus les nuages)

        # --- Contraintes de déplacement de la jauge --- :

        if jauge_width < 300:
            jauge_width += 0.01
        else:
            jauge_width = 300
        jaugePouvoir(jauge, jauge_x, jauge_y, jauge_width)
        spone(jauge_x, 715, contour_jauge)

        # --- Contraintes d'apparition des fioles  --- :

        if fiole_x < limit_x1 or fiole_x > limit_x2:
            fiole_lancee = False

        if fiole_lancee == False:
            limit_x1 = randint(-1500, -200)  # gestion du temps d'apparition
            limit_x2 = randint(1200, 2500)
            fiole_depart = randint(0, 1)
            if fiole_depart == 0:
                fiole_x = -100
            else:
                fiole_x = 1100
            fiole_y = randint(50, 700)
            fiole_lancee = True

        if fiole_depart == 0:
            fiole_x += 0.2
        else:
            fiole_x -= 0.2

        fiole(redBull, fiole_x, fiole_y)

        # --- Gestion des collisions perso / fiole  --- :
        if perso_x >= fiole_x - 100 and perso_x <= fiole_x + 45 and perso_y >= fiole_y - 75 and perso_y <= fiole_y:
            jauge_width += 100
            fiole_y = -200

        # --- Gestion de l'utilisation du pouvoir --- :
        temps_actuel = time.time()
        if float(temps_actuel - start_time) >= float(2 * puissance):
            pouvoir_active = False
            murDeVent = False
            if volume_actif == True:
                son_vent.stop()
                son_courant.play()

        if pouvoir_active:
            if volume_actif == True:
                son_courant.stop()
                son_vent.play()
            if murDeVent:
                vent1_x = 14
                vent2_x = 142
                vent3_x = 270
                vent4_x = 398
                vent5_x = 526
                vent6_x = 654
                vent7_x = 782
                vent8_x = 910
                if y_defini == False:
                    vent_mur_y = perso_y - 110
                    y_defini = True
            else:
                vent_x = perso_x - 10
                vent_y = perso_y - 110
        else:
            vent_x = 1500
            vent_y = -500
            vent1_x = 1500
            vent2_x = 1500
            vent3_x = 1500
            vent4_x = 1500
            vent5_x = 1500
            vent6_x = 1500
            vent7_x = 1500
            vent8_x = 1500
            vent_mur_y = -500

        spone(vent_x, vent_y, vent)
        spone(vent1_x, vent_mur_y, vent)
        spone(vent2_x, vent_mur_y, vent)
        spone(vent3_x, vent_mur_y, vent)
        spone(vent4_x, vent_mur_y, vent)
        spone(vent5_x, vent_mur_y, vent)
        spone(vent6_x, vent_mur_y, vent)
        spone(vent7_x, vent_mur_y, vent)
        spone(vent8_x, vent_mur_y, vent)

        actuvie(nb_vie)  # actualisation de la vie

        # --- Text chrono + Difficulté  --- :

        actual_time_chrono = time.time()
        chrono = int(actual_time_chrono - start_time_chrono)

        font = pygame.font.Font(None, 40)  # 40 = taille de la police
        ton_text = font.render(str(chrono) + "s", 1, (255, 255, 255))
        fenetre.blit(ton_text, (960, 5))

        if (chrono < 20):
            difficulte = 0
            if volume_actif == True:
                son_basique.play()
        elif (chrono >= 20 and chrono < 40):
            difficulte = 1
            if volume_actif == True:
                son_basique.stop()
                son_moyen.play()
                son_courant = son_moyen
                
        elif (chrono >= 40 and chrono < 60):
            difficulte = 2
                
        elif (chrono >= 60 and chrono < 80):
            difficulte = 3
            son_moyen.stop()
            if volume_actif == True:
                son_moyen.stop()
                son_rapide.play()
                son_courant = son_rapide
        elif (chrono >= 80 and chrono < 90):
            difficulte = 4
        elif (chrono >= 90 and chrono < 100):
            difficulte = 5
        elif (chrono >= 100 and chrono < 110):
            difficulte = 6
        elif (chrono >= 110 and chrono < 120):
            difficulte = 7
        elif (chrono >= 120):
            difficulte = 8

        diff = ("Difficulte: " + str(difficulte))
        font = pygame.font.Font(None, 30)  # 40 = taille de la police
        text_diff = font.render(diff, 1, (255, 255, 255))
        fenetre.blit(text_diff, (900, 30))

        res = min(difficulte * 2, 5)

        # --- init nb aléatoire patern  --- :
        v = 0.80 + (difficulte / 5)
        if not (pat_playing):
            nb_ball = randint(2, res + 16)  # nb_patern
            if (nb_ball == 20):
                shuffle(lis_pos)
                difficulte_temp20 = difficulte
                projectile1_y = -700 - (difficulte_temp20 * 100)
                coef = 2 + difficulte

            if (nb_ball >= 14 and nb_ball <= 16):
                shuffle(lis_pos2)
            if (difficulte >= 1):
                fast_turbo = randint(0, 30 - difficulte * 2)

            shuffle(lis_patern)
            pat_playing = True

        # --- les patern fire ball

        if pat_playing:
            if nb_ball == 2:
                projectile1_y += (0.40 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (lis_patern[0], projectile1_y))

                projectile2_y += (0.46 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (lis_patern[1], projectile2_y))

                if not (invincible) and (perso_x + 65 >= lis_patern[0] and perso_x <= lis_patern[
                    0] + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[1] and perso_x <= lis_patern[
                    1] + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()
                ####################
                if (vent_x + 65 >= lis_patern[0] and vent_x <= lis_patern[
                    0] + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (vent_x + 65 >= lis_patern[1] and vent_x <= lis_patern[
                    1] + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1
                    ##############

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    pat_playing = False

            if nb_ball == 3:
                projectile1_y += (0.37 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (lis_patern[0], projectile1_y))

                projectile2_y += (0.5 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (lis_patern[1], projectile2_y))

                projectile3_y += (0.36 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (lis_patern[2], projectile3_y))

                if not (invincible) and (perso_x + 65 >= lis_patern[0] and perso_x <= lis_patern[
                    0] + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[1] and perso_x <= lis_patern[
                    1] + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[2] and perso_x <= lis_patern[
                    2] + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                #######

                if (vent_x + 65 >= lis_patern[0] and vent_x <= lis_patern[
                    0] + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (vent_x + 65 >= lis_patern[1] and vent_x <= lis_patern[
                    1] + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (vent_x + 65 >= lis_patern[2] and vent_x <= lis_patern[
                    2] + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    pat_playing = False

            if nb_ball >= 4 and nb_ball <= 9:
                projectile1_y += (0.36 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (lis_patern[0], projectile1_y))

                projectile2_y += (0.35 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (lis_patern[1], projectile2_y))

                projectile3_y += (0.4 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (lis_patern[2], projectile3_y))

                projectile4_y += (0.36 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (lis_patern[3], projectile4_y))

                if not (invincible) and (perso_x + 65 >= lis_patern[0] and perso_x <= lis_patern[
                    0] + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[1] and perso_x <= lis_patern[
                    1] + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[2] and perso_x <= lis_patern[
                    2] + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[3] and perso_x <= lis_patern[
                    3] + 60 and perso_y + 70 >= projectile4_y and perso_y <= projectile4_y + 95):
                    nb_vie -= 1
                    projectile4_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                    ####
                if (vent_x + 65 >= lis_patern[0] and vent_x <= lis_patern[
                    0] + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (vent_x + 65 >= lis_patern[1] and vent_x <= lis_patern[
                    1] + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (vent_x + 65 >= lis_patern[2] and vent_x <= lis_patern[
                    2] + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if (vent_x + 65 >= lis_patern[3] and vent_x <= lis_patern[
                    3] + 60 and vent_y + 70 >= projectile4_y and vent_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y and vent_mur_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    pat_playing = False

            if nb_ball >= 10 and nb_ball <= 15:
                projectile1_y += (0.35 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (lis_patern[0], projectile1_y))

                projectile2_y += (0.32 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (lis_patern[1], projectile2_y))

                projectile3_y += (0.41 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (lis_patern[2], projectile3_y))

                projectile4_y += (0.36 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (lis_patern[3], projectile4_y))

                projectile5_y += (0.36 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (lis_patern[4], projectile5_y))

                if not (invincible) and (perso_x + 65 >= lis_patern[0] and perso_x <= lis_patern[
                    0] + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[1] and perso_x <= lis_patern[
                    1] + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[2] and perso_x <= lis_patern[
                    2] + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[3] and perso_x <= lis_patern[
                    3] + 60 and perso_y + 70 >= projectile4_y and perso_y <= projectile4_y + 95):
                    nb_vie -= 1
                    projectile4_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_patern[4] and perso_x <= lis_patern[
                    4] + 60 and perso_y + 70 >= projectile5_y and perso_y <= projectile5_y + 95):
                    nb_vie -= 1
                    projectile5_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                #####

                if (vent_x + 65 >= lis_patern[0] and vent_x <= lis_patern[
                    0] + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (vent_x + 65 >= lis_patern[1] and vent_x <= lis_patern[
                    1] + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (vent_x + 65 >= lis_patern[2] and vent_x <= lis_patern[
                    2] + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if (vent_x + 65 >= lis_patern[3] and vent_x <= lis_patern[
                    3] + 60 and vent_y + 70 >= projectile4_y and vent_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if (vent_x + 65 >= lis_patern[4] and vent_x <= lis_patern[
                    4] + 60 and vent_y + 70 >= projectile5_y and vent_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                #####

                if murDeVent and (perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y and vent_mur_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile5_y and vent_mur_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    pat_playing = False

            if nb_ball >= 16 and nb_ball <= 16:

                projectile1_y += (0.365 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (lis_pos2[3], projectile1_y - 400))

                projectile2_y += (0.36 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (lis_pos2[4], projectile2_y - 252))

                projectile3_y += (0.40 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (lis_pos2[5], projectile3_y - 250))

                projectile4_y += (0.36 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (lis_pos2[6], projectile4_y - 400))

                projectile5_y += (0.37 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (lis_pos2[7], projectile5_y - 250))

                projectile6_y += (0.36 + (difficulte / 3)) * coeff_invers6
                fenetre.blit(p6, (lis_pos2[8], projectile6_y - 250))

                projectile7_y += (0.42 + (difficulte / 3)) * coeff_invers7
                fenetre.blit(p7, (lis_pos2[9], projectile7_y - 252))

                projectile8_y += (0.36 + (difficulte / 3)) * coeff_invers8
                fenetre.blit(p8, (lis_pos2[10], projectile8_y - 250))

                projectile9_y += (0.36 + (difficulte / 3)) * coeff_invers9
                fenetre.blit(p9, (lis_pos2[11], projectile9_y - 100))

                projectile10_y += (0.42 + (difficulte / 3)) * coeff_invers10
                fenetre.blit(p10, (lis_pos2[12], projectile10_y - 450))

                projectile11_y += (0.36 + (difficulte / 3)) * coeff_invers11
                fenetre.blit(p11, (lis_pos2[13], projectile11_y - 250))

                projectile12_y += (0.39 + (difficulte / 3)) * coeff_invers12
                fenetre.blit(p12, (lis_pos2[14], projectile12_y))

                projectile13_y += (0.36 + (difficulte / 3)) * coeff_invers13
                fenetre.blit(p13, (lis_pos2[15], projectile13_y))

                projectile14_y += (0.36 + (difficulte / 3)) * coeff_invers14
                fenetre.blit(p14, (lis_pos2[16], projectile14_y))

                projectile15_y += (0.36 + (difficulte / 3)) * coeff_invers15
                fenetre.blit(p15, (lis_pos2[17], projectile15_y))

                projectile16_y += (0.36 + (difficulte / 3)) * coeff_invers16
                fenetre.blit(p16, (lis_pos2[18], projectile16_y ))

                projectile17_y += (0.36 + (difficulte / 3)) * coeff_invers17
                fenetre.blit(p17, (lis_pos2[19], projectile17_y))

                projectile18_y += (0.36 + (difficulte / 3)) * coeff_invers18
                fenetre.blit(p18, (lis_pos2[20], projectile18_y ))

                if not (invincible) and (perso_x + 65 >= lis_pos2[3] and perso_x <= lis_pos2[
                    3] + 60 and perso_y + 70 >= projectile1_y - 400 and perso_y <= projectile1_y - 400 + 95):
                    nb_vie -= 1
                    projectile1_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[4] and perso_x <= lis_pos2[
                    4] + 60 and perso_y + 70 >= projectile2_y - 252 and perso_y <= projectile2_y - 252 + 95):
                    nb_vie -= 1
                    projectile2_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[5] and perso_x <= lis_pos2[
                    5] + 60 and perso_y + 70 >= projectile3_y - 250 and perso_y <= projectile3_y - 250 + 95):
                    nb_vie -= 1
                    projectile3_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[6] and perso_x <= lis_pos2[
                    6] + 60 and perso_y + 70 >= projectile4_y - 400 and perso_y <= projectile4_y - 400 + 95):
                    nb_vie -= 1
                    projectile4_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[7] and perso_x <= lis_pos2[
                    7] + 60 and perso_y + 70 >= projectile5_y - 250 and perso_y <= projectile5_y - 250 + 95):
                    nb_vie -= 1
                    projectile5_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[8] and perso_x <= lis_pos2[
                    8] + 60 and perso_y + 70 >= projectile6_y - 250 and perso_y <= projectile6_y - 250 + 95):
                    nb_vie -= 1
                    projectile6_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[9] and perso_x <= lis_pos2[
                    9] + 60 and perso_y + 70 >= projectile7_y - 252 and perso_y <= projectile7_y - 252 + 95):
                    nb_vie -= 1
                    projectile7_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[10] and perso_x <= lis_pos2[
                    10] + 60 and perso_y + 70 >= projectile8_y - 250 and perso_y <= projectile8_y - 250 + 95):
                    nb_vie -= 1
                    projectile8_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[11] and perso_x <= lis_pos2[
                    11] + 60 and perso_y + 70 >= projectile9_y - 100 and perso_y <= projectile9_y - 100 + 95):
                    nb_vie -= 1
                    projectile9_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[12] and perso_x <= lis_pos2[
                    12] + 60 and perso_y + 70 >= projectile10_y - 450 and perso_y <= projectile10_y - 450 + 95):
                    nb_vie -= 1
                    projectile10_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[13] and perso_x <= lis_pos2[
                    13] + 60 and perso_y + 70 >= projectile11_y - 250 and perso_y <= projectile11_y - 250 + 95):
                    nb_vie -= 1
                    projectile11_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[14] and perso_x <= lis_pos2[
                    14] + 60 and perso_y + 70 >= projectile12_y and perso_y <= projectile12_y + 95):
                    nb_vie -= 1
                    projectile12_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[15] and perso_x <= lis_pos2[
                    15] + 60 and perso_y + 70 >= projectile13_y and perso_y <= projectile13_y + 95):
                    nb_vie -= 1
                    projectile13_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[16] and perso_x <= lis_pos2[
                    16] + 60 and perso_y + 70 >= projectile14_y and perso_y <= projectile14_y + 95):
                    nb_vie -= 1
                    projectile14_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[17] and perso_x <= lis_pos2[
                    17] + 60 and perso_y + 70 >= projectile15_y and perso_y <= projectile15_y + 95):
                    nb_vie -= 1
                    projectile15_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[18] and perso_x <= lis_pos2[
                    18] + 60 and perso_y + 70 >= projectile16_y and perso_y <= projectile16_y + 95):
                    nb_vie -= 1
                    projectile16_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[19] and perso_x <= lis_pos2[
                    19] + 60 and perso_y + 70 >= projectile17_y and perso_y <= projectile17_y + 95):
                    nb_vie -= 1
                    projectile17_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (perso_x + 65 >= lis_pos2[20] and perso_x <= lis_pos2[
                    20] + 60 and perso_y + 70 >= projectile18_y and perso_y <= projectile18_y + 95):
                    nb_vie -= 1
                    projectile18_y = 1455
                    invincible = True
                    chrono_invincible_debut = time.time()

                ####

                if (vent_x + 65 >= lis_pos2[3] and vent_x <= lis_pos2[
                    3] + 60 and vent_y + 70 >= projectile1_y - 400 and vent_y <= projectile1_y - 400 + 95):
                    coeff_invers = -1

                if (vent_x + 65 >= lis_pos2[4] and vent_x <= lis_pos2[
                    4] + 60 and vent_y + 70 >= projectile2_y - 252 and vent_y <= projectile2_y - 252 + 95):
                    coeff_invers2 = -1

                if (vent_x + 65 >= lis_pos2[5] and vent_x <= lis_pos2[
                    5] + 60 and vent_y + 70 >= projectile3_y - 250 and vent_y <= projectile3_y - 250 + 95):
                    coeff_invers3 = -1

                if (vent_x + 65 >= lis_pos2[6] and vent_x <= lis_pos2[
                    6] + 60 and vent_y + 70 >= projectile4_y - 400 and vent_y <= projectile4_y - 400 + 95):
                    coeff_invers4 = -1

                if (vent_x + 65 >= lis_pos2[7] and vent_x <= lis_pos2[
                    7] + 60 and vent_y + 70 >= projectile5_y - 250 and vent_y <= projectile5_y - 250 + 95):
                    coeff_invers5 = -1

                if (vent_x + 65 >= lis_pos2[8] and vent_x <= lis_pos2[
                    8] + 60 and vent_y + 70 >= projectile6_y - 250 and vent_y <= projectile6_y - 250 + 95):
                    coeff_invers6 = -1

                if (vent_x + 65 >= lis_pos2[9] and vent_x <= lis_pos2[
                    9] + 60 and vent_y + 70 >= projectile7_y - 252 and vent_y <= projectile7_y - 252 + 95):
                    coeff_invers7 = -1

                if (vent_x + 65 >= lis_pos2[10] and vent_x <= lis_pos2[
                    10] + 60 and vent_y + 70 >= projectile8_y - 250 and vent_y <= projectile8_y - 250 + 95):
                    coeff_invers8 = -1

                if (vent_x + 65 >= lis_pos2[11] and vent_x <= lis_pos2[
                    11] + 60 and vent_y + 70 >= projectile9_y - 100 and vent_y <= projectile9_y - 100 + 95):
                    coeff_invers9 = -1

                if (vent_x + 65 >= lis_pos2[12] and vent_x <= lis_pos2[
                    12] + 60 and vent_y + 70 >= projectile10_y - 450 and vent_y <= projectile10_y - 450 + 95):
                    coeff_invers10 = -1

                if (vent_x + 65 >= lis_pos2[13] and vent_x <= lis_pos2[
                    13] + 60 and vent_y + 70 >= projectile11_y - 250 and vent_y <= projectile11_y - 250 + 95):
                    coeff_invers11 = -1

                if (vent_x + 65 >= lis_pos2[14] and vent_x <= lis_pos2[
                    14] + 60 and vent_y + 70 >= projectile12_y and vent_y <= projectile12_y + 95):
                    coeff_invers12 = -1

                if (vent_x + 65 >= lis_pos2[15] and vent_x <= lis_pos2[
                    15] + 60 and vent_y + 70 >= projectile13_y and vent_y <= projectile13_y + 95):
                    coeff_invers13 = -1

                if (vent_x + 65 >= lis_pos2[16] and vent_x <= lis_pos2[
                    16] + 60 and vent_y + 70 >= projectile14_y and vent_y <= projectile14_y + 95):
                    coeff_invers14 = -1

                if (vent_x + 65 >= lis_pos2[17] and vent_x <= lis_pos2[
                    17] + 60 and vent_y + 70 >= projectile15_y and vent_y <= projectile15_y + 95):
                    coeff_invers15 = -1

                if (vent_x + 65 >= lis_pos2[18] and vent_x <= lis_pos2[
                    18] + 60 and vent_y + 70 >= projectile16_y and vent_y <= projectile16_y + 95):
                    coeff_invers16 = -1

                if (vent_x + 65 >= lis_pos2[19] and vent_x <= lis_pos2[
                    19] + 60 and vent_y + 70 >= projectile17_y and vent_y <= projectile17_y + 95):
                    coeff_invers17 = -1

                if (vent_x + 65 >= lis_pos2[20] and vent_x <= lis_pos2[
                    20] + 60 and vent_y + 70 >= projectile18_y and vent_y <= projectile18_y + 95):
                    coeff_invers18 = -1

                #####

                if murDeVent and (vent_mur_y + 70 >= projectile1_y - 400 and vent_mur_y <= projectile1_y - 400 + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y - 252 and vent_mur_y <= projectile2_y - 252 + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y - 250 and vent_mur_y <= projectile3_y - 250 + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y - 400 and vent_mur_y <= projectile4_y - 400 + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile5_y - 250 and vent_mur_y <= projectile5_y - 250 + 95):
                    coeff_invers5 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile6_y - 250 and vent_mur_y <= projectile6_y - 250 + 95):
                    coeff_invers6 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile7_y - 252 and vent_mur_y <= projectile7_y - 252 + 95):
                    coeff_invers7 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile8_y - 250 and vent_mur_y <= projectile8_y - 250 + 95):
                    coeff_invers8 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile9_y - 100 and vent_mur_y <= projectile9_y - 100 + 95):
                    coeff_invers9 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile10_y - 450 and vent_mur_y <= projectile10_y - 450 + 95):
                    coeff_invers10 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile11_y - 250 and vent_mur_y <= projectile11_y - 250 + 95):
                    coeff_invers11 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile12_y and vent_mur_y <= projectile12_y + 95):
                    coeff_invers12 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile13_y and vent_mur_y <= projectile13_y + 95):
                    coeff_invers13 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile14_y and vent_mur_y <= projectile14_y + 95):
                    coeff_invers14 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile15_y and vent_mur_y <= projectile15_y + 95):
                    coeff_invers15 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile16_y and vent_mur_y <= projectile16_y + 95):
                    coeff_invers16 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile17_y and vent_mur_y <= projectile17_y + 95):
                    coeff_invers17 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile18_y and vent_mur_y <= projectile18_y + 95):
                    coeff_invers18 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210) and (
                        projectile6_y >= 1455 or projectile6_y <= -210) and (
                        projectile7_y >= 1455 or projectile7_y <= -210) and (
                        projectile8_y >= 1455 or projectile8_y <= -210) and (
                        projectile9_y >= 1455 or projectile9_y <= -210) and (
                        projectile10_y >= 1455 or projectile10_y <= -210) and (
                        projectile11_y >= 1455 or projectile11_y <= -210) and (
                        projectile12_y >= 1455 or projectile12_y <= -210) and (
                        projectile13_y >= 1455 or projectile13_y <= -210) and (
                        projectile14_y >= 1455 or projectile14_y <= -210) and (
                        projectile15_y >= 1455 or projectile15_y <= -210) and (
                        projectile16_y >= 1455 or projectile16_y <= -210) and (
                        projectile17_y >= 1455 or projectile17_y <= -210) and (
                        projectile18_y >= 1455 or projectile18_y <= -210)):  # pas besoin de faire tou les boule de la meme ligne
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    projectile6_y = -200
                    projectile7_y = -200
                    projectile8_y = -200
                    projectile9_y = -200
                    projectile10_y = -200
                    projectile11_y = -200
                    projectile12_y = -200
                    projectile13_y = -200
                    projectile14_y = -200
                    projectile15_y = -200
                    projectile16_y = -200
                    projectile17_y = -200
                    projectile18_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    coeff_invers6 = 1
                    coeff_invers7 = 1
                    coeff_invers8 = 1
                    coeff_invers9 = 1
                    coeff_invers10 = 1
                    coeff_invers11 = 1
                    coeff_invers12 = 1
                    coeff_invers13 = 1
                    coeff_invers14 = 1
                    coeff_invers15 = 1
                    coeff_invers16 = 1
                    coeff_invers17 = 1
                    coeff_invers18 = 1
                    pat_playing = False

            if nb_ball == 17:  ##lioke this /*     ****      */
                projectile1_y += (0.35 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (400, projectile1_y))

                projectile2_y += (0.35 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (450, projectile2_y))

                projectile3_y += (0.35 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (500, projectile3_y))

                projectile4_y += (0.35 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (550, projectile4_y))

                projectile5_y += (0.35 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (600, projectile5_y))

                projectile6_y += (0.35 + (difficulte / 3)) * coeff_invers6
                fenetre.blit(p6, (1, projectile6_y))

                projectile7_y += (0.35 + (difficulte / 3)) * coeff_invers7
                fenetre.blit(p7, (949, projectile7_y))

                if not (invincible) and (
                        perso_x + 65 >= 400 and perso_x <= 400 + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 450 and perso_x <= 450 + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 500 and perso_x <= 500 + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 550 and perso_x <= 550 + 60 and perso_y + 70 >= projectile4_y and perso_y <= projectile4_y + 95):
                    nb_vie -= 1
                    projectile4_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 600 and perso_x <= 600 + 60 and perso_y + 70 >= projectile5_y and perso_y <= projectile5_y + 95):
                    nb_vie -= 1
                    projectile5_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 1 and perso_x <= 1 + 60 and perso_y + 70 >= projectile6_y and perso_y <= projectile6_y + 95):
                    nb_vie -= 1
                    projectile6_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 949 and perso_x <= 949 + 60 and perso_y + 70 >= projectile7_y and perso_y <= projectile7_y + 95):
                    nb_vie -= 1
                    projectile7_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                #######

                if (
                        vent_x + 65 >= 400 and vent_x <= 400 + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (
                        vent_x + 65 >= 450 and vent_x <= 450 + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (
                        vent_x + 65 >= 500 and vent_x <= 500 + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if (
                        vent_x + 65 >= 550 and vent_x <= 550 + 60 and vent_y + 70 >= projectile4_y and vent_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if (
                        vent_x + 65 >= 600 and vent_x <= 600 + 60 and vent_y + 70 >= projectile5_y and vent_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if (
                        vent_x + 65 >= 1 and vent_x <= 1 + 60 and vent_y + 70 >= projectile6_y and vent_y <= projectile6_y + 95):
                    coeff_invers6 = -1

                if (
                        vent_x + 65 >= 949 and vent_x <= 949 + 60 and vent_y + 70 >= projectile7_y and vent_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                #####

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y and vent_mur_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile5_y and vent_mur_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile6_y and vent_mur_y <= projectile6_y + 95):
                    coeff_invers6 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile7_y and vent_mur_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210) and (
                        projectile6_y >= 1455 or projectile6_y <= -210) and (
                        projectile7_y >= 1455 or projectile7_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    projectile6_y = -200
                    projectile7_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    coeff_invers6 = 1
                    coeff_invers7 = 1
                    pat_playing = False

            if nb_ball == 18:  ##lioke this /*****   *****/
                projectile1_y += (0.35 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (0, projectile1_y))

                projectile2_y += (0.35 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (50, projectile2_y))

                projectile3_y += (0.35 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (100, projectile3_y))

                projectile4_y += (0.35 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (150, projectile4_y))

                projectile5_y += (0.35 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (200, projectile5_y))

                projectile6_y += (0.35 + (difficulte / 3)) * coeff_invers6
                fenetre.blit(p6, (750, projectile6_y))

                projectile7_y += (0.35 + (difficulte / 3)) * coeff_invers7
                fenetre.blit(p7, (800, projectile7_y))

                projectile8_y += (0.35 + (difficulte / 3)) * coeff_invers8
                fenetre.blit(p8, (850, projectile8_y))

                projectile9_y += (0.35 + (difficulte / 3)) * coeff_invers9
                fenetre.blit(p9, (900, projectile9_y))

                projectile10_y += (0.35 + (difficulte / 3)) * coeff_invers10
                fenetre.blit(p10, (950, projectile10_y))

                if not (invincible) and (
                        perso_x + 65 >= 0 and perso_x <= 0 + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 50 and perso_x <= 50 + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 100 and perso_x <= 100 + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 150 and perso_x <= 150 + 60 and perso_y + 70 >= projectile4_y and perso_y <= projectile4_y + 95):
                    nb_vie -= 1
                    projectile4_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 200 and perso_x <= 200 + 60 and perso_y + 70 >= projectile5_y and perso_y <= projectile5_y + 95):
                    nb_vie -= 1
                    projectile5_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 750 and perso_x <= 750 + 60 and perso_y + 70 >= projectile6_y and perso_y <= projectile6_y + 95):
                    nb_vie -= 1
                    projectile6_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 800 and perso_x <= 800 + 60 and perso_y + 70 >= projectile7_y and perso_y <= projectile7_y + 95):
                    nb_vie -= 1
                    projectile7_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 850 and perso_x <= 850 + 60 and perso_y + 70 >= projectile8_y and perso_y <= projectile8_y + 95):
                    nb_vie -= 1
                    projectile8_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 900 and perso_x <= 900 + 60 and perso_y + 70 >= projectile9_y and perso_y <= projectile9_y + 95):
                    nb_vie -= 1
                    projectile9_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 950 and perso_x <= 950 + 60 and perso_y + 70 >= projectile10_y and perso_y <= projectile10_y + 95):
                    nb_vie -= 1
                    projectile10_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                ####

                if (
                        vent_x + 65 >= 0 and vent_x <= 0 + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (
                        vent_x + 65 >= 50 and vent_x <= 50 + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (
                        vent_x + 65 >= 100 and vent_x <= 100 + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if (
                        vent_x + 65 >= 150 and vent_x <= 150 + 60 and vent_y + 70 >= projectile4_y and vent_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if (
                        vent_x + 65 >= 200 and vent_x <= 200 + 60 and vent_y + 70 >= projectile5_y and vent_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if (
                        vent_x + 65 >= 750 and vent_x <= 750 + 60 and vent_y + 70 >= projectile6_y and vent_y <= projectile6_y + 95):
                    coeff_invers6 = -1

                if (
                        vent_x + 65 >= 800 and vent_x <= 800 + 60 and vent_y + 70 >= projectile7_y and vent_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                if (
                        vent_x + 65 >= 850 and vent_x <= 850 + 60 and vent_y + 70 >= projectile8_y and vent_y <= projectile8_y + 95):
                    coeff_invers8 = -1

                if (
                        vent_x + 65 >= 900 and vent_x <= 900 + 60 and vent_y + 70 >= projectile9_y and vent_y <= projectile9_y + 95):
                    coeff_invers9 = -1

                if (
                        vent_x + 65 >= 950 and vent_x <= 950 + 60 and vent_y + 70 >= projectile10_y and vent_y <= projectile10_y + 95):
                    coeff_invers10 = -1

                #####

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y and vent_mur_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile5_y and vent_mur_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile6_y and vent_mur_y <= projectile6_y + 95):
                    coeff_invers6 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile7_y and vent_mur_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile8_y and vent_mur_y <= projectile8_y + 95):
                    coeff_invers8 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile9_y and vent_mur_y <= projectile9_y + 95):
                    coeff_invers9 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile10_y and vent_mur_y <= projectile10_y + 95):
                    coeff_invers10 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210) and (
                        projectile6_y >= 1455 or projectile6_y <= -210) and (
                        projectile7_y >= 1455 or projectile7_y <= -210) and (
                        projectile8_y >= 1455 or projectile8_y <= -210) and (
                        projectile9_y >= 1455 or projectile9_y <= -210) and (
                        projectile10_y >= 1455 or projectile10_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    projectile6_y = -200
                    projectile7_y = -200
                    projectile8_y = -200
                    projectile9_y = -200
                    projectile10_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    coeff_invers6 = 1
                    coeff_invers7 = 1
                    coeff_invers8 = 1
                    coeff_invers9 = 1
                    coeff_invers10 = 1
                    pat_playing = False

            if nb_ball == 19:  # *
                projectile1_y += (0.75 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (0, projectile1_y))
                # *
                projectile2_y += (0.70 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (100, projectile2_y))

                projectile3_y += (0.65 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p3, (200, projectile3_y))

                projectile4_y += (0.60 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p4, (300, projectile4_y))

                projectile5_y += (0.55 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (400, projectile5_y))

                projectile7_y += (0.50 + (difficulte / 3)) * coeff_invers7
                fenetre.blit(p7, (600, projectile7_y))

                projectile8_y += (0.45 + (difficulte / 3)) * coeff_invers8
                fenetre.blit(p8, (700, projectile8_y))

                projectile9_y += (0.40 + (difficulte / 3)) * coeff_invers9
                fenetre.blit(p9, (800, projectile9_y))

                projectile10_y += (0.35 + (difficulte / 3)) * coeff_invers10
                fenetre.blit(p10, (900, projectile10_y))

                if not (invincible) and (
                        perso_x + 65 >= 0 and perso_x <= 0 + 60 and perso_y + 70 >= projectile1_y and perso_y <= projectile1_y + 95):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 100 and perso_x <= 100 + 60 and perso_y + 70 >= projectile2_y and perso_y <= projectile2_y + 95):
                    nb_vie -= 1
                    projectile2_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 200 and perso_x <= 200 + 60 and perso_y + 70 >= projectile3_y and perso_y <= projectile3_y + 95):
                    nb_vie -= 1
                    projectile3_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 300 and perso_x <= 300 + 60 and perso_y + 70 >= projectile4_y and perso_y <= projectile4_y + 95):
                    nb_vie -= 1
                    projectile4_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 400 and perso_x <= 400 + 60 and perso_y + 70 >= projectile5_y and perso_y <= projectile5_y + 95):
                    nb_vie -= 1
                    projectile5_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 600 and perso_x <= 600 + 60 and perso_y + 70 >= projectile7_y and perso_y <= projectile7_y + 95):
                    nb_vie -= 1
                    projectile7_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 700 and perso_x <= 700 + 60 and perso_y + 70 >= projectile8_y and perso_y <= projectile8_y + 95):
                    nb_vie -= 1
                    projectile8_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 800 and perso_x <= 800 + 60 and perso_y + 70 >= projectile9_y and perso_y <= projectile9_y + 95):
                    nb_vie -= 1
                    projectile9_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 900 and perso_x <= 900 + 60 and perso_y + 70 >= projectile10_y and perso_y <= projectile10_y + 95):
                    nb_vie -= 1
                    projectile10_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                ####

                if (
                        vent_x + 65 >= 0 and vent_x <= 0 + 60 and vent_y + 70 >= projectile1_y and vent_y <= projectile1_y + 95):
                    coeff_invers = -1

                if (
                        vent_x + 65 >= 100 and vent_x <= 100 + 60 and vent_y + 70 >= projectile2_y and vent_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if (
                        vent_x + 65 >= 200 and vent_x <= 200 + 60 and vent_y + 70 >= projectile3_y and vent_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if (
                        vent_x + 65 >= 300 and vent_x <= 300 + 60 and vent_y + 70 >= projectile4_y and vent_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if (
                        vent_x + 65 >= 400 and vent_x <= 400 + 60 and vent_y + 70 >= projectile5_y and vent_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if (
                        vent_x + 65 >= 600 and vent_x <= 600 + 60 and vent_y + 70 >= projectile7_y and vent_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                if (
                        vent_x + 65 >= 700 and vent_x <= 700 + 60 and vent_y + 70 >= projectile8_y and vent_y <= projectile8_y + 95):
                    coeff_invers8 = -1

                if (
                        vent_x + 65 >= 800 and vent_x <= 800 + 60 and vent_y + 70 >= projectile9_y and vent_y <= projectile9_y + 95):
                    coeff_invers9 = -1

                if (
                        vent_x + 65 >= 900 and vent_x <= 900 + 60 and vent_y + 70 >= projectile10_y and vent_y <= projectile10_y + 95):
                    coeff_invers10 = -1

                #####

                if murDeVent and (vent_mur_y + 70 >= projectile1_y and vent_mur_y <= projectile1_y + 95):
                    coeff_invers = -1

                if murDeVent and (vent_mur_y + 70 >= projectile2_y and vent_mur_y <= projectile2_y + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile3_y and vent_mur_y <= projectile3_y + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile4_y and vent_mur_y <= projectile4_y + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile5_y and vent_mur_y <= projectile5_y + 95):
                    coeff_invers5 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile7_y and vent_mur_y <= projectile7_y + 95):
                    coeff_invers7 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile8_y and vent_mur_y <= projectile8_y + 95):
                    coeff_invers8 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile9_y and vent_mur_y <= projectile9_y + 95):
                    coeff_invers9 = -1

                if murDeVent and (vent_mur_y + 70 >= projectile10_y and vent_mur_y <= projectile10_y + 95):
                    coeff_invers10 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210) and (
                        projectile7_y >= 1455 or projectile7_y <= -210) and (
                        projectile8_y >= 1455 or projectile8_y <= -210) and (
                        projectile9_y >= 1455 or projectile9_y <= -210) and (
                        projectile10_y >= 1455 or projectile10_y <= -210)):
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    projectile7_y = -200
                    projectile8_y = -200
                    projectile9_y = -200
                    projectile10_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    coeff_invers7 = 1
                    coeff_invers8 = 1
                    coeff_invers9 = 1
                    coeff_invers10 = 1

                    pat_playing = False

            if nb_ball == 20:  # /      O       /

                projectile1_y += (0.60 + (difficulte_temp20 / 3)) * coeff_invers
                fenetre.blit(p1, (lis_pos[0], projectile1_y))
                p1 = pygame.transform.scale(p1, (90 * coef, 105 * coef))

                if (coef >= 3):
                    coef -= 1
                if (coef >= 4):
                    coef -= 1

                if not (invincible) and (perso_x + 0 >= lis_pos[0] - (18 * coef) and perso_x <= lis_pos[0] + (
                        78 * coef) and perso_y + 0 >= projectile1_y - (32 * coef) and perso_y <= projectile1_y + (
                                                 90 * coef)):
                    nb_vie -= 1
                    projectile1_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if (vent_x + 0 >= lis_pos[0] - (18 * coef) and vent_x <= lis_pos[0] + (
                        78 * coef) and vent_y + 0 >= projectile1_y - (32 * coef) and vent_y <= projectile1_y + (
                        90 * coef)):
                    coeff_invers = -1

                if (projectile1_y >= 800 or projectile1_y <= -210):
                    p1 = pygame.transform.scale(p1, (70, 105))
                    projectile1_y = -200
                    coeff_invers = 1
                    pat_playing = False

            if nb_ball == 21:  ##lioke this /*****
                # *****/
                projectile1_y += (0.36 + (difficulte / 3)) * coeff_invers
                fenetre.blit(p1, (0, projectile1_y - 250))

                projectile2_y += (0.36 + (difficulte / 3)) * coeff_invers2
                fenetre.blit(p2, (50, projectile2_y - 250))

                projectile3_y += (0.36 + (difficulte / 3)) * coeff_invers3
                fenetre.blit(p3, (100, projectile3_y - 250))

                projectile4_y += (0.36 + (difficulte / 3)) * coeff_invers4
                fenetre.blit(p4, (150, projectile4_y - 250))

                projectile5_y += (0.36 + (difficulte / 3)) * coeff_invers5
                fenetre.blit(p5, (200, projectile5_y - 250))

                projectile6_y += (0.36 + (difficulte / 3)) * coeff_invers6
                fenetre.blit(p6, (250, projectile6_y - 250))

                projectile7_y += (0.36 + (difficulte / 3)) * coeff_invers7
                fenetre.blit(p7, (300, projectile7_y - 250))

                projectile8_y += (0.36 + (difficulte / 3)) * coeff_invers8
                fenetre.blit(p8, (350, projectile8_y - 250))

                projectile9_y += (0.36 + (difficulte / 3)) * coeff_invers9
                fenetre.blit(p9, (400, projectile9_y - 250))

                projectile10_y += (0.36 + (difficulte / 3)) * coeff_invers10
                fenetre.blit(p10, (450, projectile10_y - 250))

                projectile13_y += (0.36 + (difficulte / 3)) * coeff_invers13
                fenetre.blit(p13, (550, projectile13_y))

                projectile14_y += (0.36 + (difficulte / 3)) * coeff_invers14
                fenetre.blit(p14, (600, projectile14_y))

                projectile15_y += (0.36 + (difficulte / 3)) * coeff_invers15
                fenetre.blit(p15, (650, projectile15_y))

                projectile16_y += (0.36 + (difficulte / 3)) * coeff_invers16
                fenetre.blit(p16, (700, projectile16_y))

                projectile17_y += (0.36 + (difficulte / 3)) * coeff_invers17
                fenetre.blit(p17, (750, projectile17_y))

                projectile18_y += (0.36 + (difficulte / 3)) * coeff_invers18
                fenetre.blit(p18, (800, projectile18_y))

                projectile19_y += (0.36 + (difficulte / 3)) * coeff_invers19
                fenetre.blit(p19, (850, projectile19_y))

                projectile20_y += (0.36 + (difficulte / 3)) * coeff_invers20
                fenetre.blit(p20, (900, projectile20_y))

                projectile21_y += (0.36 + (difficulte / 3)) * coeff_invers21
                fenetre.blit(p21, (950, projectile21_y))

                if not (invincible) and (
                        perso_x + 65 >= 0 and perso_x <= 0 + 60 and perso_y + 70 >= projectile1_y - 250 and perso_y <= projectile1_y - 250 + 95):
                    nb_vie -= 1
                    projectile1_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 50 and perso_x <= 50 + 60 and perso_y + 70 >= projectile2_y - 250 and perso_y <= projectile2_y - 250 + 95):
                    nb_vie -= 1
                    projectile2_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 100 and perso_x <= 100 + 60 and perso_y + 70 >= projectile3_y - 250 and perso_y <= projectile3_y - 250 + 95):
                    nb_vie -= 1
                    projectile3_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 150 and perso_x <= 150 + 60 and perso_y + 70 >= projectile4_y - 250 and perso_y <= projectile4_y - 250 + 95):
                    nb_vie -= 1
                    projectile4_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 200 and perso_x <= 200 + 60 and perso_y + 70 >= projectile5_y - 250 and perso_y <= projectile5_y - 250 + 95):
                    nb_vie -= 1
                    projectile5_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 250 and perso_x <= 250 + 60 and perso_y + 70 >= projectile6_y - 250 and perso_y <= projectile6_y - 250 + 95):
                    nb_vie -= 1
                    projectile6_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 300 and perso_x <= 300 + 60 and perso_y + 70 >= projectile7_y - 250 and perso_y <= projectile7_y - 250 + 95):
                    nb_vie -= 1
                    projectile7_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 350 and perso_x <= 350 + 60 and perso_y + 70 >= projectile8_y - 250 and perso_y <= projectile8_y - 250 + 95):
                    nb_vie -= 1
                    projectile8_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 400 and perso_x <= 400 + 60 and perso_y + 70 >= projectile9_y - 250 and perso_y <= projectile9_y - 250 + 95):
                    nb_vie -= 1
                    projectile9_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 450 and perso_x <= 450 + 60 and perso_y + 70 >= projectile10_y - 250 and perso_y <= projectile10_y - 250 + 95):
                    nb_vie -= 1
                    projectile10_y = 1200
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 550 and perso_x <= 550 + 60 and perso_y + 70 >= projectile13_y and perso_y <= projectile13_y + 95):
                    nb_vie -= 1
                    projectile13_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 600 and perso_x <= 600 + 60 and perso_y + 70 >= projectile14_y and perso_y <= projectile14_y + 95):
                    nb_vie -= 1
                    projectile14_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 650 and perso_x <= 650 + 60 and perso_y + 70 >= projectile15_y and perso_y <= projectile15_y + 95):
                    nb_vie -= 1
                    projectile15_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 700 and perso_x <= 700 + 60 and perso_y + 70 >= projectile16_y and perso_y <= projectile16_y + 95):
                    nb_vie -= 1
                    projectile16_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 750 and perso_x <= 750 + 60 and perso_y + 70 >= projectile17_y and perso_y <= projectile17_y + 95):
                    nb_vie -= 1
                    projectile17_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 800 and perso_x <= 800 + 60 and perso_y + 70 >= projectile18_y and perso_y <= projectile18_y + 95):
                    nb_vie -= 1
                    projectile18_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 850 and perso_x <= 850 + 60 and perso_y + 70 >= projectile19_y and perso_y <= projectile19_y + 95):
                    nb_vie -= 1
                    projectile19_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 900 and perso_x <= 900 + 60 and perso_y + 70 >= projectile20_y and perso_y <= projectile20_y + 95):
                    nb_vie -= 1
                    projectile20_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                if not (invincible) and (
                        perso_x + 65 >= 950 and perso_x <= 950 + 60 and perso_y + 70 >= projectile21_y and perso_y <= projectile21_y + 95):
                    nb_vie -= 1
                    projectile21_y = 850
                    invincible = True
                    chrono_invincible_debut = time.time()

                ##
                if (
                        vent_x + 65 >= 0 and vent_x <= 0 + 60 and vent_y + 70 >= projectile1_y - 250 and vent_y <= projectile1_y - 250 + 95):
                    coeff_invers = -1

                if (
                        vent_x + 65 >= 50 and vent_x <= 50 + 60 and vent_y + 70 >= projectile2_y - 250 and vent_y <= projectile2_y - 250 + 95):
                    coeff_invers2 = -1

                if (
                        vent_x + 65 >= 100 and vent_x <= 100 + 60 and vent_y + 70 >= projectile3_y - 250 and vent_y <= projectile3_y - 250 + 95):
                    coeff_invers3 = -1

                if (
                        vent_x + 65 >= 150 and vent_x <= 150 + 60 and vent_y + 70 >= projectile4_y - 250 and vent_y <= projectile4_y - 250 + 95):
                    coeff_invers4 = -1

                if (
                        vent_x + 65 >= 200 and vent_x <= 200 + 60 and vent_y + 70 >= projectile5_y - 250 and vent_y <= projectile5_y - 250 + 95):
                    coeff_invers5 = -1

                if (
                        vent_x + 65 >= 250 and vent_x <= 250 + 60 and vent_y + 70 >= projectile6_y - 250 and vent_y <= projectile6_y - 250 + 95):
                    coeff_invers6 = -1

                if (
                        vent_x + 65 >= 300 and vent_x <= 300 + 60 and vent_y + 70 >= projectile7_y - 250 and vent_y <= projectile7_y - 250 + 95):
                    coeff_invers7 = -1

                if (
                        vent_x + 65 >= 350 and vent_x <= 350 + 60 and vent_y + 70 >= projectile8_y - 250 and vent_y <= projectile8_y - 250 + 95):
                    coeff_invers8 = -1

                if (
                        vent_x + 65 >= 400 and vent_x <= 400 + 60 and vent_y + 70 >= projectile9_y - 250 and vent_y <= projectile9_y - 250 + 95):
                    coeff_invers9 = -1

                if (
                        vent_x + 65 >= 450 and vent_x <= 450 + 60 and vent_y + 70 >= projectile10_y - 250 and vent_y <= projectile10_y - 250 + 95):
                    coeff_invers10 = -1

                if (
                        vent_x + 65 >= 550 and vent_x <= 550 + 60 and vent_y + 70 >= projectile13_y and vent_y <= projectile13_y + 95):
                    coeff_invers13 = -1

                if (
                        vent_x + 65 >= 600 and vent_x <= 600 + 60 and vent_y + 70 >= projectile14_y and vent_y <= projectile14_y + 95):
                    coeff_invers14 = -1

                if (
                        vent_x + 65 >= 650 and vent_x <= 650 + 60 and vent_y + 70 >= projectile15_y and vent_y <= projectile15_y + 95):
                    coeff_invers15 = -1

                if (
                        vent_x + 65 >= 700 and vent_x <= 700 + 60 and vent_y + 70 >= projectile16_y and vent_y <= projectile16_y + 95):
                    coeff_invers16 = -1

                if (
                        vent_x + 65 >= 750 and vent_x <= 750 + 60 and vent_y + 70 >= projectile17_y and vent_y <= projectile17_y + 95):
                    coeff_invers17 = -1

                if (
                        vent_x + 65 >= 800 and vent_x <= 800 + 60 and vent_y + 70 >= projectile18_y and vent_y <= projectile18_y + 95):
                    coeff_invers18 = -1

                if (
                        vent_x + 65 >= 850 and vent_x <= 850 + 60 and vent_y + 70 >= projectile19_y and vent_y <= projectile19_y + 95):
                    coeff_invers19 = -1

                if (
                        vent_x + 65 >= 900 and vent_x <= 900 + 60 and vent_y + 70 >= projectile20_y and vent_y <= projectile20_y + 95):
                    coeff_invers20 = -1

                if (
                        vent_x + 65 >= 950 and vent_x <= 950 + 60 and vent_y + 70 >= projectile21_y and vent_y <= projectile21_y + 95):
                    coeff_invers21 = -1

                #####

                if murDeVent and (vent_y + 70 >= projectile1_y - 250 and vent_y <= projectile1_y - 250 + 95):
                    coeff_invers = -1

                if murDeVent and (vent_y + 70 >= projectile2_y - 250 and vent_y <= projectile2_y - 250 + 95):
                    coeff_invers2 = -1

                if murDeVent and (vent_y + 70 >= projectile3_y - 250 and vent_y <= projectile3_y - 250 + 95):
                    coeff_invers3 = -1

                if murDeVent and (vent_y + 70 >= projectile4_y - 250 and vent_y <= projectile4_y - 250 + 95):
                    coeff_invers4 = -1

                if murDeVent and (vent_y + 70 >= projectile5_y - 250 and vent_y <= projectile5_y - 250 + 95):
                    coeff_invers5 = -1

                if murDeVent and (vent_y + 70 >= projectile6_y - 250 and vent_y <= projectile6_y - 250 + 95):
                    coeff_invers6 = -1

                if murDeVent and (vent_y + 70 >= projectile7_y - 250 and vent_y <= projectile7_y - 250 + 95):
                    coeff_invers7 = -1

                if murDeVent and (vent_y + 70 >= projectile8_y - 250 and vent_y <= projectile8_y - 250 + 95):
                    coeff_invers8 = -1

                if murDeVent and (vent_y + 70 >= projectile9_y - 250 and vent_y <= projectile9_y - 250 + 95):
                    coeff_invers9 = -1

                if murDeVent and (vent_y + 70 >= projectile10_y - 250 and vent_y <= projectile10_y - 250 + 95):
                    coeff_invers10 = -1

                if murDeVent and (vent_y + 70 >= projectile13_y and vent_y <= projectile13_y + 95):
                    coeff_invers13 = -1

                if murDeVent and (vent_y + 70 >= projectile14_y and vent_y <= projectile14_y + 95):
                    coeff_invers14 = -1

                if murDeVent and (vent_y + 70 >= projectile15_y and vent_y <= projectile15_y + 95):
                    coeff_invers15 = -1

                if murDeVent and (vent_y + 70 >= projectile16_y and vent_y <= projectile16_y + 95):
                    coeff_invers16 = -1

                if murDeVent and (vent_y + 70 >= projectile17_y and vent_y <= projectile17_y + 95):
                    coeff_invers17 = -1

                if murDeVent and (vent_y + 70 >= projectile18_y and vent_y <= projectile18_y + 95):
                    coeff_invers18 = -1

                if murDeVent and (vent_y + 70 >= projectile19_y and vent_y <= projectile19_y + 95):
                    coeff_invers19 = -1

                if murDeVent and (vent_y + 70 >= projectile20_y and vent_y <= projectile20_y + 95):
                    coeff_invers20 = -1

                if murDeVent and (vent_y + 70 >= projectile21_y and vent_y <= projectile21_y + 95):
                    coeff_invers21 = -1

                if ((projectile2_y >= 800 or projectile2_y <= -210) and (
                        projectile1_y >= 800 or projectile1_y <= -210) and (
                        projectile3_y >= 800 or projectile3_y <= -210) and (
                        projectile4_y >= 800 or projectile4_y <= -210) and (
                        projectile5_y >= 800 or projectile5_y <= -210) and (
                        projectile6_y >= 1455 or projectile6_y <= -210) and (
                        projectile7_y >= 1455 or projectile7_y <= -210) and (
                        projectile8_y >= 1455 or projectile8_y <= -210) and (
                        projectile9_y >= 1455 or projectile9_y <= -210) and (
                        projectile10_y >= 1455 or projectile10_y <= -210) and (
                        projectile13_y >= 1455 or projectile13_y <= -210) and (
                        projectile14_y >= 1455 or projectile14_y <= -210) and (
                        projectile15_y >= 1455 or projectile15_y <= -210) and (
                        projectile16_y >= 1455 or projectile16_y <= -210) and (
                        projectile17_y >= 1455 or projectile17_y <= -210) and (
                        projectile18_y >= 1455 or projectile18_y <= -210) and (
                        projectile19_y >= 1455 or projectile19_y <= -210) and (
                        projectile20_y >= 1455 or projectile20_y <= -210) and (
                        projectile21_y >= 1455 or projectile21_y <= -210)):  # pas besoin de faire tou les boule de la meme ligne
                    projectile1_y = -200
                    projectile2_y = -200
                    projectile3_y = -200
                    projectile4_y = -200
                    projectile5_y = -200
                    projectile6_y = -200
                    projectile7_y = -200
                    projectile8_y = -200
                    projectile9_y = -200
                    projectile10_y = -200
                    projectile13_y = -200
                    projectile14_y = -200
                    projectile15_y = -200
                    projectile16_y = -200
                    projectile17_y = -200
                    projectile18_y = -200
                    projectile19_y = -200
                    projectile20_y = -200
                    projectile21_y = -200
                    coeff_invers = 1
                    coeff_invers2 = 1
                    coeff_invers3 = 1
                    coeff_invers4 = 1
                    coeff_invers5 = 1
                    coeff_invers6 = 1
                    coeff_invers7 = 1
                    coeff_invers8 = 1
                    coeff_invers9 = 1
                    coeff_invers10 = 1
                    coeff_invers13 = 1
                    coeff_invers14 = 1
                    coeff_invers15 = 1
                    coeff_invers16 = 1
                    coeff_invers17 = 1
                    coeff_invers18 = 1
                    coeff_invers19 = 1
                    coeff_invers20 = 1
                    coeff_invers21 = 1

                    pat_playing = False

            if (fast_turbo == 1 or fast_turbo == 2 or fast_turbo == 3):
                projectile4_y += 0.8 + (difficulte / 3)
            if (fast_turbo == 10):
                projectile1_y += 0.8 + (difficulte / 3)
                projectile5_y += 0.7 + (difficulte / 3)
                projectile8_y += 0.8 + (difficulte / 3)

        if (invincible == True):
            if (int(time.time() - chrono_invincible_debut) > 0.5):
                if volume_actif == True:
                    son_aoutch.stop()
                    son_courant.play()
            else:
                if volume_actif == True:
                    son_courant.stop()
                    son_aoutch.play()
                    son_aoutch_deja_joue = True
            if (int(time.time() - chrono_invincible_debut) % 2 == 0):
                if (type_skin_perso == True):
                    perso = persomalade
                    type_skin_perso = False
                else:
                    perso = perso_normal
                    type_skin_perso = True

            if int(time.time() - chrono_invincible_debut) >= 2:
                invincible = False
                if volume_actif == True:
                    son_aoutch_deja_joue = False
                perso = perso_normal
                type_skin_perso = True

        pygame.display.update()

    # --- Fin du programme --- :
def vrai_start(url, volume_actif):
    res = start(url,volume_actif)
    if(res):
        fichier.start_fichier(res, volume_actif, url)
