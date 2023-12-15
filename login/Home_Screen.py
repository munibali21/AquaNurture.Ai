from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from pymongo import MongoClient
from Signup_Screen import SignupScreen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Adding background image for the home screen
        self.background = Image(source="home_image.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        home_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(300, 300),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})

        title = Label(text="Welcome Home!", font_size=40, size_hint_y=None, height=40, font_name='times', bold=True)
        home_layout.add_widget(title)

        home_button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 40), spacing=10)
        home_button_layout.pos_hint = {'center_x': 0.5}  # Centering the buttons horizontally

        home_button = Button(text="Home")
        # Add functionality for the home button here

        contact_us_button = Button(text="Contact Us")
        # Add functionality for the contact us button here

        help_button = Button(text="Help")
        # Add functionality for the help button here

        home_button_layout.add_widget(home_button)
        home_button_layout.add_widget(contact_us_button)
        home_button_layout.add_widget(help_button)

        home_layout.add_widget(home_button_layout)

        self.add_widget(home_layout)
