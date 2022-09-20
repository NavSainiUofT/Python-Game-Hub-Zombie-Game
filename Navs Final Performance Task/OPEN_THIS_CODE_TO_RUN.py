#-------------------------------------------------------------------------------
# Name:        Login App/ Game Hub
# Purpose:      To simulate a login ui with game selector
#
# Author:      Navdeep Saini
#
# Created:     06/05/2016
#-------------------------------------------------------------------------------
#Import the class that created the ui that we made in designer from both the login and signup windows. This way the ui could be changed still without effecting the rest of the code.
"""ZOMBIE AND SNAKE GAME HAVE OTHER COMMENTS AND FILE APPENDING CODES
   ALSO TUPLES ARE USED IN THE ZOMBIE GAME"""
from Login_UI import Ui_MainWindow
from signup_UI import Ui_signup
from Top10_UI import Ui_Top_10_Scorers
from PyQt4 import QtCore, QtGui
from NavPick import Game_Pick
from Zombie_Game import Background

import pygame

class Game_Picker(QtGui.QMainWindow,Game_Pick,Background):
    def __init__(self,username):
        QtGui.QMainWindow.__init__(self)
        #calls the ui from another file
        self.game_select = Game_Pick()
        self.game_select.setupUi(self)
        #Gives functions to the clicked buttons
        self.game_select.back_btn.clicked.connect(self.game_picker_exit)
        self.game_select.zombie_btn.clicked.connect(self.runzom)
        self.game_select.snake_btn.clicked.connect(self.runsnake)
        username_read = open("usernames.txt","r")
        for line in username_read:
            if line.startswith(username):
                scorevals = line.split()
        #goes through the username file and displays the high score for the logged in user
        self.game_select.zombie_scorelcd.display(scorevals[2])
        self.game_select.snake_scorelcd.display(scorevals[1])

        self.namess = username
    #exits
    def game_picker_exit(self):
        self.close()
    #runs snake game
    def runsnake(self):
        pygame.init()
        import snakeSummative
        snakescore = snakeSummative.main(self.namess)

    #if zombie game button is pressed runs zombie game
    def runzom(self):
        pygame.init()
        pygame.mixer.music.load("Crusade.mp3")
        pygame.mixer.music.play(50)
        zomrun = Background()
        zomscore = zomrun.level_pass(self.namess)




# THis class handels the top 10 table window
class Top_10(QtGui.QMainWindow, Ui_Top_10_Scorers):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.top_10_ui = Ui_Top_10_Scorers()
        self.top_10_ui.setupUi(self)
        self.top_10_ui.Close_btn_topscorers.clicked.connect(self.top_10_exit)
        #sets row and columb counts for the snake and zombie tables
        self.top_10_ui.Snake_Table.setRowCount(10)
        self.top_10_ui.Snake_Table.setColumnCount(2)
        self.top_10_ui.Zombie_Table.setRowCount(10)
        self.top_10_ui.Zombie_Table.setColumnCount(2)
        self.tabledisplayer()

    def tabledisplayer(self):
        #opens a file and creates 2 empty lists
        scoresortfile = open("top10.txt","r")
        snakelist = []
        zombielist = []
        #APPENDS all the usernames and scores into a 2d list
        for line in scoresortfile:
            splitter = line.split()
            snakelist.append(splitter)
            zombielist.append(splitter)
        #if the length is bigger then 0, runs the functions below to sort the lists
        if len(snakelist) > 0 and len(zombielist) > 0:
            finalsnakelist = self.topsnake(snakelist)
            snakelistcounter = 0
            finalzombielist = self.topzombie(zombielist)
            zombielistcounter = 0
            #k and i are the rows and colombs and this nested for loop displays the values on the table.
            for k in range(10):
                if snakelistcounter < len(finalsnakelist)-1:
                    for i in range(2):
                        if int(finalsnakelist[snakelistcounter][1])!= 0:
                            if i+1 == 1:
                                self.top_10_ui.Snake_Table.setItem(k,i,QtGui.QTableWidgetItem(str(finalsnakelist[snakelistcounter][0])))
                            if i+1 == 2:
                                self.top_10_ui.Snake_Table.setItem(k,i,QtGui.QTableWidgetItem(str(finalsnakelist[snakelistcounter][1])))
                snakelistcounter += 1
            # same as above but for other table
            for o in range(10):
                #if there is less than 10 entrys in the list
                if zombielistcounter < len(finalzombielist)-1:
                    for p in range(2):
                        if int(finalzombielist[zombielistcounter][2]) != 0:
                            if p+1 == 1:
                                self.top_10_ui.Zombie_Table.setItem(o,p,QtGui.QTableWidgetItem(str(finalzombielist[zombielistcounter][0])))
                            if p+1 == 2:
                                self.top_10_ui.Zombie_Table.setItem(o,p,QtGui.QTableWidgetItem(str(finalzombielist[zombielistcounter][2])))
                zombielistcounter += 1


    # Sorts the 2d list by checking the score element inside and switching the whole list if nessisary
    def topsnake(self,snakelist):
        for k in range (len(snakelist)):
            for j in range(len(snakelist)-1):
                if int(snakelist[j][1]) > int(snakelist[j+1][1]):
                    pass
                else:
                    var1 = snakelist[j+1]
                    var2 = snakelist[j]
                    snakelist[j] = var1
                    snakelist[j+1] = var2
        if int (snakelist[-1][1])>int(snakelist[0][1]):
            snakelist.insert(snakelist[-1],0)
            snakelist.pop([-1])
        return snakelist

    def topzombie(self,zombielist):
        for k in range (len(zombielist)):
            for j in range(len(zombielist)-1):
                if int(zombielist[j][2]) > int(zombielist[j+1][2]):
                    pass
                else:
                    var1 = zombielist[j+1]
                    var2 = zombielist[j]
                    zombielist[j] = var1
                    zombielist[j+1] = var2
        if int (zombielist[-1][2])>int(zombielist[0][2]):
            zombielist.insert(0,zombielist[-1])
            zombielist.pop([-1])
        return zombielist



    def top_10_exit(self):
        self.close()


#creates a class that inherits the main ui_signup class from the signup ui python file
class SignUp(QtGui.QMainWindow, Ui_signup):
    #initialized all of out buttons and functions from the inherited class and gives the buttons functions from this class when clicked.
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #created a variable to represent an instance of our signup ui for code reusabilty.
        self.signup_ui = Ui_signup()
        #called the setup method from our signup window py file.
        self.signup_ui.setupUi(self)
        #gave the cancel button and the signup button functions to work with
        self.signup_ui.cancel_btn_signup.clicked.connect(self.signup_exit)
        self.signup_ui.signup_btn_signup.clicked.connect(self.signup_text)
    #defined the cancel buttons function so that it exits only the instance of the signup window and not the main window
    def signup_exit(self):
        self.close()

    #to make things simpler because i created several message boxes, I just made a function that takes 2 strings as arguments and makes a message box
    def msgBox(self,header,text):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'header', 'Completed')
        msgBox.setText(text)
        msgBox.addButton(QtGui.QPushButton('ok'), QtGui.QMessageBox.YesRole)
        ret = msgBox.exec_();

    #this function handles all tasks necissary when the sign up button is clicked
    def signup_text(self):
        #opens the username and password file for appending but just the username file for reading to check if usernames are taken.
        username_file = open("usernames.txt", "a")
        password_file = open("passwords.txt", "a")
        username_read = open("usernames.txt","r")
        #converted the qlineedites into string so that it could be compared to elements in our username text files and appended to both text files when neccisary
        # the \n is so that it appends to the next line and reads the next line when iterating.
        password1 = self.signup_ui.password_txtfield_signup.text()+"\n"
        password2 = self.signup_ui.confirmpassword_txtfield_signup.text()+"\n"
        username = self.signup_ui.username_txtfield_signup.text()


        #to account for all scenarios like if the user left the username blank
        if username == "":
            self.msgBox("Something Went Wrong!!","Username Was Left Empty!!")
        elif (" " in username) == True:
            self.msgBox("Something Went Wrong!!","Sorry You cant have Spaces in your Username!!")
        elif password1 == ""+"\n":
            self.msgBox("Something Went Wrong!!","Sorry your password is BLANK!!")
        elif (" " in password1) == True:
            self.msgBox("Something Went Wrong!!","Sorry You cant have Spaces in your password!!")
        #sets up a sinerio that must hold true in order to append the text to the files
        elif password1 == password2 and password1!="" and username != "" :
            #creates a variable so it can be changed if the username is taken and then the file appending can be prevented.
            stop_username = 0
            for line in username_read:
                #if line is equal to username that means its taken and so stopusername changes and the text is not appended. instead a message box comes up telling the user whats going on
                if username == line:
                    self.msgBox("Something Went Wrong!!","Username Was Taken")
                    stop_username = 1

            #if the for loop is passed successfully than the text is appended . remember users can have the same password but not usernames thats why i did not check passwords.
            if stop_username == 0:
                password_file.write(password1)
                username_file.write(username+' 0'+' 0'+'\n')
                self.msgBox("Something Went Right!!","You have successfully SIGNED UP!!")



        #checks if you passwords match cant be in the elif because I want this to run after the others go through because the signup failed if it gets to this point
        if password1 != password2:
            self.msgBox("Something Went Wrong!!","Sorry your passwords DONT MATCH!!")





########################################################################


#this is the class that inherits the window from the login ui py file which is our main window
class Main(QtGui.QMainWindow, Ui_MainWindow):
    #initiallizes the imported class and sets a variable to represent an instance of it for code reusability
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #gives the buttons functions once they are clicked. those functions are within this "MAIN" class
        self.ui.Signup_btn.clicked.connect(self.signup)
        self.ui.Cancel_btn.clicked.connect(self.mainwindow_exit)
        self.ui.Login_btn.clicked.connect(self.login_function)
        self.ui.Score_btn.clicked.connect(self.top10)
    #If the sign up button is clicked it creates an instance of the other signup class.
    def signup(self):
        self.new_user=SignUp()
        self.new_user.show()
    def top10(self):
        self.top10 = Top_10()
        self.top10.show()
    def gamepick(self,username):
        self.game_selector = Game_Picker(username)
        self.game_selector.show()
    #If the cancel button is pressed, closes the window
    def mainwindow_exit(self):
        self.close()
    #just like in the other class for reuse purposes it was easier to make this function and pass it strings.
    def msgBox(self,header,text):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'header', 'Completed')
        msgBox.setText(text)
        msgBox.addButton(QtGui.QPushButton('ok'), QtGui.QMessageBox.YesRole)
        #shows the message box but unlike show() shows until acted upon
        ret = msgBox.exec_();
    #when the login button is pressed, this runs.
    def login_function(self):
        #opens both files for reading because we dont need to append here
        username_read = open("usernames.txt","r")
        password_read = open ("passwords.txt","r")
        #grabs whatever text is in the qlineedites and converts it to str so it can be compared to the opened file's lines
        username = self.ui.Username_txtfield.text()
        password = self.ui.Password_txtfield.text()+"\n"

        #sets up a counter variable and a checker variable
        self.line_num = 0
        user_in = 0


        #iterates through the lines in the username file
        for line in username_read:
            alist = []


            #adds to the counter

            alist.append(str.split(line))
            if alist[0][0] == username:
                user_in = 1
            if user_in == 0:
                self.line_num+=1



            #if the loops failed and userin is still 0, a message box comes up saying the names doesnt exist
        if user_in == 0:
            self.msgBox("Something Went Wrong!!","This Username Does Not EXIST! PLEASE SIGNUP!")
        # if the username was indeed in one of those lines(or in our case = to a line), than this code runs
        if user_in == 1:
            #sets another counter for the password file
            pass_line_num=0
            #iterates through the opened password text doc
            for line in password_read:
                #adds to the counter

                #once the counter is equal to where the username counter stopped than it checks if that line is equal to the value entered by the user.
                if pass_line_num == self.line_num:
                    if line == password:
                        #sends the usernames through to be used in other classes as well
                        gamepicker = self.gamepick(username)


                        #tells the user they logged in or are incorrect.
                    else:
                        self.msgBox("Something Went Wrong!!","You password was INCORRECT!! Please double check your CAPS!!")
                pass_line_num+=1



# allows this code to be reused by only running if run from this code and so class can be imported.
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #Creating an instance of our main login window (not the signup window that comes within the login window class "Main")
    window = Main()
    #Displays the main window on the screen
    window.show()
    #Allows the user to exit if neccisary
    sys.exit(app.exec_())