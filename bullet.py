import pygame
import random
class Bullet: 
    def __init__(self):
        self.upSprite = pygame.image.load('data/sprites/bullet.gif')
        self.downSprite = pygame.transform.flip(self.upSprite, False, True).convert()
        self.rightSprite = pygame.transform.rotate(self.upSprite, -90).convert()
        self.leftSprite= pygame.transform.rotate(self.upSprite, +90).convert()
        self.sprite = self.downSprite
        self.position = pygame.Vector2()
        self.position.xy
        self.velocity = pygame.Vector2()
        self.velocity.xy = 0, 0
        self.width = self.sprite.get_width()/2
        self.height = self.sprite.get_height()-10
        self.xvalue = self.position.x+8
        self.yvalue =self.position.y-3

    def create_down(self,DISPLAY):
        self.sprite= self.downSprite
        self.position.xy=random.randint(0, DISPLAY.get_width() - self.sprite.get_width()),-60
        self.velocity.xy=0,random.randint(1,5)+ random.randint(0,9)* 0.1
        return self


    def create_up(self,DISPLAY):
        self.sprite= self.upSprite
        self.position.xy=random.randint(0, DISPLAY.get_width() - self.sprite.get_width()),(DISPLAY.get_height()+60)
        self.velocity.xy=0,(-random.randint(1,5)- random.randint(0,9)* 0.1)
        return self


    def create_right(self,DISPLAY):
        self.sprite= self.rightSprite
        self.position.xy=-60,random.randint(0, DISPLAY.get_height() - self.sprite.get_height())
        self.velocity.xy=random.randint(1,5)+ random.randint(0,9)* 0.1,0
        return self

    def create_left(self,DISPLAY):
        self.sprite= self.leftSprite
        self.position.xy=DISPLAY.get_width()+60,random.randint(0, DISPLAY.get_height() - self.sprite.get_height())
        self.velocity.xy=(-random.randint(1,5)- random.randint(0,9)* 0.1),0
        return self



 







    def bullet_increase(self,bulletsList,DISPLAY,borderBullet):
        li=[False]
        if borderBullet/2>= (len(bulletsList[0])+len(bulletsList[1])+len(bulletsList[2])+len(bulletsList[3])):
            borderBullet=0         
            rand=random.randint(0,3)
            newbullet=Bullet()
            if   rand==0:newbullet.create_down(DISPLAY)
            elif rand==1:newbullet.create_up(DISPLAY)
            elif rand==2:newbullet.create_right(DISPLAY)
            elif rand==3:newbullet.create_left(DISPLAY)
            li.pop()
            li.append(True)        
            li.append(rand)
            li.append(newbullet)

        return li     

            
