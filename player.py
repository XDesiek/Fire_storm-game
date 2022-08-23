import pygame



class Player:
    def __init__(self):
        self.position = pygame.Vector2()
        self.position.xy = 0, 0
        self.velocity = pygame.Vector2()
        self.velocity = 3
        self.acceleration = 0.1
        self.sprite = pygame.image.load('data/sprites/vortex_ball.png')
        self.coinPoints=0
        self.points=0
        self.pointMultipier=1
        
        self.dash=False
        self.dead=False
        
        
        self.dashtime=0


        self.xvalue = self.position.x+2 
        self.yvalue = self.position.y+3 
        self.width = self.sprite.get_width()/8*7
        self.height = self.sprite.get_height()/16*13




    def dashy(self):
        if self.dash:
            self.velocity=15
            self.dashtime+=1
            if self.dashtime==10:
                self.velocity=3
                self.dashtime=0
                self.dash=False   