import pygame, time, random

pygame.init()                                                                    #initiate all parts of pygame, must do all times first

display_width, display_height = 800, 600                                         # make the size variable for referencing ease.

black=(0,0,0)                                                                    #color definitions using rgb, arg(tuples) are r,g,b.
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
blue = (0,0,200)
bright_blue=(0,0,255)

colorBox =(black, red, blue, bright_blue, bright_green, bright_red, green)
randColor= blue
car_width=69
introPic =pygame.image.load('Images\Start screen!.png')
crashPic =pygame.image.load('Images\crash screen.png')
pause = False
gameDisplay = pygame.display.set_mode((display_width, display_height))           #window resolution, argument is a tuple
pygame.display.set_caption('PYCAR 2017')                                         #window title
clock= pygame.time.Clock()                                                       #clocking the game

carImg = pygame.image.load('Images\car.png')
caricon =pygame.image.load('Images\mini-car-icon.png')
pygame.display.set_icon(caricon)
crashSound = pygame.mixer.Sound('Sfx\crash.wav')
pygame.mixer.music.load('Sfx\Electro-Light_-_Symbolism_NCS_Release.wav')

def things_dodged(count):
    font = pygame.font.SysFont('comicsansms.ttf', 25)
    text =font.render('Score: ' + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x, y):
    gameDisplay.blit(carImg,(x,y))                                               #blits or draws the car\img to the location tuple (x,y)

def crashScreen():
    gameDisplay.blit(crashPic,(0,0))
def introScreen():
    gameDisplay.blit(introPic, (0,0))


def text_objects(text, font, color= red):
    textSurface = font.render(text, True, color)                                   # render(objectName, AntialisingStatus, Color)
    return textSurface, textSurface.get_rect()



def quitgame():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] >x and y + h > mouse[1] > y:
           pygame.draw.rect(gameDisplay, ac,(x, y, w,h))
           if click[0] == 1 and action != None:
               action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x, y, w, h))

    smallText= pygame.font.SysFont('comicsansms.ttf', 30)
    TextSurf, TextRect = text_objects(msg, smallText, white)
    TextRect.center = ((x+(w/2)), ( y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def crash():
    #crash = True
    colorBox =(black, red, blue, bright_blue, bright_green, bright_red, green)
    crashScreen()
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)
    largeText = pygame.font.SysFont('comicsansms.ttf',90)
    TextSurf, TextRect = text_objects(" ", largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()

        button('Vroom again!', 150, 450, 150, 50, green, bright_green,game_loop)

        button('Leave!!', 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():

    intro = True
    while intro:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()

        #gameDisplay.fill(white)
        introScreen()
        largeText = pygame.font.SysFont('comicsansms.ttf',90)
        TextSurf, TextRect = text_objects(" ", largeText)
        TextRect.center =((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Vroom!!', 150, 450, 100, 50, green, bright_green,game_loop)

        button('Leave!!', 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.flip()
        clock.tick(15)

#def colorRandomizer():
    #randColor = random.randrange(colorBox)


def unpause():
    global pause
    pause= False
    pygame.mixer.music.unpause()
    

def paused():
    
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont('comicsansms.ttf',90)
    TextSurf, TextRect = text_objects(" Paused ", largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()

        #gameDisplay.fill(white)


        button('Continue!', 150, 450, 150, 50, green, bright_green,unpause)

        button('Leave!!', 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    global randColor
    pygame.mixer.music.play(1)
    x=(display_width * 0.45)
    y=(display_height * 0.8)
    x_change=0

    thing_startx =random.randrange(0,display_width)
    thing_starty = -600
    thing_speed =3
    thing_width=100
    thing_height=100
    Score = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():                                         #captures human input; mouse click, keyboard clicks etc.
            if event.type == pygame.QUIT:                                        #Exit the game when press 'X'
               quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change= 10
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)                                                  #fills the display with white, use first!

        #randColor = random.randrange(colorBox)
        #index = random.randrange(0, len(colorBox))
        #randColor = colorBox[index]


        things(thing_startx,thing_starty,thing_width,thing_height, randColor)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(Score)
        #index = random.randrange(0, len(colorBox))
        #randColor = colorBox[index]

        if x > display_width - car_width or x< 0:                                # the top left part of the car is x0 y0 so use w:r: t: that
               crash()

        if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx= random.randrange(0, display_width)
                Score += 1
                thing_speed += 1
                thing_width += (Score*1.1)
                index = random.randrange(0, len(colorBox))
                randColor = colorBox[index]

        if y < thing_starty+thing_height:
            #print('y crossover')
            if x > thing_startx and x < thing_startx+ thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                #print('x crossover')
                crash()

        pygame.display.flip()                                                    #updates the argument entered
        clock.tick(60)                                                           #arg is FPS
game_intro()
game_loop()
quitgame()                                                                          #program exit
