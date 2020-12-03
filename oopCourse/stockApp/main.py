# APIT to aplhavantage.com FD6O0TA1HD6WBYR4.
# https://www.alphavantage.co/documentation/#
# News Api key d360d65bebb442afbf30ca5cee551b8c
import kivy, random, json, requests
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition, SwapTransition
from kivy.properties import StringProperty
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
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
    time = datetime.now().strftime("%Y-%m-d%")
    url = f'https://newsapi.org/v2/top-headlines?q=market&from={time}&apiKey=d360d65bebb442afbf30ca5cee551b8c'
    r = requests.get(url)
    data = r.json()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Layout one with navi buttons
        gridNavi = GridLayout(cols=3)
        gridNavi.add_widget(Button(text="Your stocks"))
        gridNavi.add_widget(Button(text="Find stock"))
        gridNavi.add_widget(Button(text="Wallet"))
        
        #Layout two with stock 
        gridNews = GridLayout(cols=1, size_hint_y=None)
        gridNews.bind(minimum_height=gridNews.setter('height'))
        for i in range(len(self.data['articles'])):
            gridNews.add_widget(Label(text=self.data['articles'][i]['title'], size_hint_y=None))
            gridNews.add_widget(Label(text=self.data['articles'][i]['description'], size_hint_y=None))
            gridNews.add_widget(Button(text="Go to", on_press=print("ok")))
            # self.build_label(self.data['articles'][i]['title'])
            # self.build_label(self.data['articles'][i]['description'])
        scrollviewNews = ScrollView(size_hint=(1, None),size=(Window.width, Window.height))
        scrollviewNews.add_widget(gridNews)
        gridNavi.add_widget(scrollviewNews)
       
        self.add_widget(gridNavi)
    
    def showStock(self):
        print(self.data['articles'][0])
        print(len(self.data['articles']))

    def build_label(self, text):
        label = Label(text=text)
        return label
    

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