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
import random
from test import fibonacci


class MainWindow(BoxLayout):
    submit_button = ObjectProperty(None)
    result = ObjectProperty(None)

    def btn_clk(self):
        inputLabel = self.ids.inputLabel.text
        self.lbl.text = str(fibonacci(int(inputLabel)))

class MainPage(App):
    def build(self):
        return MainWindow()

MainPage().run()
# print(fibonacci(10))
# BoxLayoutApp().run()