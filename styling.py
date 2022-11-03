from classes import *
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager


screen_manager = ScreenManager()
Window.size = (800, 600)
screen_manager.add_widget(Menu(name="menu"))
screen_manager.add_widget(SavedTexts(name="saved_texts"))

styling = """
#:import RGBA kivy.utils.rgba
#:import NoTransition kivy.uix.screenmanager.NoTransition

ScreenManager:
    transition: NoTransition()
    Menu:
    SavedTexts:
 
 
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    unfocus_color: "#f7f4e7"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: "#f7f4e7"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    _no_ripple_effect: True

<Menu>
    name: "menu"
    
    MDFloatLayout:  
    
        MDLabel:
            id: helper_text
            text: "Speech engine off"
            halign: "center"
            pos_hint: {'center_x': .2, 'center_y': .9} 
        
        MDCheckbox:
            id: power_state
            size: "48dp", "48dp"
            size_hint: None,None
            hint_text: "Remember me"
            on_active: app.reader_state(*args)
            pos_hint: {'center_x': .1, 'center_y': .9}  
            
    MDRectangleFlatIconButton:
        icon: "script-text-play-outline"
        text: "Read text"
        md_bg_color: 0, .3, .8, .1
        icon_size: "20sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.16}
        on_release: app.speech_output()
        
    MDFloatLayout:        
        MDTextFieldRect:
            id: text_field
            size_hint_x: .8
            size_hint_y: .6
            hint_text: "Enter text here"
            max_height: "200dp"
            background_color: [1, 0.99, 0.81, 1]
            foreground_color : [0, 0, 1, 1]
            multiline: True
            pos_hint: {"center_x": .5, "center_y": .51}
            font_size : 20
            

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open") if nav_drawer.state == "close" else nav_drawer.set_state("close")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: "#f7f4e7"

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Side Menu"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Main"
                    
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: "#4a4939"
                    text: "Menu"

                DrawerClickableItem:
                    icon: "book"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Saved texts"
                    on_press: root.manager.current = "saved_texts"
    
        
<SavedTexts>
    name: "saved_texts"
    
    MDBoxLayout:    
        orientation: "vertical"
        
        MDBottomNavigation:
            text_color_normal: 1, 1, 1, 1
                
            MDBottomNavigationItem:
                name: "add"
                text: "Add text"
                icon: "book-plus"
                on_tab_release: app.add_entry_popup()
    
    ScrollView:
        size_hint_y: .8
        size_hint_x: 1
        pos_hint: {"center_y": 0.5, "center_x": 0.5}
            
        MDList:
            id: container
            
    
    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open") if nav_drawer.state == "close" else nav_drawer.set_state("close")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: "#f7f4e7"

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Side Menu"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Main"
                    
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: "#4a4939"
                    text: "Menu"
                    on_press: root.manager.current = "menu"
                    on_press: selected = "True"
                    
                        

                DrawerClickableItem:
                    icon: "book"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Saved texts"
                    
    

"""


