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

def properAssign(r,c,r_prev,c_prev):
        if(r==r_prev):
            return abs(c-c_prev)==3
        if(c==c_prev):
            return abs(r-r_prev)==3
        return abs(c-c_prev)==2 and abs(r-r_prev)==2


class Square:
    def __init__(self,r,c):
        self.set(r,c,0)

    def set(self,r,c,v):
        self.status = v
        self.r = r
        self.c = c

class Square100(Screen):
    def __init__(self,**kwargs):
        super().__init__()
        self.count = 1
        self.checkerboard = []
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(Square(i,j))
            self.checkerboard.append(temp)
        self.curr = Square(0,0)
        self.history = []

    def assign(self,r,c):
        r_prev = self.curr.r
        c_prev = self.curr.c
        if(self.checkerboard[r][c].status!=0 or (not properAssign(r,c,r_prev,c_prev) and self.count>1)):
            return False
        self.checkerboard[r][c].status = self.count
        self.curr.set(r,c,self.count)
        history = [r,c]
        self.history.append(history)
        self.count += 1
        if(self.count>100):
            self.ids["r"+str(r)+"c"+str(c)].color = [0,1,0]
        self.ids["r"+str(r)+"c"+str(c)].text = str(self.count-1)
        return True

    def clear(self):
        self.count = 1
        self.curr.r = 0
        self.curr.c = 0
        for i in range(10):
            for j in range(10):
                self.checkerboard[i][j].status = 0
                self.ids["r"+str(i)+"c"+str(j)].text = ""
        self.history = []

    def prevMove(self):
        if(self.count<=1):
            return False
        self.checkerboard[self.curr.r][self.curr.c].status = 0
        self.ids["r"+str(self.curr.r)+"c"+str(self.curr.c)].text = ""
        self.count -= 1
        self.history.pop()
        if(self.history!=[]):
            prev = self.history[-1]
        else:
            prev = [0,0]
        self.curr.r = prev[0]
        self.curr.c = prev[1]
        return True
    
    