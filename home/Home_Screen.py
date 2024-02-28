from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CircularMaskImage(BoxLayout):
    pass


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Adding background image for the home screen
        self.background = Image(source="home.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        # Logo and Logout button layout
        top_layout2 = BoxLayout(orientation='horizontal', size_hint=(None, None), height=40,
                               pos_hint={'top': 0.93, 'left': 0.98})

        top_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), height=40,
                              pos_hint={'top': 0.85, 'left': 0.98})

        top_layout1 = BoxLayout(orientation='vertical',spacing=10, size_hint=(None, None), height=40,
                                pos_hint={'top': 0.7, 'right': 0.95})

        # Add the circular logo image to the top-left corner
        logo = CircularMaskImage(size_hint=(None, None), size=(70, 70))
        logo.add_widget(AsyncImage(source="logo.png", size=(80, 80), allow_stretch=True))
        top_layout2.add_widget(logo)

        # Add three buttons on the top-right vertically with equal margin
        contact_button = Button(text="Contact", size_hint=(None, None), size=(150, 50),
                        background_color=(0, 0.5, 1, 1), color=(1, 1, 1, 1))

        help_button = Button(text="Help", size_hint=(None, None), size=(150, 50),background_color=(0, 0.5, 1, 1),
                     color=(1, 1, 1, 1))
        scan_button = Button(text="Scan", size_hint=(None, None), size=(150, 50),background_color=(0, 0.5, 1, 1),
                     color=(1, 1, 1, 1))
        logout_button = Button(text="Logout", size_hint=(None, None), size=(150, 50),background_color=(0, 0.5, 1, 1),
                     color=(1, 1, 1, 1))
        
        # Bind the on_press event to go_to_login_or_signup method
        logout_button.bind(on_press=self.go_to_login_or_signup)

        # Equal margin between buttons
        margin_size = 10
        top_layout1.add_widget(logout_button)
        top_layout1.add_widget(Label(size_hint_y=None, height=margin_size))
        top_layout1.add_widget(contact_button)
        top_layout1.add_widget(Label(size_hint_y=None, height=margin_size))
        top_layout1.add_widget(help_button)
        top_layout1.add_widget(Label(size_hint_y=None, height=margin_size))
        top_layout1.add_widget(scan_button)

        self.add_widget(top_layout)
        self.add_widget(top_layout1)
        self.add_widget(top_layout2)

        # Central transparent square box with a plus button
        center_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(200, 200),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})

        with center_layout.canvas.before:
            Color(0, 0, 0, 0.5)  # Transparent black color
            Rectangle(pos=center_layout.pos, size=center_layout.size)

        plus_button = Button(text="+", size_hint=(None, None), size=(50, 50),background_color=(0, 0.5, 1, 1),
                     color=(1, 1, 1, 1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        plus_button.bind(on_press=self.on_plus_button_press)

        center_layout.add_widget(plus_button)
        self.add_widget(center_layout)

    def go_to_login_or_signup(self, instance):
        # Add your conditions here to decide whether to go to login or signup
        # For now, let's assume you want to go to the login screen
        self.manager.current = 'login_screen'

    def on_plus_button_press(self, instance):
        # Handle the plus button press by switching to the NewEntryScreen
        self.manager.current = 'new_entry_screen'
