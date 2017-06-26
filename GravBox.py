from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', 0)
from kivy.app             import App
from kivy.uix.widget      import Widget
from kivy.uix.boxlayout   import BoxLayout
from kivy.lang            import Builder
from kivy.properties      import ObjectProperty
from kivy.graphics        import Color, Ellipse, Line, Triangle, Rectangle
from kivy.uix.button      import Button
from kivy.uix.label       import Label
from kivy.uix.slider      import Slider
from kivy.uix.image       import Image
import numpy as np
import random

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

#Creates application
class GravBox(App):
    def build(self):
        
        #Creates main layout
        layout=BoxLayout(padding=10)
        size=(1000,500)
        
        #Creates left layout within main layout
        LeftLayout=BoxLayout(padding=10)
        size=(700,500)
        layout.add_widget(LeftLayout)
        
        #Creates right layout within main layout, with vertical orientation
        RightLayout=BoxLayout(padding=10,orientation='vertical')
        size=(300,500)
        layout.add_widget(RightLayout)
        
        #Creates object menu button
        ObjectButton = Button(text="Object",background_color=[0,0,1,1], bold=True)
        RightLayout.add_widget(ObjectButton)
        
        #Angle Label
        AngleLabel = Label(text='Angle: 0',font_size=20)
        RightLayout.add_widget(AngleLabel)
        
        #Creates the layout for the angle slider
        SliderLayout1 = BoxLayout(padding=10,orientation='horizontal')
        size=(300,400)
        RightLayout.add_widget(SliderLayout1)
        
        #Aspects of the angle slider
        ZeroLabel1 = Label(text='0',font_size=20)
        SliderLayout1.add_widget(ZeroLabel1)
        AngleSlider = Slider(min=0,max=360,step=0.5,value=0)
        SliderLayout1.add_widget(AngleSlider)
        #Function to have the angle slider interact with the angle label
        def OnAngleSliderValueChange(instance,value):
            AngleLabel.text = 'Angle: ' + str(value)
        AngleSlider.bind(value=OnAngleSliderValueChange)
        ThreeSixtyLabel = Label(text='360',font_size=20)
        SliderLayout1.add_widget(ThreeSixtyLabel)
        
        #Speed Label
        SpeedLabel = Label(text='Speed: 0.0',font_size=20)
        RightLayout.add_widget(SpeedLabel)
        
        #Creates the layout for the speed slider
        SliderLayout2 = BoxLayout(padding=10,orientation='horizontal')
        RightLayout.add_widget(SliderLayout2)
        
        #Aspects of the speed slider
        ZeroLabel2 = Label(text='0',font_size=20)
        SliderLayout2.add_widget(ZeroLabel2)
        SpeedSlider = Slider(min=0,max=1,step=0.01,value=0)
        SliderLayout2.add_widget(SpeedSlider)
        def OnSpeedSliderValueChange(instance,value):
            SpeedLabel.text = 'Speed: ' + str(value)
        SpeedSlider.bind(value=OnSpeedSliderValueChange)
        OneLabel = Label(text='1',font_size=20)
        SliderLayout2.add_widget(OneLabel)
        
        #Go! Button
        GoButton = Button(text='Go!',font_size=40,bold=True)
        RightLayout.add_widget(GoButton)
        return layout
    
class InteractiveEnvironment(Widget):
    def build(self):
        layout=BoxLayout(padding=10)
        size=(500,500)
    
if __name__ == "__main__":
    app=GravBox()
    app.run()
    