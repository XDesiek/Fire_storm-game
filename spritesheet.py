from pygame.locals import *
import pygame

class Spritesheet():
    def __init__(self, filename):
        self.filename = filename
        self.spriteheet=pygame.image.load(filename).convert()
    

    def get_sprite(self,x_position,y_position,width,height):
        sprite=pygame.Surface((width,height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.spriteheet,(0,0),(x_position,y_position,width,height))
        return sprite