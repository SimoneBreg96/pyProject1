import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
kivy.require('2.1.0') # replace with your current kivy version !

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue =  [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class BoxLayoutApp(App):
    def build(self):
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets 
        superBox = BoxLayout(orientation ='vertical')
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation ='horizontal')
        colors = [red, green, blue, purple]

        # styling the button boxlayout
        btn1 = Button(text ="One", background_color = random.choice(colors), font_size = 32, size_hint =(0.7, 1))
        btn2 = Button(text ="Two", background_color = random.choice(colors), font_size = 32, size_hint =(0.7, 1))

        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(btn1)
        HB.add_widget(btn2)

        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = BoxLayout(orientation ='vertical')

        btn3 = Button(text ="Three", background_color = random.choice(colors), font_size = 32, size_hint =(1, 10))
        btn4 = Button(text ="Four", background_color = random.choice(colors), font_size = 32, size_hint =(1, 15))

        # VB represents the vertical boxlayout orientation
        # declared above
        VB.add_widget(btn3)
        VB.add_widget(btn4)

        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox