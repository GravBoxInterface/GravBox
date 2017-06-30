from kivy.config import Config
Config.set('graphics', 'width', '1250')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 0)
from kivy.app                 import App
from kivy.uix.widget          import Widget
from kivy.uix.boxlayout       import BoxLayout
from kivy.uix.relativelayout  import RelativeLayout
from kivy.lang                import Builder
from kivy.properties          import ObjectProperty, NumericProperty
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
        LeftLayout=RelativeLayout(padding=10,size_hint=[.5,1])
        size=(500,500)
        layout.add_widget(LeftLayout)
        
        Background_Image = Image(source='color_field_0.jpg')
        LeftLayout.add_widget(Background_Image)
        
        Painter = DrawingEnvironment(size_hint=[.5,1])
        size=(500,500)
        LeftLayout.add_widget(Painter)
        
        #Creates right layout within main layout, with vertical orientation
        RightLayout=BoxLayout(padding=10,orientation='vertical',size_hint=[.5,1])
        size=(500,500)
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
	x_init = NumericProperty(0)
	y_init = NumericProperty(0)
	x_fin = NumericProperty(0)
	y_fin = NumericProperty(0)
	x_diff = NumericProperty(0)
	y_diff = NumericProperty(0)
	angle = NumericProperty(0)
	out = None

	#Provides functionality for a touch_down event
	def on_touch_down(self, touch):
		global out
		global x_init
		global y_init
		with self.canvas:
			self.canvas.clear()
			if touch.x > 500:
				out = True
				pass
			else:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				x_init = touch.x
				print x_init
				y_init = touch.y
				print y_init				
				out = False
				print "Touch down out of bounds"

	#Provides functionality for a touch_up event            
	def on_touch_up(self, touch):
		global out
		global x_init
		global y_init
		global x_diff
		global y_diff
		with self.canvas:
			self.canvas.clear()
			if touch.x > 500 and out == False:
				d = 10
				Ellipse(pos=(500 - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(500, touch.y))
				x_diff = (500 - x_init)
				print x_diff
				y_diff = (touch.y - y_init)
				print y_diff
				Line(points=[x_init,y_init,500,touch.y])
				
			elif touch.x <= 500 and out == False:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				x_diff = (touch.x - x_init)
				print x_diff
				y_diff = (touch.y - y_init)
				print y_diff

				Line(points=[x_init,y_init,touch.x,touch.y])
			elif touch.x > 500 and out == True:
				print "Touch up out of bounds"
				pass
			elif touch.x <= 500 and out == True:
				pass            

	#Provides functionality for a touch_move event            
	def on_touch_move(self,touch):
		global out
		global x_init
		global y_init
		global x_fin
		global y_fin
		with self.canvas:
			self.canvas.clear()
			if touch.x <= 500 and out == False:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				x_fin = touch.x
				print x_fin
				y_fin = touch.y
				print y_fin
				Line(points=[x_init,y_init,touch.x,touch.y])
			elif touch.x > 500 and out == False:
				d = 10
				Ellipse(pos=(500 - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				x_fin = 500
				print x_fin
				y_fin = touch.y
				print y_fin
				Line(points=[x_init,y_init,500,touch.y])
			elif touch.x > 500 and out == True:
				print "Touch move out of bounds"
				pass
			elif touch.x <= 500 and out == True:
				pass

if __name__ == "__main__":
	app=GravBox()
	app.run()