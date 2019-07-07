import pygame
import menus as m

x = 100
y = 50
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


#initialises pygame
pygame.init()

win = pygame.display.set_mode((1024,600))

loop = True

while loop:
    m.main_menu(win)
    
    
