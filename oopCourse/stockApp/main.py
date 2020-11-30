# APIT to aplhavantage.com FD6O0TA1HD6WBYR4.
# https://www.alphavantage.co/documentation/#

import kivy, random, json, requests
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
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users.keys():
            if users[username]['password'] == password:
                self.manager.current = "main_screen"
            else:
                self.ids.login_title.text = "Wrong password!"
        else:
            self.ids.login_title.text = f"There is no user {username}"

class MainScreen(Screen):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=FD6O0TA1HD6WBYR4."
    r = requests.get(url)
    data = r.json()
    def showStock(self):
        print(self.data)

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(MainScreen(name="main_screen"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()