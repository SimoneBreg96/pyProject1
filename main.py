# I have disabled Pylance VS extension..
import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
from widgets import BoxLayoutApp


class MyApp(App):
    def build(self):
        return MainWindow()


BoxLayoutApp().run()