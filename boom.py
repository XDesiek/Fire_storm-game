from turtle import position
import pygame
from spritesheet import Spritesheet


class Boom:
    def __init__(self):

        boomSpriteSheeet=Spritesheet("data/sprites/explosion_spritesheet.png")


        img1=boomSpriteSheeet.get_sprite(0,0,360,360)
        img2=boomSpriteSheeet.get_sprite(360,0,360,360)
        img3=boomSpriteSheeet.get_sprite(720,0,360,360)
        img4=boomSpriteSheeet.get_sprite(1080,0,360,360)
        img5=boomSpriteSheeet.get_sprite(1440,0,360,360)
        img6=boomSpriteSheeet.get_sprite(0,360,360,360)
        img7=boomSpriteSheeet.get_sprite(360,360,360,360)
        self.boomlist=[img1,img2,img3,img4,img5,img6,img7]
    def render_gif(self,DISPLAY,position):
        xpos,ypos=position
        xpos-=180
        ypos-=180
        position=xpos,ypos            
        for img in self.boomlist:
            DISPLAY.blit(img,position)
            pygame.display.update()
            pygame.time.delay(60)