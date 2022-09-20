import pygame
import random

pygame.init()

#gameDisplay = pygame.display.set_mode((1280, 720)) #create a canvas
#pygame.display.set_caption("The Running Dead: Super Deluxe Complete Edition 2.0")
#icon = pygame.image.load("pepe2.png")
#pygame.display.set_icon(icon)

class MoveTheHair(object):
    

        

        

    #pygame.mouse.set_visible(0)
    def crosshair(self,x):
        LeadX = 640
        LeadY = 360
        lead_dx = 0
        lead_dy = 0
    
        gameExit = False
        ender = 0
        white = (255, 255, 255)
        red = (255, 0, 0)

        
        LeadXY = pygame.mouse.get_pos()
        LeadX = LeadXY[0]
        LeadY = LeadXY[1]

        pygame.mouse.set_visible(0)
        pygame.draw.circle(x, white,[LeadX,LeadY],35)
        pygame.draw.rect(x, red, [LeadX-25, LeadY, 50, 2])
        pygame.draw.rect(x, red, [LeadX, LeadY-25, 2, 50])
        #pygame.display.update()

        #if LeadX > canvaswdth or LeadY > canvashei or LeadX < 0 or LeadY < 0 or ender == 1:
            #LeadX = 640
            #LeadY = 360
            

                    


