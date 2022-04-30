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
import random
import time

class C5Team(Screen):
    def __init__(self,**kwargs):
        super().__init__()
        self.time = 0
        self.t0 = 0
        self.duration = 0
        self.isRunning = False
        self.precision = 0

    def start(self,duration=3600,precision=1):
        self.reset()
        self.duration = duration
        self.precision = precision
        self.isRunning = True
        self.time = 0
        Clock.schedule_interval(self.count, self.precision)
    
    def count(self,dt):
        self.time = self.time+self.precision
        self.ids.clockLabel.text = str(self.time)

    def stop(self):
        Clock.unschedule(self.count)

    def reset(self):
        self.t0 = 0
        self.time = 0