from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string
db = client["login_page"]  # Create or use the signup_db database
users_collection = db["login_signup"]  # Create a collection named users for storing signup data

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
        # Authentication logic (placeholder)
        print(f"Login with username: {username} and password: {password}")

    def go_to_signup(self, instance):
        self.manager.current = 'signup_screen'

# ... (Previous code remains unchanged)

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'signup_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Adding background image for signup screen
        self.background = Image(source="images (11).jpeg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        signup_layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), size=(300, 300),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})
        signup_layout.bind(minimum_size=signup_layout.setter('size'))

        title = Label(text="Signup Page", font_size=40, size_hint_y=None, height=40, font_name='times', bold=True)
        signup_layout.add_widget(title)

        # Add signup input fields and buttons similar to login screen
        signup_input_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=200)

        # Customize input fields' background color
        input_background_color = (1, 1, 1, 0.7)  # Transparent color (black with alpha 0)

        self.signup_username_input = TextInput(
            hint_text="First name", multiline=False, size_hint_y=None, height=40,
            background_color=input_background_color,  # Set background color
            hint_text_color=[0, 0, 0, 1]  # Set hint text color to white
#white:[1111]
#black[0,0,0,1]
        )
        signup_input_layout.add_widget(self.signup_username_input)

        self.signup_lastname_input = TextInput(
            hint_text="Last name", multiline=False, size_hint_y=None, height=40,
            background_color=input_background_color, # Set background color
            hint_text_color=[0, 0, 0, 1]  # Set hint text color to white

        )
        signup_input_layout.add_widget(self.signup_lastname_input)

        self.signup_email_input = TextInput(
            hint_text="Email", multiline=False, size_hint_y=None, height=40,
            background_color=input_background_color,  # Set background color
            hint_text_color=[0, 0, 0, 1]  # Set hint text color to white

        )
        signup_input_layout.add_widget(self.signup_email_input)

        self.signup_password_input = TextInput(
            hint_text="Password", password=True, multiline=False, size_hint_y=None, height=40,
            background_color=input_background_color,  # Set background color
            hint_text_color=[0, 0, 0, 1]  # Set hint text color to white

        )
        signup_input_layout.add_widget(self.signup_password_input)

        signup_layout.add_widget(signup_input_layout)

        signup_button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 40), spacing=10)
        signup_button_layout.pos_hint = {'center_x': 0.5}  # Centering the buttons horizontally

        self.create_account_button = Button(text="Create Account")
        self.create_account_button.bind(on_press=self.create_account)
        self.create_account_button.font_name = 'times'  # Setting font for the create account button
        signup_button_layout.add_widget(self.create_account_button)

        signup_layout.add_widget(signup_button_layout)

        self.add_widget(signup_layout)

    def create_account(self, instance):
        username = self.signup_username_input.text
        password = self.signup_password_input.text
        last_name = self.signup_lastname_input.text
        email = self.signup_email_input.text
        # Signup logic (placeholder)
        print(f"Create account with username: {username} and password: {password}")
        
        # Insert signup data into the users collection
        user_data = {
            "username": username,
            "password": password,
            "last_name": last_name,
            "email": email
        }
        users_collection.insert_one(user_data)
        print(f"Account created for username: {username}")


class LoginSignupApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(SignupScreen())
        return sm


if __name__ == "__main__":
    LoginSignupApp().run()
