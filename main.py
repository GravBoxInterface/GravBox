from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', 0)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Ellipse, Line

Builder.load_file('hueLayout.kv')

class ColorLoopWidget(Widget):
    xlabel = ObjectProperty()
    ylabel = ObjectProperty()
    xlabel2 = ObjectProperty()
    ylabel2 = ObjectProperty()
    def on_touch_down(self, touch):
        with self.canvas:
            self.canvas.clear()
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.xlabel.text = 'x: '+str(touch.x)
            self.ylabel.text = 'y: '+str(touch.y)
            
    def on_touch_up(self, touch):
        with self.canvas:
            self.canvas.clear()
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.xlabel2.text = 'x: '+str(touch.x)
            self.ylabel2.text = 'y: '+str(touch.y)




class HueLayout(Widget):
    colorloopwidget = ObjectProperty()
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


class HueApp(App):
    def build(self):
        return HueLayout()

if __name__ == '__main__':
    HueApp().run()