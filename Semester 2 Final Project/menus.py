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

                elif (386 + 259 > mouse[0] > 386) and (412 + 56 > mouse[1] > 412):

                    loop = False
                    interpolation_UI(win)

                elif (75 + 259 > mouse[0] > 75) and (488 + 56 > mouse[1] > 488):

                    loop = False
                    numericalDifferentiationUI(win)

                elif (699 + 259 > mouse[0]> 699) and (337 + 56 > mouse[1] > 337):

                    loop = False
                    optimizationUI(win)

                    
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

    font = pygame.font.SysFont("Arial",20)

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

                elif (10 + 28 > mouse[0] > 10) and (7 + 35 > mouse[1] > 7):
                    loop = False
                    rootFinding_UI(win)

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


def interpolation_UI(win):

    bg = pygame.image.load("Background_PNG/InterpolationUI2.png")

    loop = True

    font = pygame.font.SysFont("Arial",20)

    visctext = ""
    resulttext = ""
    viscInputExist = False
    currInputing = "none"

    x_sample = [0,5,10,15]
    y_sample = [1.792,1.519,1.308,1.140]

    while loop:

        events = pygame.event.get()

        for event in events:

            if (event.type == pygame.QUIT):

                pygame.quit()
                exit()

            elif (event.type == pygame.MOUSEBUTTONDOWN):

                mouse = pygame.mouse.get_pos()
                
                
                if (10 + 28 > mouse[0] > 10 ) and  (7 + 35 > mouse[1] > 7):
                    loop = False
                    main_menu(win)

                elif (236 + 390 > mouse[0] > 236) and (262 + 40 > mouse[1] > 262):


                    if (viscInputExist):
                        visctext = viscInput.get_text()
                        viscInputExist = False
                        currInputing = "none"

                    viscInputExist = True
                    viscInput = pygame_textinput.TextInput(visctext,"Arial",20)
                    visctext = ""
                    currInputing = "visc"

                elif (235 + 259 > mouse[0] > 235) and (404 + 56 > mouse[1] > 404):

                    if (viscInputExist):
                        visctext = viscInput.get_text()
                        viscInputExist = False
                        currInputing = "none"
                    
                    val = int (visctext)

                    result = calc.mylagrange(x_sample,y_sample,val)

                    resulttext = str(round(result,3))



                else:

                    if (viscInputExist):
                        visctext = viscInput.get_text()
                        viscInputExist = False
                        currInputing = "none"
           
            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):

                    if (currInputing == "visc"):

                        visctext = viscInput.get_text()
                        viscInputExist = False
                        currInputing = "none"

        win.blit(bg,(0,0))
        
        if (viscInputExist):
            viscInput.update(events)
            win.blit(viscInput.get_surface(),(258,280))

        renvisctext = font.render(visctext,False,(0,0,0))
        renrestext =  font.render(resulttext,False,(0,0,0))

        win.blit(renvisctext,(258,280))
        win.blit(renrestext,(250,365))


        pygame.display.update()


def numericalDifferentiationUI(win):

    bg = pygame.image.load("Background_PNG/NumericalDifferentiationUI2.png")

    loop = True
    funcInputExist = False
    levelInputExist = False
    newimg = False

    currInputing = "none"
    clock = pygame.time.Clock()
    
    functext = "x**2 - 2"
    leveltext = "2"
    resulttext = ""

    font = pygame.font.SysFont("Arial",20)

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

                    elif (levelInputExist):

                        leveltext = levelInput.get_text()
                        levelInputExist = False
                        currInputing = "none"

                    functionInput = pygame_textinput.TextInput(functext,"Arial",20)
                    functext = ""
                    funcInputExist = True
                    currInputing = "function"

                elif (10 + 28 > mouse[0] > 10) and (7 + 35 > mouse[1] > 7):
                    
                    loop = False
                    main_menu(win)

                elif  (458 + 176 > mouse[0] > 458) and (276 + 40 > mouse[1] > 276):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (levelInputExist):

                        leveltext = levelInput.get_text()
                        levelInputExist = False
                        currInputing = "none"

                    levelInput = pygame_textinput.TextInput(leveltext,"Arial",20)
                    leveltext = ""
                    levelInputExist = True
                    currInputing = "level"


                elif (46 + 259 > mouse[0] > 46) and (418 + 56 > mouse[1] > 418):

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (levelInputExist):

                        leveltext = levelInput.get_text()
                        levelInputExist = False
                        currInputing = "none"

                    f = lambda x : eval(functext)
                    level = int(leveltext)
                    calc.centralNumDifferentiation(f,level)
                    newImg = pygame.image.load("result.png")
                    newimg = True
                    
                    


                else:

                    if (funcInputExist):
                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (levelInputExist):

                        leveltext = levelInput.get_text()
                        levelInputExist = False
                        currInputing = "none"


            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):

                    if (currInputing == "function"):

                        functext = functionInput.get_text()
                        funcInputExist = False
                        currInputing = "none"

                    elif (currInputing == "level"):

                        leveltext = levelInput.get_text()
                        upInputExist = False
                        currInputing = "none"


        win.blit(bg,(0,0))
        
        if (funcInputExist):    
            functionInput.update(events)
            win.blit(functionInput.get_surface(),(70,290))

        elif (levelInputExist):
            levelInput.update(events)
            win.blit(levelInput.get_surface(),(480,290))
            

        renfunctext = font.render(functext, False,(0,0,0))
        renuptext = font.render(leveltext, False,(0,0,0))
        renrestext = font.render(str(resulttext), False, (0,0,0))

        win.blit(renfunctext,(70,290))
        win.blit(renuptext,(480,290))
        win.blit(renrestext,(60,365))
        
        if (newimg):
            newImg = pygame.transform.scale(newImg,(288,192))
            win.blit(newImg,(700,220))

        pygame.display.update()


    

def optimizationUI(win):

    bg = pygame.image.load("Background_PNG/Optimization2.png")

    loop = True

    font = pygame.font.SysFont("Arial",20)

    x0text = ""
    resulttext = ""
    x0InputExist = False
    currInputing = "none"

    while loop:

        events = pygame.event.get()

        for event in events:

            if (event.type == pygame.QUIT):

                pygame.quit()
                exit()

            elif (event.type == pygame.MOUSEBUTTONDOWN):

                mouse = pygame.mouse.get_pos()
                
                
                if (10 + 28 > mouse[0] > 10 ) and  (7 + 35 > mouse[1] > 7):
                    loop = False
                    main_menu(win)

                elif (23 + 390 > mouse[0] > 23) and (262 + 40 > mouse[1] > 262):


                    if (x0InputExist):
                        x0text = x0Input.get_text()
                        x0InputExist = False
                        currInputing = "none"

                    x0InputExist = True
                    x0Input = pygame_textinput.TextInput(x0text,"Arial",20)
                    x0text = ""
                    currInputing = "x0"

                elif (235 + 259 > mouse[0] > 235) and (404 + 56 > mouse[1] > 404):

                    if (x0InputExist):
                        visctext = viscInput.get_text()
                        viscInputExist = False
                        currInputing = "none"
                    
                    val = int (visctext)

                    result = calc.mylagrange(x_sample,y_sample,val)

                    resulttext = str(round(result,3))

                else:

                    if (x0InputExist):
                        x0text = x0Input.get_text()
                        x0InputExist = False
                        currInputing = "none"
           
            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):

                    if (currInputing == "x0"):

                        x0text = x0Input.get_text()
                        x0InputExist = False
                        currInputing = "none"

        win.blit(bg,(0,0))
        
        if (x0InputExist):
            x0Input.update(events)
            win.blit(x0Input.get_surface(),(40,280))

        renvisctext = font.render(x0text,False,(0,0,0))
        renrestext =  font.render(resulttext,False,(0,0,0))

        win.blit(renvisctext,(40,280))
        win.blit(renrestext,(250,365))


        pygame.display.update()