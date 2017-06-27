import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.graphics import Rectangle, Color, Ellipse, Line, Triangle
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, ObjectProperty, OptionProperty, ReferenceListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.vector import Vector


Window.size = (1280, 800)

Builder.load_string('''
<Borders>
    ball: pong_ball
    anchor_x: 'right'
    canvas.before: 
        BorderImage:
            border: 10, 10, 10, 10
            texture: root.background_image.texture
            size: self.width * .7, self.height
            pos: self.pos
    canvas:
        Color:
            rgba: 0, 1, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size
    canvas.after:
        Color:
            rgba: 0, 1, 1, 1
        Line:
            points: self.points
            cap: 'round'
            joint: 'round'
            width: 2
    PongBall:
        id: pong_ball
        center: root.center
     
    AnchorLayout:
        id: main_panel
        orientation: 'horizontal'
        size_hint: (.3, 1)

        canvas:
            Color:
                rgba: .8, .4, .6 ,.9
            Rectangle:
                size: self.width, self.height
                pos: self.pos
        BoxLayout:
            id: parameter_layout
            orientation: 'vertical'
            size_hint: 1, 1
            Button:
                text: 'Object'
                on_press: self.text='changed'
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "0"
                    font_size: 20
                Slider:
                    id: angle_slider
                    min: 0
                    max: 360
                    step: .5
                    val: 0
                    on_value: angle_label.text = "Angle: " + str(self.value)
                Label:
                    text: "360"
                    font_size: 20
            Label:
                id: angle_label
                text: "Angle: 0.0"
                font_size: 24
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text: "0"
                    font_size: 20
                Slider:
                    id: speed_slider
                    min: 0
                    max: 1
                    step: .01
                    val: 0
                    on_value: speed_label.text = "Speed: " + str(self.value)
                Label:
                    text: "1"
                    font_size: 20
            Label:
                id: speed_label
                text: "Speed: 0.0"
                font_size: 24
            Button:
                id: Go_btn
                text: "GO!"
                on_press: Go_btn.text = "Sent!"
                
<PongBall>:
    size: 10, 10
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            pos: self.x + 200, self.y + 400
            size: self.width * .01, self.height * .018

        
                                                      
''')

class Borders(AnchorLayout):

    background_image = ObjectProperty(Image(source='C://Users/Mason/Downloads/bootanimation.zip', anim_delay=.5)) #CHANGE IMAGE SOURCE
            
    points = ListProperty([])
    print(points)
    
    ball = ObjectProperty(None)
    
    def BGI(self):
        global background_image
        self.background_image.reload()
        
    
    def serve_ball(self, vel=(4, 0)):
        pass
        self.ball.center = self.center
        self.ball.velocity = vel
    
    def update(self, dt):
        self.ball.move()
        self.BGI()
        
        
        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # went off a side (NEEDS WORK)
        if (self.ball.x < self.x) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        
                                                    
    def on_touch_down(self, touch):
        if super(Borders, self).on_touch_down(touch):
            return True
        touch.grab(self)
        self.points.append(touch.pos)
        return True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.points[-1] = touch.pos
            return True
        return super(Borders, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            return True
        ball = PongBall()
        ball.center = (touch.x, touch.y)
        self.add_widget(ball)
        return super(Borders, self).on_touch_up(touch)
    
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    
class ScratchApp(App):

    def build(self):
        scratch = Borders()
        scratch.serve_ball()
        Clock.schedule_interval(scratch.update, 1.0)
        return scratch

if __name__ == '__main__':
    ScratchApp().run()