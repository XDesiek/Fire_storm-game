import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from button import Button
from player import Player
from bullet import Bullet
from others import checkCollisions
from spritesheet import Spritesheet 
from boom import Boom
from coin import Coin
from title_screen import TitleScreen

def main():
    pygame.init()


    # display resolution
    size = 1280,800
    DISPLAY = pygame.display.set_mode((size))



    # get images
    bg = pygame.image.load('data/sprites/bg.png').convert()

    
    # get fonts
    font = pygame.font.Font('data/fonts/font.otf', 100)
    font_small = pygame.font.Font('data/fonts/font.otf', 32)
    font_20 = pygame.font.Font('data/fonts/font.otf', 20)  


    # get sounds
    
    death=pygame.mixer.Sound("data/sfx/death_sound.mp3")


    

    
    


    # creating everything from other files
    def create(bulletStartCount):
        global player 
        global bulletsList
        global wsad
        global mainCoin
        player=Player()
        mainCoin=Coin()
        
        # poczatkowa position of player
        player.position.x = DISPLAY.get_width()/2
        player.position.y = DISPLAY.get_height()/2

    
        
        up = False
        down = False
        right = False
        left = False
        wsad=[[pygame.K_w,up],[pygame.K_s,down],[pygame.K_d,right],[pygame.K_a,left]]
        # bullet starting pos
        noDirectBullets = [Bullet() for i in range(bulletStartCount)]
        upbullets=[]
        downbullets=[]
        rightbullets=[]
        leftbullets=[]
        bulletsList=[upbullets,downbullets,rightbullets,leftbullets]
        for bullet in noDirectBullets:
            rand=random.randint(0,3)
            if   rand==0:bulletsList[rand].append(bullet.create_down(DISPLAY))
            elif rand==1:bulletsList[rand].append(bullet.create_up(DISPLAY))
            elif rand==2:bulletsList[rand].append(bullet.create_right(DISPLAY))
            elif rand==3:bulletsList[rand].append(bullet.create_left(DISPLAY))
        

    


    # jakies variablers requred later / somewhere
    titleScreen= TitleScreen()
    pointTimer = 0
    borderBullet = 0
    highScore = 0
    framerate = 60
    last_time = time.time()
    running = True
    boom=Boom()
    bulletmulti=1
    bulletStartCount= 10
    
    create(15)

# title screen
    while titleScreen.title_screen_open:titleScreen.title_screen(DISPLAY,last_time)

        
    while running:        
        pygame.display.set_icon(Bullet().sprite)
        pygame.display.set_caption('Fire Storm')


        
        

        # czas i background
        dt = time.time() - last_time
        dt *= framerate
        last_time = time.time()
        DISPLAY.blit(bg, (0,0)) 
        


        if not player.dead:


            for event in pygame.event.get():
                # if the player quits
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                # zmienia tru false jak naciskam albo puszczamd
                for wsadkey in wsad:
                    if event.type == pygame.KEYDOWN and event.key == wsadkey[0]:wsadkey[1]=True
                    if event.type == pygame.KEYUP and event.key == wsadkey[0]:wsadkey[1]=False
#                                                           dash
                if event.type == pygame.KEYDOWN and event.key == K_i:
                    player.dash=True
                    
            player.dashy()
            
            # coins
            mainCoin.coin_work(DISPLAY,player)

            #samo ruszanie sie 
            if wsad[0][1]==True:player.position.y -= player.velocity * dt
            if wsad[1][1]==True:player.position.y += player.velocity * dt
            if wsad[2][1]==True:player.position.x += player.velocity * dt
            if wsad[3][1]==True:player.position.x -= player.velocity * dt

            # punkty
            pointTimer += 1
            if pointTimer==100:
                pointTimer=0
                player.points +=1




            cpoints = font.render(str(player.coinPoints), True, (207, 194, 136))
            DISPLAY.blit(cpoints,(20, 20))
            cointext = font_small.render("coins:", True, (200,200,200))
            DISPLAY.blit(cointext,(10,0))
            if highScore<player.coinPoints:highScore=player.coinPoints



            # walls
            if player.position.x <-10:player.position.x+=3
            if player.position.x >DISPLAY.get_width()-10:player.position.x-=3
            if player.position.y <-10:player.position.y+=3
            if player.position.y >DISPLAY.get_height()-10:player.position.y-=3





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            for bullets in bulletsList:
                for bullet in bullets:
                    DISPLAY.blit(bullet.sprite,bullet.position)
                    # ruch bulletow
                    bullet.position.x += bullet.velocity.x*dt
                    bullet.position.y += bullet.velocity.y*dt

                    # umieranko
                    if (checkCollisions((player.position.x+2), (player.position.y+3), (player.sprite.get_width()/8*7), (player.sprite.get_height()/16*13), (bullet.position.x+8), (bullet.position.y-3), (bullet.sprite.get_width()/2), (bullet.sprite.get_height()-10))):
                        player.dead= True
                        death.play()
                        DISPLAY.blit(bg, (0,0)) 
                        boom.render_gif(DISPLAY,player.position)
                        pygame.time.delay(90)



                    # respawnowanie bulletow
                    if bullet.position.y >= DISPLAY.get_height()+60 and bullet.sprite==bullet.downSprite:
                        bullet.create_down(DISPLAY)
                        borderBullet +=bulletmulti
                    elif bullet.position.y <=-60 and bullet.sprite==bullet.upSprite:
                        bullet.create_up(DISPLAY)
                        borderBullet+=bulletmulti
                    elif bullet.position.x >= DISPLAY.get_width()+60 and bullet.sprite==bullet.rightSprite:
                        bullet.create_right(DISPLAY)
                        borderBullet +=bulletmulti

                    elif bullet.position.x <= -60 and bullet.sprite==bullet.leftSprite:
                        bullet.create_left(DISPLAY)
                        borderBullet +=bulletmulti

            ql=bullet.bullet_increase(bulletsList,DISPLAY,borderBullet)
            if ql[0]:
                bulletsList[ql[1]].append(ql[2])



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                        
                        
            DISPLAY.blit(player.sprite,player.position)
#                                                              dead 
        if player.dead:
            
            for event in pygame.event.get():
                # if the player quits
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                
                # respawn 
                if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    coinnumber=random.randint(2,6)
                    create(bulletStartCount)
                
            # render napisow po skonczeniu 
            uDied = font.render('You Died', True, (200,200,200))
            DISPLAY.blit(uDied,(DISPLAY.get_width()/2, DISPLAY.get_height()/2-40))
            spaceToCont = font_small.render('press space to continue', True, (200,200,200))
            DISPLAY.blit(spaceToCont,(DISPLAY.get_width()/2+20, DISPLAY.get_height()/2+60))
            highScoreText = font_small.render('Highscore:', True, (200,200,200))
            DISPLAY.blit(highScoreText,(30, 230))
            highScoreCountText = font_small.render(str(player.coinPoints), True, (200,200,200))
            DISPLAY.blit(highScoreCountText,(180, 230))     
#                                                              dead 
        pygame.display.update()
        pygame.time.delay(10)









if __name__ == "__main__":
    main()