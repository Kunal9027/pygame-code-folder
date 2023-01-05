import pygame
import os

pygame.init()  # it initialize all pygame module

WIDTH , HEIGHT = 600, 500

screen = pygame.display.set_mode((WIDTH ,HEIGHT))  # screen = command is use for change screen size
COLOR = 150, 190, 250  # Here R=150 , G=190 , B=250 RGB full form is RED GREEN BLUE
BLACK = (0,0,0)
pygame.display.set_caption(" Game made by Kunal Chaudhary ")  # set_caption is used to change title of the screen

colck = pygame.time.Clock()
FPS = 30

SHIP_WIDTH ,SHIP_HIGHT = 50 , 50

BORDER = pygame.Rect(295 ,0 ,10, 500 )

SPEED_SHIP = 10

SPEED_BULLET = 7

YELLOW_player_image = pygame.image.load(os.path.join("assets/spaceship_yellow.png")) #os.path is used to locate the path thats why we import os 
YELLow_size = pygame.transform.scale(YELLOW_player_image, (SHIP_WIDTH,SHIP_HIGHT))
YELLOW_rotate = pygame.transform.rotate(YELLow_size , 90)

RED_player_image = pygame.image.load(os.path.join("assets/spaceship_red.png")) #load is used to used to load image 
RED_size = pygame.transform.scale(RED_player_image, (SHIP_WIDTH,SHIP_HIGHT))  #scale is used to resiz image 
RED_rotate = pygame.transform.rotate(RED_size , 270)  # transform.rotate is used to rotate image 

def draw_win(red , yellow):
    screen.fill(COLOR)  # screen.fill is used to change bg_color
    pygame.draw.rect(screen , BLACK , BORDER)
    screen.blit(YELLOW_rotate,(yellow.x , yellow.y ))    #blit is use to put image on screen  
    screen.blit(RED_rotate ,(red.x ,red.y))

    pygame.display.flip()  # pygame.display.flip is used for update


def kunal():

    red = pygame.Rect(400,150 ,SHIP_WIDTH ,SHIP_HIGHT) # RECT is use to make a rectangle 
    yellow = pygame.Rect(50,300 ,SHIP_WIDTH ,SHIP_HIGHT)

    running = True
    while running:
        colck.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        press_button = pygame.key.get_pressed()
        #YELLOW
        if press_button[pygame.K_a] and yellow.x - 4 > 0: #LEFT  #yellow.x -4 > 0 it means on x-axis we move less than zero key stop pressing
            yellow.x -=SPEED_SHIP
        if press_button[pygame.K_d] and yellow.x + 50 < 295 : #RIGHT
            yellow.x +=SPEED_SHIP
        if press_button[pygame.K_w] and yellow.y -4 >0: #UP
            yellow.y -=SPEED_SHIP
        if press_button[pygame.K_s] and yellow.y +5<455: #DOWN
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


        draw_win(red , yellow)

    pygame.quit()
    exit()


if __name__ == "__main__":
    kunal()
