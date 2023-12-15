from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from pymongo import MongoClient
from Login_Screen import LoginScreen
from Signup_Screen import SignupScreen
from Home_Screen import HomeScreen
import Data_Base

class LoginSignupApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(SignupScreen())
        sm.add_widget(HomeScreen())
        return sm


if __name__ == "__main__":
    LoginSignupApp().run()