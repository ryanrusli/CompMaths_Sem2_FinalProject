import pygame
import menus as m

#initialises pygame
pygame.init()

win = pygame.display.set_mode((1280,720))

loop = True

baseColor = "orange"
while loop:

    m.main_menu(win)
    
    



