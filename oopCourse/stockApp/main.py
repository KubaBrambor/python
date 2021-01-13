# APIT to aplhavantage.com FD6O0TA1HD6WBYR4 oraz WAQH56GFEZKK7U8W
# https://www.alphavantage.co/documentation/#
# News Api key d360d65bebb442afbf30ca5cee551b8c
import kivy, random, json, requests
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition, SwapTransition
from kivy.properties import StringProperty
from hoverable import HoverBehavior
from kivy.uix.image import Image, AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
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
        #stare
        #Layout one with navi buttons
        # gridNavi = GridLayout(cols=3)
        # gridNavi.add_widget(Button(text="Your stocks"))
        # gridNavi.add_widget(Button(text="Find stock"))
        # gridNavi.add_widget(Button(text="Wallet"))

        newsTextList = []
        def line(self):
            with self.canvas:
                Line(points=(0, 1, 2, 3, 4, 5))
                Color(1, 0, 0, .5, mode='rgba')
                Rectangle(pos=self.pos, size=self.size)

        for i in range(len(self.data['articles'])):
            newsTextList.append("[b][u][size=25]" + self.data['articles'][i]['title'] + "[/size][/u][/b]" + "\n" + \
                        "[i][size=12]" + "source: " + self.data['articles'][i]['source']['name'] + "[/size][/i]" + "\n" + \
                        "[size=20][color=#A8A8A8]" + self.data['articles'][i]['description'] + "[/color][/size]" + "\n \n \n")
        
        newsText = " ".join(newsTextList)
        print(newsText)
        self.ids.gridNews.text = newsText

        #stare, nie działało do końca
        #Layout two with stock 
        # gridNews = GridLayout(cols=1, size_hint_y=None, padding=(50,50))
        # gridNews.bind(minimum_height=gridNews.setter('height'))
        # for i in range(len(self.data['articles'])):
        #     gridNews.add_widget(Label(text=self.data['articles'][i]['title'], size_hint_y=None, size=(900,80), text_size=(200, None), font_size="20sp"))
        #     gridNews.add_widget(Label(text=self.data['articles'][i]['source']['name'], size_hint_y=None, size=(900,30), text_size=(200, None), font_size="10sp"))
        #     gridNews.add_widget(Label(padding=(5,50),text=self.data['articles'][i]['description'], size_hint_y=None, size=(900,200), text_size=(200, None), font_size="15sp"))
            
            # gridNews.add_widget(Widget(canvas=(Line(points=(0, 1, 2, 3, 4, 5)),Color(1, 0, 0, .5, mode='rgba'))))
            # gridNews.add_widget(Button(text="Go to", on_press=lambda x: print(self.data['articles'][i])))
            
        scrollviewNews = ScrollView(size_hint=(1, None),size=(Window.width, Window.height))
        # scrollviewNews.add_widget(gridNews)
        # gridNavi.add_widget(scrollviewNews)
       
        # self.add_widget(gridNavi)
    
    def showStock(self):
        print(self.data['articles'][0])
        print(len(self.data['articles']))

    def build_label(self, text):
        label = Label(text=text)
        return label

    def findStock(self):
        self.manager.current = "findStock_screen"

class FindStockScreen(Screen):
    def mainScreen(self):
        self.manager.current = "main_screen"
    
    def searchForStocks(self, searchText):
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={searchText}&apikey=WAQH56GFEZKK7U8W"
        r = requests.get(url)
        data = r.json()
        print(data)


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

# class HoverButton(Button, HoverBehavior):
#     pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(MainScreen(name="main_screen"))
sm.add_widget(FindStockScreen(name="findStock_screen"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()