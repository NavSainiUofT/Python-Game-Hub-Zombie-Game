#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wrightty
#
# Created:     03/05/2016
# Copyright:   (c) wrightty 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame, time, random

#pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)


clock = pygame.time.Clock()

#gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
#pygame.display.set_caption("Slither")





font = pygame.font.SysFont(None, 25)

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, gameDisplay):
    #text surface (just like pygame surface) where we're going to put the text
    #textRect -
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2)
    gameDisplay.blit(textSurf, textRect)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])

def gameLoop(gamerunvalue,gameDisplay):

    gameOver = gamerunvalue

    lead_x = DISPLAY_WIDTH/2 # x and y locations for the head of the snake
    lead_y = DISPLAY_HEIGHT/2
    lead_dx = BLOCK_SIZE
    lead_dy = 0
    direction = 'right'
    randAppleX = random.randrange(0, DISPLAY_WIDTH-BLOCK_SIZE, BLOCK_SIZE)
    randAppleY = random.randrange(0, DISPLAY_HEIGHT-BLOCK_SIZE, BLOCK_SIZE)
    snakeList = []
    snakeHead = []
    snakeLength = 1
    score = 1

    while gameOver is not True:
        #message_to_screen("Score: "+score,(255,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction is not 'right':
                    lead_dx = -BLOCK_SIZE
                    lead_dy = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction is not 'left':
                    lead_dx = BLOCK_SIZE
                    lead_dy = 0
                    direction = 'right'
                elif event.key == pygame.K_UP and direction is not 'down':
                    lead_dy = -BLOCK_SIZE
                    lead_dx = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction is not 'up':
                    lead_dy = BLOCK_SIZE
                    lead_dx = 0
                    direction = 'down'


        lead_x += lead_dx
        lead_y += lead_dy

        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            gameOver = True

        gameDisplay.fill(WHITE)

        appleThickness = 30
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, appleThickness, appleThickness])

        #store the position of the front of the snake in an empty list
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        #add the position of the front of the snake to the list that holds all elements
        #of our snake
        snakeList.append(snakeHead)

#if the size of the snake list is bigger then the length the snake is supposed to be,
#delete the 'end' of the snake
        if len(snakeList) > snakeLength:
            del snakeList[0]

#check if snake collides with itself
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        for xy in snakeList:
            pygame.draw.rect(gameDisplay, GREEN, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])

        message_to_screen("Score: "+str(score),(139,42,69),gameDisplay)

        pygame.display.update()
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + BLOCK_SIZE > randAppleX and lead_x + BLOCK_SIZE < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + BLOCK_SIZE > randAppleY and lead_y + BLOCK_SIZE < randAppleY + appleThickness :
                randAppleX = random.randrange(0, DISPLAY_WIDTH-BLOCK_SIZE, BLOCK_SIZE)
                randAppleY = random.randrange(0, DISPLAY_HEIGHT-BLOCK_SIZE, BLOCK_SIZE)
                snakeLength += 1
                score += 1

        clock.tick(FPS)
    return score


def playAgain(gameDisplay):

    gameDisplay.fill(WHITE)
    message_to_screen("press c to play or press q to quit", RED,gameDisplay)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                        return False
                if event.key == pygame.K_q:
                        return True



def main(username):
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    BLOCK_SIZE = 20
    FPS = 15

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 155, 0)


    gameOver = False
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Slither")
    #creates conditions that must be met to run the game loop and main menu
    while not gameOver:

        gameOver = playAgain(gameDisplay)
        if gameOver == False:
            #the game loop returns the score got
            score = gameLoop(gameOver,gameDisplay)
            totlist = []
            #opens the file to append
            username_read = open("usernames.txt","r")


            #checks which user is logged in and appends only that line to a list
            counter = 0
            for line in username_read:
                if line.startswith(username):
                    logged_score = counter
                    textValues = line.split()
                counter = counter+1
            #checks if the score is bigger than the previous high score
            if score > int(textValues[1]):
                redo = open("usernames.txt","r")
                # saves all the lines in the username file in 1 list so that it can be rewritten with new value
                for line in redo:
                    reWrite = line.split()
                    totlist.append(reWrite)
                #swaps old score with newscore
                totlist[logged_score][1] = score
                #rewrites file
                rewritter = open("usernames.txt","w")
                nextvar = -1
                for writer in range(len(totlist)):
                    nextvar += 1
                    rewritter.write(str(totlist[nextvar][0]))
                    rewritter.write(" ")
                    rewritter.write(str(totlist[nextvar][1]))
                    rewritter.write(" ")
                    rewritter.write(str(totlist[nextvar][2]))
                    rewritter.write("\n")
                rewritter.close()
            top10appender = open("top10.txt","a")
            top10appender.write(username+" "+str(score)+" "+str(0)+"\n")
            top10appender.close()

    pygame.display.quit()

