#Authors: Marc, Navdeep, Duncan, (Adi)
#Purpose: To make a sweet game
#Date Started: May 23, 2016
#Date Last Edited: Today
#
import pygame
pygame.init()
pygame.mixer.init()
import random
import time
#Imports the function that draws the crosshair
from Crosshair import MoveTheHair
from mainscreen import startScreen
#loads mp3 file to be played during game and loops 50 times(5 min song more than enough time)

class Background(object):


    def __init__(self):
        #Initializes variables
        #sets canvas size
        self.height = 720
        self.width = 1280
        #creates canvas
        self.gameDisplay = pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        #creates timer to be increased each level
        self.clock = pygame.time.Clock()
        #calls the function that creates the zombie image on the display
        self.zombie = self.create_zombie()
        #variable sent to clock to determine how fast zombies move
        self.tickvalue = 7
        #sets a stipulation for the game loop to run
        self.game_exit = False
        #determines the number of lives the player starts with
        self.life_count = 5
        #determines what level the player is on
        self.level_on = 1
        #initializes the font comic sans
        self.font = pygame.font.SysFont("comicsansms",40)

    def message_to_screen(self,msg,colour, yDisplace, xDisplace,x):
        #Function for screen text (level,lives)
        screen_text = self.font.render(msg, True, colour)
        x.blit(screen_text,[10+xDisplace,yDisplace])

    def gameloop(self):
        #Main game loop


        #Sets window title
        pygame.display.set_caption("The Running Dead")
        #Sets background image
        background_image = pygame.image.load("background.png")
        #Creates variables that help with the zombies targeting/tracking
        self.move_counter = 0
        ace_stopper = 0
        #Variables z# are used to determine if zombie is shot or reaches house '''
        z1 = 0
        z2 = 0
        z3 = 0
        #Creates the zombies with their randomized range of coords
        zombie1 = self.zombie_coords1()
        zombie2 = self.zombie_coords2()
        zombie3 = self.zombie_coords3()
        #Zombies starting points that will be increased
        xvalue1 = 0
        xvalue2 = 0
        xvalue3 = 0

        #Death counter
        deaths = 0
        #Stops code if condition is met
        temp = 0
        #How many zombies are left
        zombie_count = 3

        game_exit = False
        while not self.game_exit:
            #Background and in game text
            self.gameDisplay.blit(background_image,(0,0))
            self.message_to_screen("Lives:"+str(self.life_count),(255,0,0),0,0,self.gameDisplay)
            self.message_to_screen("Level:"+str(self.level_on),(255,0,0),50,0,self.gameDisplay)
            #X button at top right
            pygame.draw.rect(self.gameDisplay, (255,0,0), [1230, 0, 50, 50])
            self.message_to_screen("X", (0,0,0),-5,1232, self.gameDisplay)

            #Crosshair
            instance = MoveTheHair()
            instance.crosshair(self.gameDisplay)

            #Targeting/tracking mouse position
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.game_exit=True
                if event.type == pygame.MOUSEBUTTONUP:
                    #Gets mouse position when clicked and checks if its on the x-button
                    pos=pygame.mouse.get_pos()
                    #Draws yellow circle to indicate when player clicks
                    pygame.draw.circle(self.gameDisplay,(255,255,0),pos,10,10)
                    sound = pygame.mixer.Sound("Gun.ogg")
                    sound.play()
                    Quiting=self.Exit(1230,-5,pos)
                    if Quiting==True:
                        pygame.quit()
                        return True


                    #Otherwise it calls Target() which checks mouses coords with the zombies coords
                    Trial=self.Target(zombie1[0],zombie1[1],zombie2[0],zombie2[1],zombie3[0],zombie3[1],self.move_counter,pos)
                    #Checks what Trial returned (True/False , 1/2/3)
                    if Trial[0] == True:
                        if Trial[1]==1:
                            z1 = 1

                        if Trial[1]==2:
                            z2 = 1

                        if Trial[1]==3:
                            z3 = 1
            #Zombie code(Only draws zombie if zombie is not shot)
            if ace_stopper == 0:

                for i in range (3):
                    #draws the zombie if its not shot
                    if i == 0 and z1 == 0:
                        self.gameDisplay.blit(self.zombie,(xvalue1,zombie1[1]))
                        #moves the zombie x number of pixels
                        xvalue1+=15
                    if z1 == 1 :
                        xvalue1 = -10
                    if i == 1 and z2 == 0:
                        self.gameDisplay.blit(self.zombie,(xvalue2,zombie2[1]))

                        xvalue2+=15
                    if z2 == 1:
                        xvalue2 = -10
                    if i ==2 and z3 == 0:
                        self.gameDisplay.blit(self.zombie,(xvalue3,zombie3[1]))

                        xvalue3+=15
                    if z3 == 1:
                        xvalue3 = -10
                #once its determined which zombies need to be drawn, it draws them
                pygame.display.flip()


                #Keeps track of how many times zombie moved. Used in Target()
                self.move_counter += 1
                #Checks if zombie reaches end and takes away a life if true
                if temp == 0 and zombie_count>0:
                    if xvalue1>=1190:
                        ace_stopper=1
                        z1=2
                    if ace_stopper == 1:
                        deaths -=1
                    if xvalue2>=1190:
                        ace_stopper=2
                        z2=2
                    if ace_stopper == 2:
                        deaths -=1
                    if xvalue3>=1190:
                        ace_stopper=3
                        z3=2
                    if ace_stopper == 3:
                        deaths -=1

                    if ace_stopper!=0:
                        #changes the temp stopper so the code above does not run
                        temp = 1
            #Counts deaths
            self.life_count+=deaths
            deaths = 0
            #The time delay which determines their speed
            self.clock.tick(self.tickvalue)
            #pygame.time.wait(self.tickvalue)
            if z1 !=0 and z2 != 0 and z3 !=0:
                break
        return False




    def level_pass(self,username):
    #Runs game after level ends if your lives>0 otherwise it will quit program
        instance1 = startScreen()
        runner = False
        stopper = False

        while runner == False and stopper == False:
            pygame.init()
            #creates conditions that must be met in order for this program to run to prevent anything pygame running after pygame.quit
            #also to allow the main menu to end
            if stopper == False:
                instance1.x=1

                stopper = instance1.main_menu(self.gameDisplay)



                while self.life_count>0 and runner == False and stopper == False:
                    #speeds up zombies and increases level count
                    runner = self.gameloop()
                    #pygame.mouse.set_visible(True)
                    self.level_on+=1
                    self.tickvalue+=3

                totlist = []
                username_read = open("usernames.txt","r")

                counter = 0
                for line in username_read:
                    if line.startswith(username):
                        logged_score = counter
                        textValues = line.split()
                    counter = counter+1

                #checks if the score got is bigger than the old high score
                if self.level_on > int(textValues[2]):
                    redo = open("usernames.txt","r")

                    for line in redo:
                        reWrite = line.split()
                        totlist.append(reWrite)

                    totlist[logged_score][2] = self.level_on

                    rewritter = open("usernames.txt","w")
                    nextvar = -1
                    #rewrites the whole file with the new score inserted
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
                top10appender.write(username+" "+str(0)+" "+str(self.level_on)+"\n")
                top10appender.close()

            self.life_count = 5
            self.tickvalue = 7
            self.level_on=1



    def create_zombie(self):
        #Loads in zombie image
        zombie = pygame.image.load("zombie_sprite.png")
        return zombie
    def zombie_coords1(self):
        #creates zombie 1 coords
        y_cord = random.randint(59,66)*10
        x_cord = 0
        coords = (x_cord,y_cord)
        return coords
    def zombie_coords2(self):
        #creates zombie 2 coords
        y_cord = random.randint(46,52)*10
        x_cord = 0
        coords = (x_cord,y_cord)
        return coords
    def zombie_coords3(self):
        #creates zombie 3 coords
        y_cord = random.randint(33,39)*10
        x_cord = 0
        coords = (x_cord,y_cord)
        return coords
    def Target(self,zx1,zy1,zx2,zy2,zx3,zy3,moves,pos):
        #Compares mouse position to zombies coords
        #Uses moves variable to determine where zombie is currently based off of original coords passed
        moves=moves*15
        zx1+=moves
        zx2+=moves
        zx3+=moves
        #Compares x-values then y-values
        for i in range (0,30):
            if pos[0]==(zx1+i):
                for j in range(0,60):
                    if pos[1]==(zy1+j):
                        return True,1
            if pos[0]==(zx2+i):
                for j in range(0,60):
                    if pos[1]==(zy2+j):
                        return True,2
            if pos[0]==(zx3+i):
                for j in range(0,60):
                    if pos[1]==(zy3+j):
                        return True,3
        return False,0

    def Exit(self,x1,y1,pos):
        #Exits if True
        for i in range (0,50):
            if pos[0]==(x1+i):
                for j in range(0,50):
                    if pos[1]==(y1+j):
                        return True

