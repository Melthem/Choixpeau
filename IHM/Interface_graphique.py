import py
import pygame
import math
pygame.init()


class Game:
    def __init__(self):
        self.jeu_lancé = False


game = Game()


# Création de la fenêtre
pygame.display.set_caption("Choixpeau magique") #changer le titre de la fenêtre
screen = pygame.display.set_mode((1200, 700)) #Définir la taille de la fenêtre (largeur, hauteur)


# Ajouter un fond
background = pygame.image.load("fond_choipxeau.jpg")
background = pygame.transform.scale(background, (1200, 850))

# Ajouter une bannière pour la page d'accueil
banner = pygame.image.load("banner.jpg")
banner = pygame.transform.scale(banner, (1200, 800))

#Ajouter les boutons
bouton_play = pygame.image.load("button.png")
bouton_play = pygame.transform.scale(bouton_play, (350, 150))
bouton_play_rect = bouton_play.get_rect()


bouton_quit = pygame.image.load("quit.png")
bouton_quit = pygame.transform.scale(bouton_quit, (350, 150))
bouton_quit_rect = bouton_quit.get_rect()


bouton_perso = pygame.image.load("bouton_perso.png")
bouton_perso = pygame.transform.scale(bouton_perso, (400, 120))
bouton_perso_rect = bouton_perso.get_rect()

bouton_manuel = pygame.image.load("perso_manuel.png")
bouton_manuel = pygame.transform.scale(bouton_manuel, (400, 120))
bouton_manuel_rect = bouton_manuel.get_rect()


#Definir la police d'écriture
police = pygame.font.Font("harryfont.ttf", 70)


# Laisser la fenêtre ouverte
running = True 
while running:
    if game.jeu_lancé:
        screen.blit(background, (0, -100))
        screen.blit(bouton_quit, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if bouton_quit_rect.collidepoint(mouse[0], mouse[1]):
                    game.jeu_lancé = False
        screen.blit(bouton_perso, (400, 150)) 
        screen.blit(bouton_manuel, (400, 500))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if bouton_perso_rect.collidepoint(mouse[0], mouse[1]):
                    print("A FINIR VENDREDI 11")


    else:
        screen.blit(banner, (0, -100))
        screen.blit(bouton_play, (0, 0))

       
    # Mettre a jour la fenêtre
    pygame.display.flip()


    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            # Jeu fermé
            print("Vous avez fermé le jeu")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if bouton_play_rect.collidepoint(mouse[0], mouse[1]):
                game.jeu_lancé = True
                
   
          
              
    



