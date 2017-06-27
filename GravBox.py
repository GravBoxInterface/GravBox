from kivy.config import Config
Config.set('graphics', 'width', '1250')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 0)
from kivy.app                 import App
from kivy.uix.widget          import Widget
from kivy.uix.boxlayout       import BoxLayout
from kivy.uix.relativelayout  import RelativeLayout
from kivy.lang                import Builder
from kivy.properties          import ObjectProperty
from kivy.graphics            import Color, Ellipse, Line, Triangle, Rectangle
from kivy.uix.button          import Button
from kivy.uix.label           import Label
from kivy.uix.slider          import Slider
from kivy.uix.image           import Image
from kivy.uix.effectwidget    import EffectWidget
from kivy.clock               import Clock
from kivy.cache               import Cache
import numpy as np
import random
import threading


#Creates application
class GravBox(App):
    
    def build(self):
        
        #Creates main layout
        layout=BoxLayout(padding=10)
        size=(1000,500)
        
        #Creates left layout within main layout
        LeftLayout=RelativeLayout(padding=10,size_hint=[.7,1])
        size=(700,500)
        layout.add_widget(LeftLayout)
        
        Background_Image = Image(source='color_field_0.jpg')
        LeftLayout.add_widget(Background_Image)
        
        Painter = DrawingEnvironment(size_hint=[.7,1])
        size=(700,500)
        LeftLayout.add_widget(Painter)
        
        #Creates right layout within main layout, with vertical orientation
        RightLayout=BoxLayout(padding=10,orientation='vertical',size_hint=[.28,1])
        size=(280,500)
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
   
    
#Creates the drawing environment which is called by the main application
class DrawingEnvironment(Widget):
    xlabel = ObjectProperty()
    ylabel = ObjectProperty()
    xlabel2 = ObjectProperty()
    ylabel2 = ObjectProperty()
    
    #Provides functionality for a touch_down event
    def on_touch_down(self, touch):
        with self.canvas:
            if touch.x < 880:
                self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                global x_init
                global y_init
                x_init = touch.x
                y_init = touch.y
                print x_init
                print y_init
            else:
                self.canvas.clear()
                print('touch_down out of bounds')

    #Provides functionality for a touch_up event            
    def on_touch_up(self, touch):
        with self.canvas:
            if touch.x < 880:
                self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                global x_diff
                global y_diff
                x_diff = (touch.x - x_init)
                print touch.x
                print touch.y
                #print x_diff
                y_diff = (touch.y - y_init)
                #print y_diff
                global angle
                angle = np.arctan2(y_diff,x_diff)*180/np.pi
                #print angle
                Line(points=[x_init,y_init,touch.x,touch.y])
            else:
                self.canvas.clear()
                print touch.x
                print('touch_up out of bounds')
            

    #Provides functionality for a touch_move event            
    def on_touch_move(self,touch):
        with self.canvas:
            if touch.x < 880:
                self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                global x_init
                global y_init
                global x_final
                global y_final
                global x_diff
                global y_diff
                x_final = touch.x
                y_final = touch.y
                Line(points=[x_init,y_init,touch.x,touch.y])
            else:
                self.canvas.clear()
                print('touch_move out of bounds')
    
if __name__ == "__main__":
    app=GravBox()
    app.run()
    
