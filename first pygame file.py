import pygame

pygame.init()  # it initialize all pygame module

screen = pygame.display.set_mode(
    (400, 600)
)  # screen = command is use for change screen size


color = 150, 190, 250  # Here R=150 , G=190 , B=250 RGB full form is RED GREEN BLUE


pygame.display.set_caption(
    " Game made by Kunal Chaudhary "
)  # set_caption is used to change  title of the screen

# its main function for running window

if __name__ == "__main__":

    def kunal():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()  # pygame.display.flip is used for update

            screen.fill(color)  # screen.fill is used to change bg_color

        pygame.quit()
        exit()


kunal()
