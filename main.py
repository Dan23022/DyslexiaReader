from kivy.clock import mainthread

from styling import *
from classes import *
from kivy.lang import Builder
from kivymd.app import MDApp


class Dyslexia_Reader(

    MDApp, Menu, SavedTexts, Content,

):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = 'A700'
        screen = Builder.load_string(styling)
        return screen

    def on_start(self):
        #self.start_listener()
        self.set_to_default()


if __name__ == "__main__":
    Dyslexia_Reader().run()
