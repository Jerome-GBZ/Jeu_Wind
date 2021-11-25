#  /* --Importation des bibliothèques nécessaires */
import pygame


#  /* --Initialisation de la bibliothèque Pygame */
pygame.init()
pygame.display.set_caption('Wind Master - GAME OVER')

#  /* --Création de la fenêtre */
fenetre = pygame.display.set_mode((500, 380))

#  /* --set background color blue */
color = (119, 180, 254)

#  /* --Variable déterminante du lancement de la boucle principale */
game_over = True

#  /* -- Titre principal  */
font = pygame.font.Font(None, 75)
text = font.render("GAME OVER ! ", 1, (15, 15, 35))

#  /* -- Gestion du son  */

son = pygame.mixer.music.load("music/gameOver.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

while game_over:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
             pygame.mixer.music.stop()
             game_over = False  # On arrête la boucle

    fenetre.fill(color)
     # titre principal :
    fenetre.blit(text, (80, 165))
    pygame.display.update()

pygame.quit()

