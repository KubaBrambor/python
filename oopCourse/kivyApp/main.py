import kivy 
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        print("Sign up button clicked.")
        self.manager.current = "sign_up_screen"

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
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"

# one way to add widgets
# class RootWidget(ScreenManager):
#     def __init__(self):
#         self.transition = SlideTransition()

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(SignUpScreen(name="sign_up_screen")) 
sm.add_widget(SignUpScreenSuccess(name="sign_up_screen_success"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()