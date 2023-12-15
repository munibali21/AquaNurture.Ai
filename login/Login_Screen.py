from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import Data_Base as db
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Adding background image
        self.background = Image(source="fish2.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        main_layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), size=(300, 300),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.5})
        main_layout.bind(minimum_size=main_layout.setter('size'))

        title = Label(text="Login or Signup", font_size=40, size_hint_y=None, height=40, font_name='times',
                      color='white', bold=True)
        main_layout.add_widget(title)

        input_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=80)

        self.username_input = TextInput(hint_text="Username", multiline=False, size_hint_y=None, height=40,hint_text_color=[0,0,0,1])
        self.username_input.foreground_color = [0, 0, 0, 1]  # Setting text color to white (for transparent input fields)
        self.username_input.background_color = [1, 1, 1, 0.7]  # Setting background color to transparent (for transparent input fields)
        input_layout.add_widget(self.username_input)
        

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False, size_hint_y=None,height=40,hint_text_color=[0,0,0,1])
        self.password_input.foreground_color = [0, 0, 0, 1]  # Setting text color to white (for transparent input fields)
        self.password_input.background_color = [1, 1, 1, 0.7]# Setting background color to transparent (for transparent input fields)

        input_layout.add_widget(self.password_input)

        main_layout.add_widget(input_layout)

        button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 40), spacing=10)
        button_layout.pos_hint = {'center_x': 0.5}  # Centering the buttons horizontally

        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.login)
        self.login_button.font_name = 'times'  # Setting font for the login button
        button_layout.add_widget(self.login_button)

        self.signup_button = Button(text="Signup")
        self.signup_button.bind(on_press=self.go_to_signup)  # Go to signup page on press
        self.signup_button.font_name = 'times'  # Setting font for the signup button
        button_layout.add_widget(self.signup_button)

        main_layout.add_widget(button_layout)

        self.add_widget(main_layout)



    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Query the database for the entered username
        user_data = db.users_collection.find_one({"username": username})

        if user_data:  # If username exists in the database
            if user_data["password"] == password:  # Check if the password matches
                print("Correct")
                self.manager.current = 'home_screen' 
            else:
                print("Incorrect Password")
        else:
            print("Username not found")

    def go_to_signup(self, instance):
        self.manager.current = 'signup_screen'
