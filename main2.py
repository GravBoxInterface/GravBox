from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', 0)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Color, Ellipse, Line, Triangle, Rectangle
import numpy as np
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.storage.jsonstore import JsonStore
from os.path import join

Builder.load_file('huelayout.kv')

class ColorLoopWidget(Widget):
	xlabel = ObjectProperty()
	orbit = ObjectProperty()
	ylabel = ObjectProperty()
	xlabel2 = ObjectProperty()
	ylabel2 = ObjectProperty()
	'''x_init = NumericProperty(0)
	y_init = NumericProperty(0)
	x_fin = NumericProperty(0)
	y_fin = NumericProperty(0)
	x_diff = NumericProperty(0)
	y_diff = NumericProperty(0)
	angle = NumericProperty(0)'''
    
	def on_touch_down(self, touch):
		with self.canvas:
			self.canvas.clear()
			if touch.x > 500:
				pass
			else:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				self.xlabel.text = 'x: '+str(touch.x)
				self.ylabel.text = 'y: '+str(touch.y)
				global x_init
				x_init = touch.x
				print x_init
				global y_init
				y_init = touch.y
				print y_init
					
	def on_touch_up(self, touch):
		with self.canvas:
			self.canvas.clear()
			if touch.x > 500:
				pass
			else:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				self.xlabel2.text = 'x: '+str(touch.x)
				self.ylabel2.text = 'y: '+str(touch.y)
				global x_diff
				x_diff = (touch.x - x_init)
				print x_diff
				global y_diff
				y_diff = (touch.y - y_init)
				print y_diff
				global angle
				angle = float(np.arctan2(y_diff,x_diff)*180/np.pi)
				print angle
				
				Line(points=[x_init,y_init,touch.x,touch.y])
		
	def on_touch_move(self,touch):
		with self.canvas:
			self.canvas.clear()
			if touch.x > 500:
				pass
			else:
				d = 10
				Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
				touch.ud['line'] = Line(points=(touch.x, touch.y))
				self.xlabel2.text = 'x: '+str(touch.x)
				self.ylabel2.text = 'y: '+str(touch.y)
				global x_fin
				x_fin = touch.x
				print x_fin
				global y_fin
				y_fin = touch.y
				print y_fin
				Line(points=[x_init,y_init,touch.x,touch.y])
			
	def orbit(self, file):
		x, y = np.loadtxt(file, delimiter=',', usecols=(2,3), unpack=True)
		for i in np.arange(0, len(x)):
			#self.canvas.clear()
			#d = 10
			#Ellipse(pos=(x[i] - d/2, y[i] - d/2), size=(d,d))
			print x[i], y[i]

class HueLayout(Widget):
	colorloopwidget = ObjectProperty()
	orbit = ObjectProperty()
	xlabel = ObjectProperty()
	ylabel = ObjectProperty()
	xlabel2 = ObjectProperty()
	ylabel2 = ObjectProperty()

##    def on_touch_down():
##        ColorLoopWidget.on_touch_down()
##
##    def on_touch_move():
##        ColorLoopWidget.on_touch_move()	

	def clear_canvas(self):
		self.colorloopwidget.canvas.clear()
	
	def save(self):
		store = JsonStore('algorithm_input.json')
		store.put('x_init', pos=x_init)
		
#	def orbit(self):
#		ColorLoopWidget.orbit(self, file)

class HueApp(App):
    def build(self):
        return HueLayout()

if __name__ == '__main__':
    HueApp().run()