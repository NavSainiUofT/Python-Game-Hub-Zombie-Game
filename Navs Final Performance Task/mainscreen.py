import pygame
import sys
pygame.init() #Starts up pygame
class startScreen(object):



    def __init__(self):
        self.x = 1
        self.font = pygame.font.SysFont("comicsansms",50)


    def message_2_screen(self,msg,colour, yDisplace, xDisplace,x):
        #Function for screen text (level,lives)
        screen_text = self.font.render(msg, True, colour)
        x.blit(screen_text,[10+xDisplace,yDisplace])

    def main_menu(self,gameDisplay):
        wallpaper = pygame.image.load('menu_back.jpg')

        pygame.display.set_caption("Running Dead")

        #gameDisplay = pygame.display.set_mode((1280,720))
        while self.x ==1:
            pygame.mouse.set_visible(True)
            gameDisplay.blit(wallpaper,(0,0))



            mouse = pygame.mouse.get_pos()

            if 450 > mouse[0] > 150 and 550 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,(0,0,250),(150,450,300,100))
            else:
                pygame.draw.rect(gameDisplay,(0,0,200),(150,450,300,100))


            if 1200 > mouse[0] > 900 and 550 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,(250,0,0),(900,450,300,100))
            else:
                pygame.draw.rect(gameDisplay,(200,0,0),(900,450,300,100))


            text = pygame.font.SysFont("impact",50)

            self.message_2_screen("Play", (255,255,255),460,245,gameDisplay)
            self.message_2_screen("Quit", (255,255,255),460,985,gameDisplay)


            pygame.display.update()




            for event in pygame.event.get():
                pygame.display.update()
                if (event.type == pygame.QUIT) :
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONUP:
                    pos=pygame.mouse.get_pos()
                    for i in range(150,450):
                        if pos[0]==(i):
                            for j in range(450,550):
                                if pos[1]==(j):
                                    self.x=0
                                    return False
                    for b in range(900,1200):
                        if pos[0]==(b):
                            for k in range(450,550):
                                if pos[1]==(k):
                                    pygame.quit()
                                    return True








