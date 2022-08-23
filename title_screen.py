import pygame,time,sys
from pygame.locals import *
from bullet import Bullet
from button import Button
from others import checkCollisions

class TitleScreen:
    def __init__(self):
        self.bg = pygame.image.load('data/sprites/bg.png').convert()
        self.cool_font= pygame.font.Font('data/fonts/better_font.ttf', 150)  
        self.font_small = pygame.font.Font('data/fonts/font.otf', 32)
        self.title_screen_open=True

    def title_screen(self,DISPLAY,last_time):
        pygame.display.set_caption('Fire Storm')
        pygame.display.set_icon(Bullet().sprite)
        # czas and background
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()


        startButton=Button()
        DISPLAY.blit(self.bg, (0,0)) 
        startButton.position.xy=DISPLAY.get_width()/2-80,DISPLAY.get_height()/2
        DISPLAY.blit(startButton.currentsprite,(startButton.position))
        startMessage = self.font_small.render("START", False, (0, 0, 0))
        DISPLAY.blit(startMessage, (startButton.position.x+18,startButton.position.y+20))
        gamenametext = self.cool_font.render("Fire Storm", False, (95, 96, 99))
        DISPLAY.blit(gamenametext,(190,130))   


        # get the position of the mouse
        mouseX,mouseY = pygame.mouse.get_pos() 
        
        # checking events
        for event in pygame.event.get():

            
            # if the player quits
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_SPACE:startButton.clicked=True
            if event.type == pygame.MOUSEBUTTONDOWN and checkCollisions(mouseX, mouseY, 3, 3, startButton.position.x ,startButton.position.y ,startButton.currentsprite.get_width(), startButton.currentsprite.get_width()): startButton.clicked = True 
            


        # wlaczanie gry przez start button
        if startButton.clicked :
            startButton.currentsprite=startButton.pressedsprite
            DISPLAY.blit(startButton.currentsprite,(startButton.position))
            DISPLAY.blit(startMessage, (startButton.position.x+18,startButton.position.y+20))
            pygame.display.update()
            self.title_screen_open=False
            pygame.time.delay(250)
    
        pygame.display.update()
        pygame.time.delay(10)