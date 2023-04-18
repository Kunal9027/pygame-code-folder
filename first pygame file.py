# ------PYGAME------- #

import pygame
import os
pygame.font.init()
pygame.mixer.init()

pygame.init()  # it initialize all pygame module

WIDTH , HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH ,HEIGHT))  # screen = command is use for change screen size
pygame.display.set_caption(" Game made by Kunal Chaudhary ")  # set_caption is used to change title of the screen

COLOR = 150, 190, 250  # Here R=150 , G=190 , B=250 RGB full form is RED GREEN BLUE
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

SHIP_WIDTH ,SHIP_HIGHT = 50 , 50
BORDER = pygame.Rect(295 ,0 ,10, 500 )

colck = pygame.time.Clock()
FPS = 30

SPEED_SHIP = 10
SPEED_BULLET = 15
MAX_bullets = 4

HIT_SOUND = pygame.mixer.Sound(os.path.join("assets/Grenade+1.mp3"))
SHOOT_SOUND = pygame.mixer.Sound(os.path.join("assets/Gun+Silencer.mp3"))

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT  = pygame.font.SysFont('comcsans' , 75)


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT  =pygame.USEREVENT + 2

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets/space.png")) , (WIDTH , HEIGHT))


YELLOW_player_image = pygame.image.load(os.path.join("assets/spaceship_yellow.png")) #os.path is used to locate the path thats why we import os 
YELLow_size = pygame.transform.scale(YELLOW_player_image, (SHIP_WIDTH,SHIP_HIGHT))
YELLOW_rotate = pygame.transform.rotate(YELLow_size , 90)

RED_player_image = pygame.image.load(os.path.join("assets/spaceship_red.png")) #load is used to used to load image 
RED_size = pygame.transform.scale(RED_player_image, (SHIP_WIDTH,SHIP_HIGHT))  #scale is used to resiz image 
RED_rotate = pygame.transform.rotate(RED_size , 270)  # transform.rotate is used to rotate image 

def draw_win(red , yellow , red_bullet , yellow_bulllet , red_health ,yellow_health):
    #screen.fill(COLOR)  # screen.fill is used to change bg_color
    screen.blit(BACKGROUND_IMAGE,(0,0))
    pygame.draw.rect(screen , BLACK , BORDER)

    red_health_text = HEALTH_FONT.render('health:' + str(red_health), 1 , COLOR)
    yellow_health_text = HEALTH_FONT.render('health:' + str(yellow_health), 1 , COLOR)

    screen.blit(red_health_text , (400 , 10))
    screen.blit(yellow_health_text , (10, 10))

    screen.blit(YELLOW_rotate,(yellow.x , yellow.y ))    #blit is use to put image on screen  
    screen.blit(RED_rotate ,(red.x ,red.y))

    for bullet in red_bullet: # Draw red bullets
        pygame.draw.rect(screen , RED, bullet)

    for bullet in yellow_bulllet:
        pygame.draw.rect(screen , YELLOW, bullet)


    pygame.display.flip()  # pygame.display.flip is used for update


def MANAGE_BULLETS(YELLOW_bullet,RED_bullet,yellow,red):
    #yellow bullets hit
    for bullet in YELLOW_bullet :
        bullet.x += SPEED_BULLET
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            YELLOW_bullet.remove(bullet)
        elif bullet.x > 600 :
            YELLOW_bullet.remove(bullet)

    #red  bullet hit
    for bullet in RED_bullet :
        bullet.x -= SPEED_BULLET
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            RED_bullet.remove(bullet)
        elif bullet.x < 0:
            RED_bullet.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text , 1 , COLOR)
    screen.blit(draw_text, (150 , 200))
    pygame.display.update()
    pygame.time.delay(5000)



def kunal():

    red = pygame.Rect(400,150 ,SHIP_WIDTH ,SHIP_HIGHT) # RECT is use to make a rectangle 
    yellow = pygame.Rect(50,300 ,SHIP_WIDTH ,SHIP_HIGHT)

    RED_bullet = []
    YELLOW_bullet = []

    red_health = 10
    yellow_health = 10

    running = True
    while running:
        colck.tick(FPS)                 # clock is use to set fps how many photos update per sec.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #if is to use make condition on certain event
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:  # key down event repest key is pressed
                if event.key == pygame.K_LCTRL and len(YELLOW_bullet) < MAX_bullets :   #
                    bullet = pygame.Rect(yellow.x + SHIP_WIDTH,yellow.y + SHIP_HIGHT/2 -3 , 10 ,5)
                    YELLOW_bullet.append(bullet)
                    SHOOT_SOUND.play()


                if event.key == pygame.K_RCTRL and len(RED_bullet) < MAX_bullets:
                   bullet = pygame.Rect(red.x ,red.y + SHIP_HIGHT/2 -3 , 10 ,5)
                   RED_bullet.append(bullet)
                   SHOOT_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text  = "YELLOW won"

        if yellow_health <= 0:
            winner_text = "RED won"

        if winner_text != "":
            draw_winner(winner_text) 
            break

        press_button = pygame.key.get_pressed()
        #YELLOW
        if press_button[pygame.K_a] and yellow.x - 4 > 0: #LEFT  #yellow.x -4 > 0 it means on x-axis we move less than zero key stop pressing
            yellow.x -=SPEED_SHIP
        if press_button[pygame.K_d] and yellow.x + 50 < 295 : #RIGHT
            yellow.x +=SPEED_SHIP
        if press_button[pygame.K_w] and yellow.y -4 > 0: #UP
            yellow.y -=SPEED_SHIP
        if press_button[pygame.K_s] and yellow.y +5 < 455: #DOWN
            yellow.y +=SPEED_SHIP
        #RED
        if press_button[pygame.K_LEFT] and red.x - 4 > 305 :  
            red.x -=SPEED_SHIP 
        if press_button[pygame.K_RIGHT] and red.x + 50 < 600:
            red.x +=SPEED_SHIP   
        if press_button[pygame.K_UP] and red.y -4 >0 :
            red.y -=SPEED_SHIP
        if press_button[pygame.K_DOWN] and red.y +5<455 :
            red.y +=SPEED_SHIP

        MANAGE_BULLETS(YELLOW_bullet,RED_bullet,yellow,red)
    
        draw_win(red , yellow, RED_bullet , YELLOW_bullet, red_health ,yellow_health)
        

    kunal()
    


if __name__ == "__main__":
    kunal()


### what i learn from this project
# 1.i learn how to creat game opening windoe/display
# 2.i learn how to set controls/keys 
# 3.i learn how to change background
# 4.i learn how to set fonts
# 5.i learn how to set sounds 
# 6.i learn how to creat events
# 7.i learn how to change disply dimensions
# 8.i learn how to use clock and set FPS using colck
# 9.i learn how to creat colors (255,255,255) / (Red,Green,Blue)
# 10.i learn how to use file location like soundsfile , image files using os module 
# 11.i learn how to creat projectiles like bullets