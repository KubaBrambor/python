import kivy 
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, ShaderTransition, SlideTransition

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        print("Sign up button clicked.")
        self.manager.current = "sign_up_screen"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        print(username, password)

# one way to add widgets
# class RootWidget(ScreenManager):
#     def __init__(self):
#         self.transition = SlideTransition()

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login_screen"))
sm.add_widget(SignUpScreen(name="sign_up_screen")) 

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()