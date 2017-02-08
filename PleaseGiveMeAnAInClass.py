import pygame, sys, os, time, math, re
from pygame.locals import *
from sys import exit
pygame.init()

sys.setrecursionlimit(10000)

#screen and background objects
screen=pygame.display.set_mode((800,480),0,32)
screen_rect = screen.get_rect()
back = pygame.Surface((800,480))
background = back.convert()
pygame.display.set_caption("Assignment #3")

#font objects if needed for later implementation
#smallText = pygame.font.Font("font/gameplay.ttf", 25)

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
fileArray = []

#loop objects
running = True
intro = True
results = True
instruct = True

#re needs to be fixed
def FileIO(fileName):
    file = open(fileName)
    contents = file.readlines()
    file.close()
    for content in contents:
        binary = re.search('\d+', content)
        fileArray.append(binary.group(0))

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
    results = False
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
    results = False
    instruct = True
    background = rulesBG
    button1 = Button(mainButton, lightMainButton, 50, 400, ProgramIntro)
    button2 = Button(exitButton, lightExitButton, 650, 400, Exit)
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
    global running, intro, results, instruct
    white = pygame.Color(255, 255, 255, 255)
    running = True
    intro = False
    results = False
    instruct = False
    gameOver = False
    blue = (0,0,255) # color of the wave
    canvas_width = 800
    canvas_height = 480
    centerY = int(canvas_height/2)
    FPS = 160
    amplitude = 80 # how many pixels tall the waves with rise/fall.
    clock = pygame.time.Clock()
    xPos = 0
    posRecord = {'square': []} # keeps track of the positions for drawing the waves
    yPosSquare = amplitude # starting position
    button1 = Button(mainButton, lightMainButton, 50, 400, ProgramIntro)
    button2 = Button(rulesButton, lightRulesButton, 350, 400, Instructions)
    button3 = Button(exitButton, lightExitButton, 650, 400, Exit)
    allSprites = pygame.sprite.Group()
    allSprites.add(button1, button2, button3)

    #program loop
    while running:
        Quit()
        
        #display of frames
        clock.tick(FPS)
        text = "FPS: {0:.2f}".format(clock.get_fps())
        pygame.display.set_caption(text)

        screen.fill(white)
        
        button1.update()
        button2.update()
        button3.update()
        allSprites.draw(screen)

        #the thickness of the line
        posRecord['square'].append((int(xPos), int(yPosSquare) + (centerY-100)))
        for x, y in posRecord['square']:
            pygame.draw.circle(screen, blue, (x, y), 2)
            
        #speed of the line
        xPos += 1

        #if the line reaches the end of the screen, it restarts
        #else it creates the movement of the line
        if xPos > canvas_width:
            xPos = 0
            yPosSquare = amplitude
            posRecord['square'] = []
        else:
            #jumps occur every 20 pixels/ this is the base case
            if xPos % 20 == 0:
                yPosSquare *= -1
                # add vertical line
                for x in range(-amplitude, amplitude):
                    posRecord['square'].append((int(xPos), int(x) + (centerY-100)))

        pygame.display.update()

    
def main():

    ProgramIntro()

if __name__ == '__main__': main()
