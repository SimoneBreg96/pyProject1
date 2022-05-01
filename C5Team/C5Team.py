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