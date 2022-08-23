import random
import pygame
from others import checkCollisions


class Coin:
    def __init__(self):
        self.collectcoin=pygame.mixer.Sound("data/sfx/coin_pickup.wav")
        self.sprite=pygame.image.load('data/sprites/coin.png')
        self.position = pygame.Vector2()
        self.position.xy = 0,0
        self.coinnumber=0
        self.cos1=False
        self.coinnumber=random.randint(2,6)
        

    def coin_new_pos(self,DISPLAY):
        self.position.xy=random.randint(0,DISPLAY.get_width()),random.randint(0,DISPLAY.get_height())
        return self.position



    def coin_spawn(self,DISPLAY,player):
        if player.points == self.coinnumber:
            self.coinnumber+= random.randint(2,6)
            if not self.cos1:    
                self.position=self.coin_new_pos(DISPLAY)
                self.cos1=True
                    
    def coin_visible(self,DISPLAY):
            DISPLAY.blit(self.sprite,self.position)


    def coin_collect(self,player,DISPLAY):
            if checkCollisions((player.position.x+2), (player.position.y+3), (player.sprite.get_width()/8*7), (player.sprite.get_height()/16*13),self.position.x,self.position.y,self.sprite.get_width(),self.sprite.get_height()):
                player.coinPoints+=1
                self.coinnumber+=random.randint(1,3)
                self.position=self.coin_new_pos(DISPLAY)
                self.cos1=False
                self.collectcoin.play()
                



    def coin_work(self,DISPLAY,player):
        self.coin_spawn(DISPLAY,player)
        if self.cos1:
            self.coin_visible(DISPLAY)
            self.coin_collect(player,DISPLAY)

    