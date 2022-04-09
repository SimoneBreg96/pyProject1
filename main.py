# I have disabled Pylance VS extension..
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
kivy.require('2.1.0') # replace with your current kivy version !

class MainWindow(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MainWindow()


MyApp().run()