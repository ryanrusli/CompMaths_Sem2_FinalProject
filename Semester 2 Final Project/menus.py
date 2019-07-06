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

                if (73 + 259 > mouse[0] > 73) and (337 + 56 > mouse[1] > 337):
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

                if (77 + 259 > mouse[0] > 77 ) and (384 + 56 > mouse[1] > 384):
                    loop = False
                    bisectionMethod_UI(win)

                elif (688 + 259 > mouse[0] > 688) and (376 + 56 > mouse[1] > 376):
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
    
    functext = "x**2 - 2"
    uppertext = "5"
    lowertext = "0"
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



                if (47 + 372 > mouse[0] > 47) and (276 + 40 > mouse[1] > 276):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (upInputExist):

                        uppertext = upperInput.get_text()
                        upInputExist = False
                        currInputing = "none"

                    elif (lowInputExist):

                        lowertext = lowerInput.get_text()
                        lowInputExist = False
                        currInputing = "none"

                    functionInput = pygame_textinput.TextInput(functext,"Arial",20)
                    functext = ""
                    funcInputExist = True
                    currInputing = "function"

                elif  (458 + 176 > mouse[0] > 458) and (276 + 40 > mouse[1] > 276):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (upInputExist):

                        uppertext = upperInput.get_text()
                        upInputExist = False
                        currInputing = "none"

                    elif (lowInputExist):

                        lowertext = lowerInput.get_text()
                        lowInputExist = False
                        currInputing = "none"

                    upperInput = pygame_textinput.TextInput(uppertext,"Arial",20)
                    uppertext = ""
                    upInputExist = True
                    currInputing = "upper"

                elif (761 + 178 > mouse[0] > 761) and (276 + 40 > mouse[1] > 276):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (upInputExist):

                        uppertext = upperInput.get_text()
                        upInputExist = False
                        currInputing = "none"

                    elif (lowInputExist):

                        lowertext = lowerInput.get_text()
                        lowInputExist = False
                        currInputing = "none"


                    lowerInput = pygame_textinput.TextInput(lowertext,"Arial",20)
                    lowertext = ""
                    lowInputExist = True
                    currInputing = "lower"

                elif (46 + 259 > mouse[0] > 46) and (418 + 56 > mouse[1] > 418):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (upInputExist):

                        uppertext = upperInput.get_text()
                        upInputExist = False
                        currInputing = "none"

                    elif (lowInputExist):

                        lowertext = lowerInput.get_text()
                        lowInputExist = False
                        currInputing = "none"

                    f = lambda x : eval(functext)
                    xu = int(uppertext)
                    xl = int(lowertext)

                    result = calc.bisection(f,xl,xu,1.0E-6)

                    if (result == None):
                        resulttext = "Root Not Found"

                    else:

                        resulttext = round(result,4)


                else:

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (upInputExist):

                        uppertext = upperInput.get_text()
                        upInputExist = False
                        currInputing = "none"

                    elif (lowInputExist):

                        lowertext = lowerInput.get_text()
                        lowInputExist = False
                        currInputing = "none"


            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):

                    if (currInputing == "function"):

                        functext = functionInput.get_text()
                        print(functext)
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
            win.blit(functionInput.get_surface(),(70,290))

        elif (upInputExist):
            upperInput.update(events)
            win.blit(upperInput.get_surface(),(480,290))

        elif (lowInputExist):
            lowerInput.update(events)
            win.blit(lowerInput.get_surface(),(780,290))


        renfunctext = font.render(functext, False,(0,0,0))
        renuptext = font.render(uppertext, False,(0,0,0))
        renlowctext = font.render(lowertext, False,(0,0,0))
        renrestext = font.render(str(resulttext), False, (0,0,0))

        win.blit(renfunctext,(70,290))
        win.blit(renuptext,(480,290))
        win.blit(renlowctext,(780,290))
        win.blit(renrestext,(60,365))

        pygame.display.update()



def newtonRaphson_UI(win):



    pass

