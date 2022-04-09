# I have disabled Pylance VS extension..
import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class MainWindow(BoxLayout):
    pass

class MainPage(App):
    def build(self):
        return MainWindow()

MainPage().run()
# BoxLayoutApp().run()