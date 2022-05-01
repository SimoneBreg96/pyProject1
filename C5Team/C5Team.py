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
from kivy.clock import Clock
import pandas as pd
import math
import time

def timeTransform(t,prec=2):
    m = math.floor(t/60)
    s = t-m*60
    return [round(m,prec),round(s,prec)]

class C5Team(Screen):
    def __init__(self,**kwargs):
        super().__init__()
        self.time = 0
        self.duration = 0
        self.isRunning = False
        self.precision = 0

    def start(self,duration=3600,precision=1):
        self.duration = duration
        self.precision = precision
        self.isRunning = True
        self.printTime()
        Clock.schedule_interval(self.count, self.precision)
    
    def count(self,dt):
        self.time = self.time+self.precision
        self.printTime()

    def stop(self):
        Clock.unschedule(self.count)

    def reset(self):
        self.time = 0
        self.printTime()
    
    def printTime(self):
        T = timeTransform(self.time)
        self.ids.clockLabel.text = str(T[0])+"' "+str(100+T[1])[1:3]+"''"
    
    def readExc(self):
        data = pd.read_excel('C5Team//Torneo2021.xlsx')
        i = 1
        Ginew = Team()
        while( not pd.isna(data.values[i][2]) ):
            Ginew.addPlayer(Player(data.values[i][2]))
            i += 1
        turns_r0 = 1
        turns_c0 = 3
        turns = []
        for r in range(0,Ginew.getNumPlayers()):
            turns.append( data.values[turns_r0+r][turns_c0+1:turns_c0+Ginew.getNumPlayers()+1] )
        Ginew.setTurns(turns)
        for i in Ginew.enteringPlayers(2):
            print(i.getName())
        for i in Ginew.leavingPlayers(2):
            print(i.getName())

# Player definition
class Player:
    ID = 1
    def __init__(self,name="",turns=[]):
        self.name = ""
        self.turns = []
        if(name==""):
            self.name = "Player" + str(Player.ID)
            Player.ID += 1
        else:
            for i in name:
                if (not i=="\""):
                    self.name += i
            self.setTurns(turns)
    
    def setName(self,name):
        if(name==""):
            self.name = "Player" + str(Player.ID)
            Player.ID += 1
        else:
            self.name = str(name)

    def setTurns(self,turns):
        self.turns = []
        for i in range(0,len(turns)):
            self.turns.append( not pd.isna(turns[i]) )

    def getName(self):
        return str(self.name)

    def getTurns(self):
        return self.turns

    def isPlayingTurn(self,turn):
        return self.turns[turn]

# Team definition
class Team:
    def __init__(self,players=[]):
        self.players = []
        self.numPlayers = len(players)
        for i in range(0,self.numPlayers):
            self.players.append(Player(player[i]))
        self.turnMatrix = []
        turns = []
        for r in range(0,self.numPlayers):
            for c in range(0,self.numPlayers):
                turns.append(False)
            self.turnMatrix.append(turns)
            turns = []
    
    def addPlayer(self,player):
        self.players.append(player)
        self.numPlayers += 1
    
    def printPlayers(self):
        for i in self.players:
            print(i.getName())
    
    def getNumPlayers(self):
        return self.numPlayers
    
    def setTurns(self,turns,name=""):
        if(name==""):
            for i in range(0,self.numPlayers):
                self.players[i].setTurns(turns[i])
                self.turnMatrix.append(self.players[i].getTurns())
        else:
            if(self.searchPlayer(name)[0]):
                index = self.searchPlayer(name)[1]
                self.turnMatrix[ index ] = self.players[index].getTurns()
    
    def getTurns(self):
        return self.turnMatrix
    
    def searchPlayer(self,name):
        for i in range(0,self.numPlayers):
            if (self.players[i].getName()==name):
                return [True , i ]
        return [False , -1]

    def getPlayersForTurn(self,turn):
        if(turn<0 or turn>=self.numPlayers):
            print("Error: invalid turn input")
            return 0
        players = []
        for i in self.players:
            if(i.isPlayingTurn(turn)):
                players.append(i)
        return players
    
    def enteringPlayers(self,turn):
        currPlayers = self.getPlayersForTurn(turn)
        nextPlayers = self.getPlayersForTurn(turn+1)
        playersIn = []
        for i in nextPlayers:
            if (i not in currPlayers):
                playersIn.append(i)
        return playersIn
    
    def leavingPlayers(self,turn):
        currPlayers = self.getPlayersForTurn(turn)
        nextPlayers = self.getPlayersForTurn(turn+1)
        playersOut = []
        for i in currPlayers:
            if (i not in nextPlayers):
                playersOut.append(i)
        return playersOut