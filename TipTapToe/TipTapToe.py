import kivy
import kivymd
kivy.require('2.0.0') # replace with your current kivy version !
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import random

class Player:
    def __init__(self,id):
        self.id = id

class Square:
    def __init__(self,x,y):
        self.status = 0     # 0=empty, 1=occupied by player1, 2=occupied by player2
        self.x = x
        self.y = y
    
    def clear(self):
        self.status = 0

class TipTapToe(Screen):
    def __init__(self,**kwargs):
        super().__init__()
        self.checkerboard = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(Square(i,j))
            self.checkerboard.append(temp)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.currPlayer = random.randint(1,2)    
        self.ids.message.text = "Player" + str(self.currPlayer) + "'s turn"
    
    # sets the square [x,y] as occupied by playerID
    def assign(self,x,y,playerID=-1):
        if(self.checkerboard[x][y].status!=0):
            if(playerID==-1):
                return [ False , self.currPlayer ]
            else:
                return [ False , playerID ]
        if (playerID==-1):
            playerID = self.currPlayer
        self.checkerboard[x][y].status = playerID
        check = self.checkWin(x, y, playerID)
        if(check):
            return [ True , playerID ]
        self.currPlayer = 3-playerID
        return [ False , playerID ]

    # clear the checkerboard
    def clear(self,x=-1,y=-1):
        if(x==-1):
            mx=0
            Mx=3
        else:
            mx=x
            Mx=x+1
        if(y==-1):
            my=0
            My=3
        else:
            my=y
            My=y+1
        for i in range( mx , Mx ):
            for j in range( my , My ):
                self.checkerboard[i][j].clear()
    
    # check if the current move causes a match win
    def checkWin(self,x,y,playerID=-1):
        if (playerID==-1):
            playerID = self.currPlayer
        sum = 0
        for i in range(3):  # horizontal ckeck
            if self.checkerboard[x][i].status!=playerID:
                break
            else:
                sum += self.checkerboard[x][i].status
        if(sum==3*playerID):
            return True
        sum = 0
        for i in range(3):  # vertical ckeck
            if self.checkerboard[i][y].status!=playerID:
                break
            else:
                sum += self.checkerboard[i][y].status
        if(sum==3*playerID):
            return True
        if( (x+y)%2!=0 ):
            return False
        sum = 0
        for i in range(3):  # forward-slash ckeck
            if self.checkerboard[i][i].status!=playerID:
                break
            else:
                sum += self.checkerboard[i][i].status
        if(sum==3*playerID):
            return True
        sum = 0
        for i in range(3):  # backslash ckeck
            if self.checkerboard[2-i][i].status!=playerID:
                break
            else:
                sum += self.checkerboard[2-i][i].status
        return sum==3*playerID 

    # prints the status of the checkerboard
    def printStatus(self):
        s = ""
        for i in range(3):
            for j in range(3):
                s += " " + str(self.checkerboard[i][j].status)
            s += "\n"
        print(s)

    # sets a sign on the checkerboard depending on the current player
    def writeOnCheckerboard(self,x,y): 
        playerID = 3-self.currPlayer 
        targetStr = "r"+str(x)+"c"+str(y)
        if(x<0 or x>2 or y<0 or y>2 or (self.ids[targetStr].text == "X") or (self.ids[targetStr].text == "O")):
            return False
        if (playerID==1):
            self.ids[targetStr].text = "X"
        elif (playerID==2):
            self.ids[targetStr].text = "O"
        else:
            return False
        return True
        

# player1 = 1
# player2 = 2
# chk = Checkerboard()
# chk.assign(0, 0, player1)
# chk.assign(2, 2, player1)
# chk.assign(1, 0, player1)
# for i in range(0,3):
#     for j in range(0,3):
#         toClear = chk.checkerboard[i][j].status==0
#         win = chk.assign(i, j, player1)
#         chk.printStatus()
#         print(win,"\n----")
#         if(toClear):
#             chk.clear(i,j)

# chk.assign(0, 0, player1)
# chk.assign(0, 2, player1)
# chk.assign(1, 2, player1)
# win = chk.assign(2, 2, player1)
# chk.printStatus()
# print(win)