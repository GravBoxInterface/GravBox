import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.core.window import Window

Window.size = (1900,1200)

class Controller(FloatLayout):
    pass
    
class GravBoxApp(App):

    def build(self):
        return Controller()

if __name__ == '__main__':
    SliderApp().run()