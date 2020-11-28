# APIT to aplhavantage.com FD6O0TA1HD6WBYR4.

import kivy 
import random
import json
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition, SwapTransition
from kivy.properties import StringProperty
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()