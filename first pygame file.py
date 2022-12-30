import pygame

pygame.init()  # it initialize all pygame module

screen = pygame.display.set_mode((600, 500))  # screen = command is use for change screen size

COLOR = 150, 190, 250  # Here R=150 , G=190 , B=250 RGB full form is RED GREEN BLUE

pygame.display.set_caption(" Game made by Kunal Chaudhary ")  # set_caption is used to change  title of the screen

colck = pygame.time.Clock()
FPS = 30


def draw_win():
    screen.fill(COLOR)  # screen.fill is used to change bg_color
    pygame.display.flip()  # pygame.display.flip is used for update


def kunal():
    running = True
    while running:
        colck.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_win()

    pygame.quit()
    exit()


if __name__ == "__main__":
    kunal()
