import kivy 
import random
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition, SwapTransition
from kivy.properties import StringProperty
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        print("Sign up button clicked.")
        self.manager.current = "sign_up_screen"
    
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users.keys():
            if users[username]["password"] == password:
                self.manager.current = "login_screen_success"
                self.manager.transition = SlideTransition(direction="left")
            else:
                self.ids.title.text = "Password is incorrect!"
        else:
            self.ids.title.text = f"There is no user {username}"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        print(username, password)
        with open("users.json") as file:
            users = json.load(file)
            print(users)
        users[username] = {
                "username": username,
                "password": password,
                "created": datetime.now().strftime("%Y-%M-%D %H-%M-%S")
            }
        print(users)
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.transition = SlideTransition()
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        # self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.current = "login_screen"
    def quote_generator(self, mood_file):      # read file given in function parameter
        with open(f"quotes/{mood_file}") as file:
            quotes = file.read()
        quotes_split = quotes.splitlines() # splitting text by new lines
        # quotes_len = len(quotes_split)-1        
        # random_int = random.randint(0, quotes_len) # create random int based on quotes_split length
        self.ids.quote_label.text = random.choice(quotes_split)

# one way to add widgets
# class RootWidget(ScreenManager):
#     def __init__(self):
#         self.transition = SlideTransition()

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(SignUpScreen(name="sign_up_screen")) 
sm.add_widget(SignUpScreenSuccess(name="sign_up_screen_success"))
sm.add_widget(LoginScreenSuccess(name="login_screen_success"))
class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()