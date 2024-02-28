from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class NewEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'new_entry_screen'
        self.orientation = "vertical"
        self.spacing = 5  # Reduced spacing between widgets
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        self.background = Image(source="NewEntry.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        # Add a BoxLayout to hold text input fields dynamically
        self.text_input_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(None, None), size=(400, 300))
        self.text_input_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(self.text_input_layout)

        # Add text input fields for "Tank ID," "Tank Size," and "Total Fish" with labels and placeholders
        self.add_labeled_text_input("Tank ID", "Enter Tank ID")
        self.add_labeled_text_input("Tank Size", "Enter Tank Size")
        self.add_labeled_text_input("Total Fish", "Enter Total Fish")

        # Add some space between the last text input and the submit button
        self.text_input_layout.add_widget(Label(size_hint_y=None, height=20))

        # Add a submit button
        submit_button = Button(text='Submit', size_hint=(None, None), size=(120, 40), pos_hint={'center_x': 0.75})
        submit_button.bind(on_press=self.submit_form)
        self.text_input_layout.add_widget(submit_button)
    
        # Add a back button
        back_button = Button(text='Back', size_hint=(None, None), size=(120, 40), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

    def add_labeled_text_input(self, label_text, placeholder_text):
        # Helper method to add a labeled text input field with a placeholder
        label = Label(text=label_text, halign='right', valign='middle', size_hint=(None, None), height=30, width=150)
        text_input = TextInput(multiline=False, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5},
                               hint_text=placeholder_text)

        # Set the background color of the text input field to be translucent
        text_input.background_color = (1, 1, 1, 0.5)  # Adjust the last value (alpha) for transparency
        
        # Set the color of the placeholder text to black
        text_input.hint_text_color = (0, 0, 0, 1)  # Black color
        
        # Create a horizontal BoxLayout for each label-text_input pair
        box_layout = BoxLayout(orientation='horizontal', spacing=10)
        box_layout.add_widget(label)
        box_layout.add_widget(text_input)

        self.text_input_layout.add_widget(box_layout)

    def submit_form(self, instance):
        # Add functionality to handle form submission (e.g., save data)
        # Access entered data from each text input field in the layout
        for box_layout in self.text_input_layout.children:
            label = box_layout.children[0]
            text_input = box_layout.children[1]
            print(f"{label.text}: {text_input.text}")

    def go_back(self, instance):
        # Add functionality to navigate back to the homepage
        # For example, you can use the ScreenManager to switch screens
        self.manager.current = 'home_screen'
