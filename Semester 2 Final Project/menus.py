import pygame
import pygame_textinput
import formulas as calc

def main_menu(win):

    bg = pygame.image.load("Background_PNG/main_menu2.png")
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):

            	mouse = pygame.mouse.get_pos()

            	if (259 + 79 > mouse[0] > 79) and (365 + 44 > mouse[1] > 365):
            		loop = False
            		rootFinding_UI(win)



                	
        win.blit(bg,(0,0))

        pygame.display.update()



def rootFinding_UI(win):

	bg = pygame.image.load("Background_PNG/rootFindingUI_menu2.png")

	loop = True

	while loop:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()

			elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):

				mouse = pygame.mouse.get_pos()

				if (95 + 206 > mouse[0] > 95 ) and (412 + 44 > mouse[1] > 412):
					loop = False
					bisectionMethod_UI(win)

				elif (712 + 817 > mouse[0] > 712) and (404 + 44 > mouse[1] > 404):
					loop = False
					newtonRaphson_UI(win)

		win.blit(bg,(0,0))
		pygame.display.update()


def bisectionMethod_UI(win):

	bg = pygame.image.load("Background_PNG/bisectionUI_menu2.png")

	loop = True
	funcInputExist = False
	upInputExist = False
	lowInputExist = False

	currInputing = "none"
	clock = pygame.time.Clock()
	
	functext = ""
	uppertext = ""
	lowertext = ""
	resulttext = ""

	font = pygame.font.SysFont("Arial",25)

	while loop:
		clock.tick(120)

		events = pygame.event.get()
		for event in events:

			if (event.type  == pygame.QUIT):
				pygame.quit()
				exit()

			elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):

				mouse = pygame.mouse.get_pos()

				if (173 + 47 > mouse[0] > 173) and (276 + 40 > mouse[1] > 276):

					functionInput = pygame_textinput.TextInput(functext,"Arial",20)
					functext = ""
					funcInputExist = True
					currInputing = "function"

				elif  (618 + 546 > mouse[0] > 618) and (296 + 40 > mouse[1] > 296):

					upperInput = pygame_textinput.TextInput(uppertext,"Arial",20)
					uppertext = ""
					upInputExist = True
					currInputing = "upper"

				elif (882 + 850> mouse[0] > 882) and (296 + 40 > mouse[1] > 296):

					lowerInput = pygame_textinput.TextInput(lowertext,"Arial",20)
					lowertext = ""
					lowInputExist = True
					currInputing = "lower"

				elif (791 + 135 > mouse[0] > 791) and (382 + 48 > mouse[1] > 382):

					f = lambda x : eval(functext)
					xu = int(uppertext)
					xl = int(lowertext)

					resultext = str(calc.bisection(f,xu,xl,1.0E-6))





			elif (event.type == pygame.KEYDOWN):

				if (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):

					if (currInputing == "function"):

						functext = functionInput.get_text()
						funcInputExist = False
						currInputing = "none"

					elif (currInputing == "upper"):

						uppertext = upperInput.get_text()
						upInputExist = False
						currInputing = "none"

					elif (currInputing == "lower"):

						lowertext = lowerInput.get_text()
						lowInputExist = False
						currInputing = "none"


		win.blit(bg,(0,0))
		if (funcInputExist):	
			functionInput.update(events)
			win.blit(functionInput.get_surface(),(210,405))

		elif (upInputExist):
			upperInput.update(events)
			win.blit(upperInput.get_surface(),(660,405))

		elif (lowInputExist):
			lowerInput.update(events)
			win.blit(lowerInput.get_surface(),(920,405))


		renfunctext = font.render(functext, False,(0,0,0))
		renuptext = font.render(uppertext, False,(0,0,0))
		renlowctext = font.render(lowertext, False,(0,0,0))
		renrestext = font.render(resulttext, False, (0,0,0))

		win.blit(renfunctext,(210,405))
		win.blit(renuptext,(660,405))
		win.blit(renlowctext,(920,405))
		win.blit(renrestext,(310,635))

		pygame.display.update()



def newtonRaphson_UI(win):

	pass
