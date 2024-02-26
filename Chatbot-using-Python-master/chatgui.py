from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
import json
import random
import numpy as np
import pickle

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: 10  # Adjust the spacing between widgets
    padding: 20  # Add padding around the entire window
    canvas.before:
        Color:
            rgba: 0.2, 0.2, 0.2, 1  # Set background color to dark gray
        Rectangle:
            pos: self.pos
            size: self.size

    MDScreen:

        MDScrollView:

            BoxLayout:
                orientation: 'vertical'
                spacing: 10  # Adjust the spacing between chat log and user input

                MDLabel:
                    id: chat_log
                    text: ''
                    markup: True
                    size_hint_y: None
                    height: self.texture_size[1]
                    color: 1, 1, 1, 1  # Set text color to white
                    padding: 10, 10  # Add margin around the text
                    spacing: 10  # Add margin around the chat log

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: "56dp"
                    padding: 10  # Add margin around the entire box

                    MDTextField:
                        id: user_input
                        hint_text: "Type your message"
                        helper_text: "Press Enter to send"
                        helper_text_mode: "on_focus"
                        multiline: False
                        foreground_color: 1, 1, 1, 1  # Set text color to white
                        size_hint_x: 0.85

                    MDRaisedButton:
                        text: "Send"
                        size_hint_x: 0.15
                        on_press: app.send_message()
                        padding: 10  # Add margin around the button

'''

class ChatBotApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def send_message(self):
        user_message = self.root.ids.user_input.text.strip()
        self.root.ids.user_input.text = ""

        if user_message:
            bot_response = self.chatbot_response(user_message)

            # Update chat log
            chat_log = self.root.ids.chat_log
            chat_log.text += f"[b]You:[/b] {user_message}\n"
            chat_log.text += f"[b]Bot:[/b] {bot_response}\n"
            chat_log.height = chat_log.texture_size[1]

    def chatbot_response(self, msg):
        p = self.bow(msg, words)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []

        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})

        tag = return_list[0]['intent']
        list_of_intents = intents['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break

        return result

    def bow(self, sentence, words):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)

        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1

        return np.array(bag)

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words


if __name__ == '__main__':
    ChatBotApp().run()
