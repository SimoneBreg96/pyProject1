# I have disabled Pylance VS extension..
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
from functionsRepository1 import *
import TipTapToe.TipTapToe
import Square100.Square100

class MainWindow(BoxLayout,Screen):
    pass

class FuelCost(BoxLayout,Screen):
    submit_button = ObjectProperty(None)
    result = ObjectProperty(None)

    def btn_clk(self):
        distance = self.ids.distance.text
        cost = self.ids.cost.text
        consumption = self.ids.consumption.text
        passengers = self.ids.passengers.text
        if (distance=="" or cost=="" or consumption==""):
            self.result.text = "Enter something!"
            return 0
        if(not(isfloat(distance)) or not(isfloat(cost)) or not(isfloat(consumption))):
            self.result.text = "Only numbers are accepted as inputs!"
            return 0
        x = fuelPrice(float(distance),float(cost),float(consumption))/float(passengers)
        if(x<=0):
            self.result.text = "Invalid input!"
            return 0
        self.result.text = str(x)
        return 0
    
    def clear(self):
        self.distance.text = ""
        self.cost.text = ""
        self.consumption.text = ""
        self.result.text = ""
        self.ids.passengers.text = self.ids.passengers.values[0]

class TipTapToe(Screen):
    pass
class Square100(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mainpage.kv")

class MainPage(App):
    def build(self):
        return kv

MainPage().run()