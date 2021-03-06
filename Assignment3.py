import pygame, sys, os, time, math, re, pygame_textinput
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

sys.setrecursionlimit(10000)

#screen and background objects
screen=pygame.display.set_mode((800,480),0,32)
screen_rect = screen.get_rect()
back = pygame.Surface((800,480))
background = back.convert()
pygame.display.set_caption("Assignment #3")

#font objects
smallText = pygame.font.Font("font/gameplay.ttf", 12)

#program mechanics
introBG = pygame.image.load("img/introBG.png")
rulesBG = pygame.image.load("img/rulesBG.png")
mainButton = pygame.image.load("img/mainButton.png")
lightMainButton = pygame.image.load("img/lightMainButton.png")
startButton = pygame.image.load("img/startButton.png")
lightStartButton = pygame.image.load("img/lightStartButton.png")
rulesButton = pygame.image.load("img/rulesButton.png")
lightRulesButton = pygame.image.load("img/lightRulesButton.png")
exitButton = pygame.image.load("img/exitButton.png")
lightExitButton = pygame.image.load("img/lightExitButton.png")
nrzlButton = pygame.image.load("img/nrzlButton.png")
lightNrzlButton = pygame.image.load("img/lightNrzlButton.png")
nrziButton = pygame.image.load("img/nrziButton.png")
lightNrziButton = pygame.image.load("img/lightNrziButton.png")
bamiButton = pygame.image.load("img/bamiButton.png")
lightBamiButton = pygame.image.load("img/lightBamiButton.png")
pdtyButton = pygame.image.load("img/pdtyButton.png")
lightPdtyButton = pygame.image.load("img/lightPdtyButton.png")
mchrButton = pygame.image.load("img/mchrButton.png")
lightMchrButton = pygame.image.load("img/lightMchrButton.png")
dmhrButton = pygame.image.load("img/dmhrButton.png")
lightDmhrButton = pygame.image.load("img/lightDmhrButton.png")
b8zsButton = pygame.image.load("img/b8zsButton.png")
lightB8zsButton = pygame.image.load("img/lightB8zsButton.png")
hdb3Button = pygame.image.load("img/hdb3Button.png")
lightHdb3Button = pygame.image.load("img/lightHdb3Button.png")
enterButton = pygame.image.load("img/enterButton.png")
lightEnterButton = pygame.image.load("img/lightEnterButton.png")
fileButton = pygame.image.load("img/fileButton.png")
lightFileButton = pygame.image.load("img/lightFileButton.png")


txtbx = "01001100011"
txtbx2 = ""
asciiArray = []
fileArray = []

#line objects
xPos = 0
amplitude = 100 # how many pixels tall the waves with rise/fall.
yPosSquare = amplitude # starting position
random = randint(0,2)

#loop objects
running = True
intro = True
results = True
instruct = True

def Change():
    global txtbx, txtbx2
    txtbx = str(txtbx2.get_text())

def Change2():
    global txtbx, fileArray
    txtbx = ''.join(fileArray)
    

def FileIO():
    global fileArray
    file = open("file.txt")
    contents = file.readlines()
    file.close()
    for content in contents:
        binary = re.search('\d+', content)
        fileArray.append(binary.group(0))
    Change2()

    

#Class for the button
class Button(pygame.sprite.Sprite):
    """moves a sprite on the screen, following the mouse"""
    def __init__(self, inactive, active, x, y, action=None):
        pygame.sprite.Sprite.__init__(self)
        self.inactive = inactive
        self.active = active
        self.image = inactive
        self.width = self.inactive.get_width()
        self.height = self.inactive.get_height()
        self.action = action
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        "move the player based on the mouse position"
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.x+self.width > self.mouse[0] > self.x and self.y+self.height > self.mouse[1] > self.y:
            self.image = self.active
            self.rect = (self.x, self.y, self.image.get_width(), self.image.get_height())
            if self.click[0] == 1 and self.action != None:
                self.action()    
        else:
            self.image = self.inactive
            self.rect = (self.x, self.y, self.image.get_width(), self.image.get_height())

#Quit and Exit are used for quiting the game
def Quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
def Exit():
    pygame.quit()
    sys.exit()

#code for the wave output. I used random numbers to test it but I could not
#completely implement it in time due to personal time restraints.
def randomWaves(canvas_width, canvas_height, centerY, blue, posRecord):
    global xPos, amplitude, yPosSquare, random

    #the thickness of the line
    for x, y in posRecord['square']:
        pygame.draw.circle(screen, blue, (x, y), 2)

    posRecord['square'].append((int(xPos), int((yPosSquare*(1/4))*4) + (centerY)))
            
    #speed of the line
    xPos += 1

    #if the line reaches the end of the screen, it restarts
    #else it creates the movement of the line
    if xPos > canvas_width:
        xPos = 0
        yPosSquare = amplitude
        posRecord['square'] = []
    else:
        #jumps occur every 20 pixels/this is the base case
        if xPos % 20 == 0:
            yPosSquare *= -1
            # add vertical line
            for x in range(-amplitude, amplitude):
                posRecord['square'].append((int(xPos), int((x*(1/4))*4) + (centerY)))


def NRZL():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)

    for i, j in enumerate(txtarr):
        if j == "0":
            asciiArray[i] = "+"
        elif j == "1":
            asciiArray[i] = "-"
        else:
            asciiArray[i] = "x"

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Nonreturn to Zero-Level (NRZ-L)', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("NRZL: " + ' | '.join(asciiArray))

    
                
def NRZI():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "0":
                if txtarr[x-1] == "1" and txtarr[x-2] == "1" and asciiArray[x-1] == "+":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "1" and asciiArray[x-1] == "-":
                    asciiArray[x] = "-"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "0" and asciiArray[x-1] == "+":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "0" and asciiArray[x-1] == "-":
                    asciiArray[x] = "-"
                elif txtarr[x-1] == "0" and asciiArray[x-1] == "+":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "0" and asciiArray[x-1] == "-":
                    asciiArray[x] = "-"
                else:
                    asciiArray[x] = "x"
            elif txtarr[x] == "1":
                if txtarr[x-1] == "1" and txtarr[x-2] == "1" and asciiArray[x-1] == "+":
                    asciiArray[x] = "-"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "1" and asciiArray[x-1] == "-":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "0" and asciiArray[x-1] == "+":
                    asciiArray[x] = "-"
                elif txtarr[x-1] == "1" and txtarr[x-2] == "0" and asciiArray[x-1] == "-":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "0" and asciiArray[x-1] == "-":
                    asciiArray[x] = "+"
                elif txtarr[x-1] == "0" and asciiArray[x-1] == "+":
                    asciiArray[x] = "-"
                else:
                    asciiArray[x] = "x"                   
            else:
                asciiArray[x] = "x"
        else:
            if txtarr[x] == "0":
                asciiArray[x] = "+"
            elif txtarr[x] == "1":
                asciiArray[x] = "-"
            else:
                asciiArray[x] = "x"

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Nonreturn to Zero Inverted (NRZI)', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("NRZI: " + ' | '.join(asciiArray))


def BAMI():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)
    last = -1

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
            elif txtarr[x] == "1" and last == -1:
                asciiArray[x] = "+"
                last = x
            elif txtarr[x] == "1" and last > -1:
                if asciiArray[last] == "+":
                    asciiArray[x] = "-"
                elif asciiArray[last] == "-":
                    asciiArray[x] = "+"
                else:
                    asciiArray[x] = "x"
                last = x
            else:
                asciiArray[x] = "x"
        else:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
            elif txtarr[x] == "1":
                asciiArray[x] = "+"
                last = x
            else:
                asciiArray[x] = "x"

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Bipolar-AMI', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("Bipolar-AMI: " + ' | '.join(asciiArray))
    
def PDTY():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)
    last = -1

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "1":
                asciiArray[x] = "_"
            elif txtarr[x] == "0" and last == -1:
                asciiArray[x] = "+"
                last = x
            elif txtarr[x] == "0" and last > -1:
                if asciiArray[last] == "+":
                    asciiArray[x] = "-"
                elif asciiArray[last] == "-":
                    asciiArray[x] = "+"
                else:
                    asciiArray[x] = "x"
                last = x
            else:
                asciiArray[x] = "x"
        else:
            if txtarr[x] == "1":
                asciiArray[x] = "_"
            elif txtarr[x] == "0":
                asciiArray[x] = "+"
                last = x
            else:
                asciiArray[x] = "x"

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Pseudoternary', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("Pseudoternary: " + ' | '.join(asciiArray))
    
def MCHR():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if txtarr[x] == "0":
            asciiArray[x] = "+ -"
        elif txtarr[x] == "1":
            asciiArray[x] = "- +"
        else:
            asciiArray[x] = "x"

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Manchester', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("Manchester: " + ' | '.join(asciiArray))
    
def DMHR():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)
    last = -1

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "0" and asciiArray[x-1] == "+ - +":
                asciiArray[x] = "- +"
            elif txtarr[x] == "1" and asciiArray[x-1] == "+ - +":
                asciiArray[x] = "+ -"
            elif txtarr[x] == "0" and asciiArray[x-1] == "- +":
                asciiArray[x] = "- +"
            elif txtarr[x] == "0" and asciiArray[x-1] == "+ -":
                asciiArray[x] = "+ -"
            elif txtarr[x] == "1" and asciiArray[x-1] == "- +" and last == -1:
                asciiArray[x] = "+ -"
                last = x
            elif txtarr[x] == "1" and asciiArray[x-1] == "+ -" and last == -1:
                asciiArray[x] = "- +"
                last = x
            elif txtarr[x] == "1" and asciiArray[x-1] == "- +" and last > -1:
                asciiArray[x] = "+ -"
                last = x
            elif txtarr[x] == "1" and asciiArray[x-1] == "+ -" and last > -1:
                asciiArray[x] = "- +"
                last = x
            else:
                asciiArray[x] = "x"
        elif x == 0:
            if txtarr[x] == "0" or txtarr[x] == "1":
                asciiArray[x] = "+ - +"
            else:
                asciiArray[x] = "x"
            
        else:
            asciiArray[x] = "x"



    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('Differential Manchester', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("Differential Manchester: " + ' | '.join(asciiArray))
    
def B8ZS():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)
    start = 0
    last = -1

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
                start = start + 1
            elif txtarr[x] == "1" and last == -1:
                asciiArray[x] = "+"
                last = x
                start = 0
            elif txtarr[x] == "1" and last > -1:
                if asciiArray[last] == "+":
                    asciiArray[x] = "-"
                    start = 0
                elif asciiArray[last] == "-":
                    asciiArray[x] = "+"
                    start = 0
                else:
                    asciiArray[x] = "x"
                    start = 0
                last = x
            else:
                asciiArray[x] = "x"
                start = 0
        else:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
                start = start + 1
            elif txtarr[x] == "1":
                asciiArray[x] = "+"
                last = x
                start = 0
            else:
                asciiArray[x] = "x"
                start = 0

        if start == 8:
            if asciiArray[x-8] == "+":
                asciiArray[x-4] = "+"
                asciiArray[x-3] = "-"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "-"
                asciiArray[x] = "+"
            else:
                asciiArray[x-4] = "-"
                asciiArray[x-3] = "+"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "+"
                asciiArray[x] = "-"
            start = 0
        

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('B8ZS', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("B8ZS: " + ' | '.join(asciiArray))
    
def HDB3():
    global txtbx, asciiArray
    txtarr = list(txtbx)
    asciiArray = list(txtbx)
    start = 0
    substitution = 0
    last = -1

    for x, (i, j) in enumerate(zip(txtarr, asciiArray)):
        if x > 0:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
                start = start + 1
            elif txtarr[x] == "1" and last == -1:
                asciiArray[x] = "+"
                last = x
                start = 0
            elif txtarr[x] == "1" and last > -1:
                if asciiArray[last] == "+":
                    asciiArray[x] = "-"
                    start = 0
                elif asciiArray[last] == "-":
                    asciiArray[x] = "+"
                    start = 0
                else:
                    asciiArray[x] = "x"
                    start = 0
                last = x
            else:
                asciiArray[x] = "x"
                start = 0
        else:
            if txtarr[x] == "0":
                asciiArray[x] = "_"
                start = start + 1
            elif txtarr[x] == "1":
                asciiArray[x] = "+"
                last = x
                start = 0
            else:
                asciiArray[x] = "x"
                start = 0

        if start == 4:
            if asciiArray[x-8] == "+" and substitution % 2 == 0:
                asciiArray[x-3] = "-"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "_"
                asciiArray[x] = "-"
                substitution = substitution + 1
            elif asciiArray[x-8] == "-" and substitution % 2 == 0:
                asciiArray[x-3] = "+"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "_"
                asciiArray[x] = "+"
                substitution = substitution + 1
            elif asciiArray[x-8] == "+" and substitution % 2 != 0:
                asciiArray[x-3] = "_"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "_"
                asciiArray[x] = "+"
                substitution = substitution + 1
            else:
                asciiArray[x-3] = "_"
                asciiArray[x-2] = "_"
                asciiArray[x-1] = "_"
                asciiArray[x] = "-"
                substitution = substitution + 1
            start = 0

    txtSurf, txtRect = text_objects(' | '.join(asciiArray), smallText, (0,0,255))
    txtRect.center = ((400),(400))
    screen.blit(txtSurf, txtRect)

    nameSurf, nameRect = text_objects('HDB3', smallText, (0,0,255))
    nameRect.center = ((400),(380))
    screen.blit(nameSurf, nameRect)

    print("HBD3: " + ' | '.join(asciiArray))
    
#Used for displaying text on screen
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Screen user is greeted with
def ProgramIntro():
    global running, intro, results, instruct, introBG
    pygame.display.set_caption("Assignment #3")
    running = False
    intro = True
    instruct = False
    background = introBG
    button1 = Button(startButton, lightStartButton, 50, 300, ProgramLoop)
    button2 = Button(rulesButton, lightRulesButton, 350, 300, Instructions)
    button3 = Button(exitButton, lightExitButton, 650, 300, Exit)
    allSprites = pygame.sprite.Group()
    allSprites.add(button1, button2, button3)

    while intro:
        Quit()
                
        screen.blit(background, (0, 0))

        button1.update()
        button2.update()
        button3.update()
        allSprites.draw(screen)

        pygame.display.update()

#Instructions on how to use the program
def Instructions():
    global running, intro, results, instruct, rulesBG
    pygame.display.set_caption("Assignment #3")
    running = False
    intro = False
    instruct = True
    background = rulesBG
    button1 = Button(mainButton, lightMainButton, 50, 425, ProgramIntro)
    button2 = Button(exitButton, lightExitButton, 650, 425, Exit)
    allSprites = pygame.sprite.Group()
    allSprites.add(button1, button2)
    while instruct:
        Quit()
                
        screen.blit(background, (0, 0))
        
        button1.update()
        button2.update()
        allSprites.draw(screen)

        pygame.display.update()

#loop that runs the the program
def ProgramLoop():
    global running, intro, results, instruct, xPos, txtbx, txtbx2
    white = pygame.Color(255, 255, 255, 255)
    txtbx = "01001100011"
    running = True
    intro = False
    results = False
    instruct = False
    gameOver = False
    clock = pygame.time.Clock()
    canvas_width = 800
    canvas_height = 480
    centerY = int(canvas_height/2)
    blue = (0,0,255) # color of the wave
    xPos = 0
    posRecord = {'square': []}
    button1 = Button(mainButton, lightMainButton, 400, 425, ProgramIntro)
    button2 = Button(rulesButton, lightRulesButton, 525, 425, Instructions)
    button3 = Button(exitButton, lightExitButton, 650, 425, Exit)

    button4 = Button(nrzlButton, lightNrzlButton, 0, 10, NRZL)
    button5 = Button(nrziButton, lightNrziButton, 100, 10, NRZI)
    button6 = Button(bamiButton, lightBamiButton, 200, 10, BAMI)
    button7 = Button(pdtyButton, lightPdtyButton, 300, 10, PDTY)
    button8 = Button(mchrButton, lightMchrButton, 400, 10, MCHR)
    button9 = Button(dmhrButton, lightDmhrButton, 500, 10, DMHR)
    button10 = Button(b8zsButton, lightB8zsButton, 600, 10, B8ZS)
    button11 = Button(hdb3Button, lightHdb3Button, 700, 10, HDB3)
    
    button12 = Button(enterButton, lightEnterButton, 600, 75, Change)
    button13 = Button(fileButton, lightFileButton, 100, 425, FileIO)


    allSprites = pygame.sprite.Group()
    allSprites.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13)

    txtbx2 = pygame_textinput.TextInput()

    #program loop
    while running:
        Quit()

        screen.fill(white)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Feed it with events every frame
        txtbx2.update(events)
        # Blit its surface onto the screen
        screen.blit(txtbx2.get_surface(), (10, 75))
        
        button1.update()
        button2.update()
        button3.update()
        button4.update()
        button5.update()
        button6.update()
        button7.update()
        button8.update()
        button9.update()
        button10.update()
        button11.update()
        button12.update()
        button13.update()
        allSprites.draw(screen)
        
        pygame.display.update()
        clock.tick(60)
        text = "FPS: {0:.2f}".format(clock.get_fps())
        pygame.display.set_caption(text)


    
def main():

    ProgramIntro()

if __name__ == '__main__': main()
