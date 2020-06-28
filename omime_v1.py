import kivy
import random
import pandas as pd

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#First App tutorial from Erin Forsyth: https://bityli.com/3pUeu (lang: english)
#class MyApp(App):
#    def build(self):
#        return Label(text='Hello World!')
#if __name__ == '__main__':
#    MyApp().run()

#data base from a list of product types displayed on marketplaces
word_list = pd.read_csv('csv/omime_db.csv')

#great playlist from @HashLDash: https://bityli.com/kdtHj (lang: portuguese)
class Mime(App):
    def build(self):
       box = BoxLayout(orientation='vertical')
       button = Button(text='Sortear!', font_size=30, on_release=self.sortear)
       self.label = Label(text='Omime', font_size=30)
       box.add_widget(self.label)
       box.add_widget(button)
       return box

    def sortear(self, button):
        word = random.choice(word_list['product_type'])
        self.label.text = ('Você vai ter que fazer um(a):\n{}!'.format(word))

Mime().run()