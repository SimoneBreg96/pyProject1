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
        i = 0
        Ginew = Team()
        while( not pd.isna(data.values[i+1][2]) ):
            Ginew.addPlayer(Player(data.values[i+1][2]))
            i += 1
        Ginew.printPlayers()


# Player definition
class Player:
    ID = 1
    def __init__(self,name="",turns=[]):
        if(name==""):
            self.name = "Player" + str(Player.ID)
            Player.ID += 1
        else:
            self.name = name
            self.turns = turns
    
    def setName(self,name):
        if(name==""):
            self.name = "Player" + str(Player.ID)
            Player.ID += 1
        else:
            self.name = name

    def setTurns(self,turns):
        self.turns = turns

    def getName(self):
        return self.name

    def getTurns(self):
        return self.turns

# Team definition
class Team:
    def __init__(self,players=[]):
        self.players = []
        self.numPlayers = len(players)
        for i in range(0,self.numPlayers):
            self.players.append(Player(player[i]))
    
    def addPlayer(self,player):
        self.players.append(player)
    
    def printPlayers(self):
        for i in self.players:
            print(i.getName())