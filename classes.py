import configparser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
import win32clipboard
import keyboard as key
from threading import Thread
import pyttsx3
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineAvatarListItem, MDList


class Menu(Screen):

    def reader_engine(self):
        engine = pyttsx3.init()
        text = self.root.get_screen('menu').ids.text_field.text
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume - 0.6)
        engine.say(text)
        engine.startLoop()
        engine.stop()

    def listener(self): #Only works on first try
        print('listener thread JOINED')
        config = configparser.ConfigParser()
        config.read('settings.ini')
        screen_reader = config.get('SETTINGS', 'screen_reader')

        while True:
            if key.is_pressed('r') and screen_reader == 'on':
                win32clipboard.OpenClipboard()
                c = win32clipboard.GetClipboardData()
                win32clipboard.EmptyClipboard()
                c = c.replace('\n', ' ')
                c = c.replace('\r', ' ')
                while c.find('  ') != -1:
                    c = c.replace('  ', ' ')
                win32clipboard.SetClipboardText(c)
                win32clipboard.CloseClipboard()
                engine = pyttsx3.init()
                volume = engine.getProperty('volume')
                engine.setProperty('volume', volume - 0.6)
                engine.say(c)
                engine.startLoop()
                engine.endLoop()
                break

    def set_to_default(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        config.set('SETTINGS', 'screen_reader', 'off')
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()

    def reader_state(self, value, checkbox):
        if checkbox:
            print('on')
            self.root.get_screen('menu').ids.helper_text.text = f"Screen reader On"
            config = configparser.ConfigParser()
            config.read('settings.ini')
            config.set('SETTINGS', 'screen_reader', 'on')
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
                configfile.close()

        else:
            print('off')
            self.root.get_screen('menu').ids.helper_text.text = f"Screen reader Off"
            config = configparser.ConfigParser()
            config.read('settings.ini')
            config.set('SETTINGS', 'screen_reader', 'off')
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
                configfile.close()

    def speech_output(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        screen_reader = config.get('SETTINGS', 'screen_reader')

        if screen_reader == 'on':
            announce = Thread(target=self.reader_engine)
            announce.start()

        if screen_reader == 'off':
            pass

    def start_listener(self):
        listener = Thread(target=self.listener)
        listener.start()


class ContentNavigationDrawer(BoxLayout):
    pass


class Content(BoxLayout):
    pass



class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class SavedTexts(Screen):
    def load_saved_texts(self):
        pass

    def add_entry(self):
        title = self.dialog.content_cls.ids.Title.text
        subtitle = self.dialog.content_cls.ids.SubTitle.text

        self.root.get_screen('saved_texts').ids.container.add_widget(
            TwoLineAvatarListItem(
                text=f"{title}",
                secondary_text=f"{subtitle}",
            ))

    def add_entry_popup(self):
        self.dialog = MDDialog(
            title="Add a new Saved Text:",
            type="custom",
            content_cls=Content(),
            buttons=[
                MDFlatButton(
                    text="Create text",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=lambda _: self.add_entry(),
                    on_release=lambda _: self.dialog.dismiss(),
                ),
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda _: self.dialog.dismiss(),
                ),
            ],
        )
        self.dialog.open()
