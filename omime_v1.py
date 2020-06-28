import kivy
import random
import pandas as pd

word_list = pd.read_csv('csv/omime_db.csv')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#exemplo First App da Erin Forsyth - https://www.youtube.com/watch?v=huY-SMs5YkY&t=304s
#class MyApp(App):
#    def build(self):
#        return Label(text='Hello World!')
#if __name__ == '__main__':
#    MyApp().run()

class Mime(App):
    def build(self):
       box = BoxLayout(orientation='vertical')
       button = Button(text='Sortear!', font_size=30, on_release=self.incrementar)
       self.label = Label(text='Omime', font_size=30)
       box.add_widget(self.label)
       box.add_widget(button)
       return box

    def incrementar(self, button):
        word = random.choice(word_list['product_type'])
        self.label.text = ('Você vai ter que fazer um(a):\n{}!'.format(word))

Mime().run()