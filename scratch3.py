import kivy
kivy.require('1.10.0')

import numpy as np

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager

from kivy.graphics import Rectangle, Color, Ellipse, Line
from functools import partial
from random import randint



from kivy.config import Config
Config.set('graphics', 'resizeable', 0) #don't make the app resizeable
#Graphics fix
Window.size = (1280, 800)
Window.clearcolor = (0, 0, 0, 1.) #fixes drawing issues on some phones



def thisbuildsitall():
    pass
    
    
    
class MyButton(Button):
    #uniform button styles class
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.015 #setting font size
        
class SmartMenu(Widget):
    #the instance created by this class appears when the game is first started
    buttonList = []
    
    def __init__(self, **kwargs):
    #create custom events first
        self.register_event_type('on_button_release')
        
        super(SmartMenu, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
    def on_button_release(self, *args):
        print ('The on_button_release event was just dispatched', args)
        pass
            
    def callback(self, instance):
        print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release') #dispatching the callback event 'on_button_release' to tell the parent instance to read the button text
            
    def addButtons(self):
        
        tmpBtn1 = MyButton(text = self.buttonList[0]) #start button
        tmpBtn1.size_hint = (.21, .09)
        tmpBtn1.pos_hint ={'x': .395, 'y': .24}
        tmpBtn1.background_color = [.4, .4, .4, .4]
        tmpBtn1.bind(on_release = self.callback) #when the button is released the callback function is called
        self.layout.add_widget(tmpBtn1)   

        tmpBtn2 = MyButton(text = self.buttonList[1]) #about button
        tmpBtn2.size_hint = (.08, .095)
        tmpBtn2.pos_hint ={'x': .618, 'y': 0}
        tmpBtn2.background_color = [.4, .4, .4, .4]
        tmpBtn2.bind(on_release = self.callback) #when the button is released the callback function is called
        self.layout.add_widget(tmpBtn2)
               
        tmpBtn3 = MyButton(text = self.buttonList[2]) #uiowa button
        tmpBtn3.size_hint = (.08, .095)
        tmpBtn3.pos_hint = {'x':.7, 'y': 0}
        tmpBtn3.background_color = [.4, .4, .4, .4]
        tmpBtn3.bind(on_release = self.callback) #when the button is released the callback function is called
        self.layout.add_widget(tmpBtn3)
    
    def addBackButton(self):
        
        tmpBtn4 = MyButton(text = self.buttonList[3]) #uiowa button
        tmpBtn4.size_hint = (.08, .095)
        tmpBtn4.pos_hint = {'x':0, 'y': 0}
        tmpBtn4.background_color = [1, 1, 1, 1]
        tmpBtn4.bind(on_release = self.callback) #when the button is released the callback function is called
        self.layout.add_widget(tmpBtn4)
               
    def buildUp(self):
        self.addButtons()


class SmartStartMenu(SmartMenu):
    #setup the menu button names
    buttonList = ['START YOUR JOURNEY', 'ABOUT', 'UIOWA', 'BACK']
    
    def __init__(self, **kwargs):        
        super(SmartStartMenu, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.layout.width = Window.width
        self.layout.height = Window.height
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
        '''
        self.msg = Label(text='')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.45, Window.height*0.75)
        self.add_widget(self.msg)
        '''
        self.img = Image(source = 'C://Users/Mason/Desktop/Sandbox Kivy/Gravity-Sandbox-homescreen.jpg')
        self.img.size = (Window.width*1.2, Window.height*1.0)
        self.img.pos = (-Window.width*0.1, -Window.height*0.0)
        self.img.opacity = 0.4
        self.add_widget(self.img)
        
     

class WidgetDrawer(Widget):
#this widget is used to draw all of the objects on the screen
#it handles: widget movement, size, positioning

    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)
#if you haven't seen with before, here's a link http://effbot.org/zone/python-with-statement.html
        with self.canvas:
#setup a default size for the object
            self.size = (Window.width*.002*25, Window.width*.002*25)
#create a rectangle w/ the image drawn on top
            self.rect_bg=Rectangle(source=imageStr, pos=self.pos, size=self.size)
#calls the update_graphics_pos func every time the position var is modified
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
        #center the widget
            self.pos = (self.x, self.y)
        #center the rectangle on the widget
            self.rect_bg.pos = self.pos
            
    def update_graphics_pos(self, instance, value):
    #if the widgets position moves, the rectangle that contains the image also moves
        self.rect_bg.pos = value
        
    #use this func to change widget size    
    def setSize(self, width, height):
        self.size = (width, height)
    
    #use this func to change widget position    
    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

        
class arbitrary(WidgetDrawer):
    pass


class MainPanel(Widget): #WORKING FOR MAIN PANEL W/ BUTTONS/SLIDERS
    sidebar = []
    
    def __init__(self, **kwargs):        
        super(MainPanel, self).__init__(**kwargs)
        
        self.layout = BoxLayout(orientation='vertical')
        self.layout.width = Window.width*.33
        self.layout.height = Window.height
        self.layout.x = 0 #Window.width/3 - self.layout.width
        self.layout.y = 0 #Window.height - self.layout.height/2
        self.add_widget(self.layout)
        btn1 = Button(text='BTN1', size_hint=(.7, 1))
        btn2 = Button(text='BTN2', size_hint=(.2, 1))
        self.add_widget(btn1)
        self.add_widget(btn2)

        
               
class GUI(Widget):
#this is the main widget that contains everything. This is the primary object 
#that runs

    asteroidList = []
#important to use numericprop here so we can bind a callback to use every
#time the number changes
    asteroidScore = NumericProperty(0)
    xlabel = ObjectProperty()
    ylabel = ObjectProperty()
    xlabel2 = ObjectProperty()
    ylabel2 = ObjectProperty()
    minProb = 1780
    
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)

  
    def drawTouchResponse(self, x, y):
        pass
        '''
        #draw the arrows directly onto the canvas
        with self.canvas:
            tmpSize = Window.width*0.07, Window.width*0.07
            tmpPos = (x-self.width/4, y-self.height/4)
            self.arrowRect = Rectangle(source='C://Users/Mason/Desktop/Sandbox Kivy/flame1.png', pos=tmpPos, size=tmpSize)
        #schedule removal of said arrows
        def removeArrows(arrow, *largs):
             self.canvas.remove(arrow)
             
        def changeExplosion(rect, newSource, *largs):
             rect.source = newSource
        #schedule the subsequent explosions
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame2.png'), 0.15)
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame3.png'), 0.3)
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame4.png'), 0.45)
        Clock.schedule_once(partial(removeArrows, self.arrowRect), 0.46)
        '''
    #handle input events
    def on_touch_down(self, touch):
        with self.canvas:
            self.canvas.clear()
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            #self.xlabel.text = 'x: '+str(touch.x)
            #self.ylabel.text = 'y: '+str(touch.y)
            #global x_init
            #global y_init
            #x_init = touch.x
            #y_init = touch.y
            
    def on_touch_up(self, touch):
        with self.canvas:
            self.canvas.clear()
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            #self.xlabel2.text = 'x: '+str(touch.x)
            #self.ylabel2.text = 'y: '+str(touch.y)
            #global x_diff
            #global y_diff
            #global angle
            #x_diff = (touch.x - x_init)
            #y_diff = (touch.y - y_init)
            #angle = np.arctan2(y_diff, x_diff)*180/np.pi
            #print (x_diff, y_diff, angle)
            
            #Line(points=[x_init, y_init, touch.x, touch.y])
            
    def on_touch_move(self, touch):
        with self.canvas:
            self.canvas.clear()
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            #self.xlabel2.text = 'x: '+str(touch.x)
            #self.ylabel2.text = 'y: '+str(touch.y)
            #global x_final, y_final, x_diff, y_diff
            #x_final = touch.x
            #y_final = touch.y
            #Line(points=[x_init, y_init, touch.x, touch.y])
        
        
    def update(self, dt):
#this update function is the main update function for the app
#ALL of the logic has origin here
#events are setup here as well
        pass
        '''
        self.ship.update()
        tmpCount = randint(1, 1800)
        if tmpCount > self.minProb:
            self.addAsteroid()
            if self.minProb < 1300:
                self.minProb = 1300
            self.minProb = self.minProb -1
            
        for k in self.asteroidList:
            if k.collide_widget(self.ship):
                print ('death')
                self.gameOver()
                Clock.unschedule(self.update)
                self.ship.explode()
            k.update()
            if k.x < -100:
                self.remove_widget(k)
                self.asteroidScore = self.asteroidScore + 1
            
        tmpAsteroidList = self.asteroidList
        tmpAsteroidList[:] = [x for x in tmpAsteroidList if ((x.x > -100))]
        self.asteroidList = tmpAsteroidList
        '''    
        
class ClientApp(App):

    def build(self):
        #this is where the root widget goes
        #should be a canvas
        self.parent = Widget() #empy holder for buttons, etc
        self.app = GUI()
        #Clock.schedule_interval(app.update, 1.0/60.0)
        #parent.add_widget(app)
        self.sm1 = SmartMenu()
        self.sm = SmartStartMenu()
        self.sm.buildUp()
        #self.sm.addBackButton()
        
        
        #GUI = ObjectProperty()
       #xlabel = ObjectProperty()
        #ylabel = ObjectProperty()
        #xlabel2 = ObjectProperty()
        #ylabel2 = ObjectProperty()
    
        def clear_canvas(self):
            self.GUI.canvas.clear
        
        
        def check_button(obj):
        #check for which button was pressed
            if self.sm.buttonText == 'START YOUR JOURNEY':
                self.parent.remove_widget(self.sm) #removes SmartStartMenu()
                print ('start the game already') 
                Clock.unschedule(self.app.update)
                Clock.schedule_interval(self.app.update, 1.0/60.0)
                self.parent = Widget()
                self.app = GUI()
                self.MP = MainPanel()
                try:
                    self.parent.remove_widget(self.aboutText)
                except:
                    print ('text removal failed')
                    
                    
            if self.sm.buttonText == 'ABOUT':
                self.parent.remove_widget(self.sm)
                
                self.aboutText = Label(text= 'ABOUT INFO HERE')
                self.aboutText.pos = (Window.width*0.45, Window.height*0.35)
                self.parent.add_widget(self.aboutText)
                
                self.backButton = Button(text= 'BACK')
                self.backButton.bind(on_release = ClientApp.build)
                self.parent.add_widget(self.backButton)
                    
     
            if self.sm.buttonText == 'UIOWA':
                self.parent.remove_widget(self.sm)
                
                self.aboutText = Label(text= 'UIOWA INFO HERE')
                self.aboutText.pos = (Window.width*0.45, Window.height*0.45)
                self.parent.add_widget(self.aboutText)
                
                self.backButton = Button(text = 'BACK')
                self.parent.add_widget(self.backButton)
                
            #if self.sm.buttonText == 'BACK':
                #print('back button checked')
                
                
                
        #bind a callback function that responds to event 'on_button_pressed' by calling function check_button
        self.sm.bind(on_button_release = check_button)
        #setup listeners for smartstartmenu
        self.parent.add_widget(self.sm)
        self.parent.add_widget(self.app) #use this hierarchy to make it easy to deal w/ buttons
        return self.parent
        
if __name__=='__main__':
    ClientApp().run()