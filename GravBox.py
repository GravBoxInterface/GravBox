from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.graphics import Color, Rectangle, Ellipse, Line
from random import randint
from time import sleep

import os
import os.path
import numpy as np

from kivy.config import Config
Config.set('graphics', 'resizeable', 1)  #makes the window resizeable if 1, static if 0
#Config.set('graphics', 'fullscreen', 1)
#Config.set('graphics', 'width', '1280')
#Config.set('graphics', 'height', '900')
Window.size = (1280, 800)
Window.clearcolor = (0, 0, 0, 1.) #fixes drawing issues on some phones

assetsdirectory = 'C://Users/Mason/Desktop/Sandbox Kivy/' #CURRENT FILEPATH FOR ALL IMAGES/ASSETS

os.chdir(r'C://Users/Mason/Desktop/Sandbox Kivy/')

class MyButton(Button):
    #uniform button styles class
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.015 #setting font size

        
class Particle(Widget):
    
    def __init__(self, pos, size):
        super(Particle, self).__init__(pos=pos, size=size)
        with self.canvas:
            Color(1,1,1)
            self.ellipse = Ellipse(pos=pos, size=size)
        self.bind(pos = self.updatePosition)
        
    def updatePosition(self, *args):
        self.ellipse.pos = self.pos    


class WelcomeScreen(Screen):
    
    buttonList = ['START YOUR JOURNEY', 'ABOUT', 'UIOWA', 'BACK'] #list of buttons, used for naming 
    
    welcomeImage = assetsdirectory+str('Gravity-Sandbox-homescreen.jpg') #WELCOME SCREEN BACKGROUND IMAGE PATH
    
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout() #Float Layout for positioning buttons and image anywhere on the screen
        self.layout.width = Window.width #the float layout is the size of the window
        self.layout.height = Window.height
        self.layout.x = Window.width/2 - self.layout.width/2 #sets the x position of the layout to 0
        self.layout.y = Window.height/2 - self.layout.height/2 #sets the y position of the layout to 0
        self.add_widget(self.layout) #adds the layout to the screen
        
        self.img = Image(source = self.welcomeImage)
        self.img.size = (Window.width*1.0, Window.height*1.2)
        self.img.pos = (-Window.width*0.0, -Window.height*0.0)
        self.img.opacity = 1.0 #alpha value between 0.0 - 1.0
        self.add_widget(self.img) #adds the image to the screen
                
        tmpBtn1 = MyButton(text = self.buttonList[0]) #start button
        tmpBtn1.size_hint = (.21, .09)
        tmpBtn1.pos_hint ={'x': .395, 'y': .24}
        tmpBtn1.background_color = [.4, .4, .4, .4] #backgroundcolor of the button (this is grayish)
        tmpBtn1.bind(on_release = self.changer) #when the button is released the changer function is called
        self.layout.add_widget(tmpBtn1) #adds the button called tmpBtn1 to the floatlayout

        tmpBtn2 = MyButton(text = self.buttonList[1]) #about button
        tmpBtn2.size_hint = (.08, .095)
        tmpBtn2.pos_hint ={'x': .618, 'y': 0}
        tmpBtn2.background_color = [.4, .4, .4, .4]
        tmpBtn2.bind(on_release = self.about) #when the button is released the about function is called
        self.layout.add_widget(tmpBtn2) #adds the button called tmpBtn2 to the floatlayout
               
        tmpBtn3 = MyButton(text = self.buttonList[2]) #uiowa button
        tmpBtn3.size_hint = (.08, .095)
        tmpBtn3.pos_hint = {'x':.7, 'y': 0}
        tmpBtn3.background_color = [.4, .4, .4, .4]
        tmpBtn3.bind(on_release = self.uiowa) #when the button is released the uiowa function is called
        self.layout.add_widget(tmpBtn3) #adds the button called tmpBtn3 to the floatlayout
            
    def callback(self, instance):
        print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release') #dispatching the callback event 'on_button_release' to tell the parent instance to read the button text
        
    def changer(self, *args): #the changer function
        self.manager.current = 'screen2' #sets the current screen to screen2 - the interaction screen
        print('This is the MAIN button') #print statement for debugging
        
    def about(self, instance): #the about function
        self.manager.current = 'screen3' #sets the current screen to screen3 - the about screen
        print('This is the ABOUT button') #print statement for debugging
        
    def uiowa(self, instance): #the uiowa function
        self.manager.current = 'screen4' #sets the current screen to screen4 - the uiowa screen
        print('This is the UIOWA button') #print statement for debuggging
        
        
    
class AboutScreen(Screen):
    
    aboutImage = assetsdirectory+str('gray_star.png') #ABOUT SCREEN BACKGROUND IMAGE 
    
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.layout.width = Window.width
        self.layout.height = Window.height
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
        self.img = Image(source = self.aboutImage)
        self.img.size = (Window.width*1.0, Window.height*1.0)
        self.img.pos = (-Window.width*0.0, -Window.height*0.0)
        self.img.opacity = 0.4
        self.add_widget(self.img)
        
        self.aboutText = Label(text= 'GravBox is the interface application for the Augmented Reality (AR) Sandbox for gravitational dynamics simulations designed and built\n by Dr. Hai Fu\'s Introduction to Astrophysics class during the 2016-2017 academic year and beyond.\n GravBox itself was designed by Zachary Luppen, Erin Maier, and Mason Reed.\n\nAR Sandbox is the result of an NSF-funded project on informal science education for freshwater lake and watershed science developed by the\n UC Davis\' W.M. Keck Center for Active Visualization in the Earth Sciences (KeckCAVES),\n together with the UC Davis Tahoe Environmental Research Center, Lawrence Hall of Science, and ECHO Lake Aquarium and Science Center.')
        self.aboutText.pos = (.5, .5)
        #self.aboutText.size = self.size
        self.add_widget(self.aboutText)
                
        tmpBtn1 = MyButton(text = 'BACK') #start button
        tmpBtn1.size_hint = (.1, .1)
        tmpBtn1.pos_hint ={'x': 0, 'y': .90}
        tmpBtn1.background_color = [.4, .4, .4, 1]
        tmpBtn1.bind(on_release = self.backButton) #when the button is released the callback function is called
        self.layout.add_widget(tmpBtn1)
        
    def backButton(self, *args):
        self.manager.current = 'screen1'
        
        
        
class UiowaScreen(Screen):
    
    uiowaImage  = assetsdirectory+str('gold_star.png') #UIOWA SCREEN BACKGROUND IMAGE
    
    def __init__(self, **kwargs):
        super(UiowaScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.layout.width = Window.width
        self.layout.height = Window.height
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
        self.img = Image(source = self.uiowaImage)
        self.img.size = (Window.width*1.0, Window.height*1.0)
        self.img.pos = (-Window.width*0.0, -Window.height*0.0)
        self.img.opacity = 0.4
        self.add_widget(self.img)
        
        self.aboutText = Label(text= 'UIOWA INFO HERE')
        self.aboutText.pos = (.25, .25)
        self.add_widget(self.aboutText)
                
        tmpBtn1 = MyButton(text = 'BACK') #start button
        tmpBtn1.size_hint = (.1, .1)
        tmpBtn1.pos_hint ={'x': 0, 'y': .9}
        tmpBtn1.background_color = [.4, .4, .4, 1]
        tmpBtn1.bind(on_release = self.backButton) #when the button is released the backButton function is called
        self.layout.add_widget(tmpBtn1)
        
    def backButton(self, *args):
        self.manager.current = 'screen1'            
        
        
        
class InteractionScreen(Screen): #This is the main screen for drawing and user input. Next steps - adding/binding buttons
          
    def __init__(self, **kwargs):
        super(InteractionScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout() #creates a Float Layout called self.layout  (self. allows reference for entire class?)
        self.layout.width = Window.width
        self.layout.height = Window.height
        self.layout.x = 0 #Window.width/2 - self.layout.width/2
        self.layout.y = 0 #Window.height/2 - self.layout.height/2

        self.rightlayout = FloatLayout() #creates an anchor Layout 
        self.rightlayout.width = self.layout.width*.3
        self.rightlayout.height = self.layout.height
        self.rightlayout.x = Window.width - self.rightlayout.width
        self.rightlayout.y = Window.height/2 - self.rightlayout.height/2
        
        self.leftlayout = FloatLayout()
        self.leftlayout.width = self.layout.width*0.7
        self.leftlayout.height = self.layout.height
        self.leftlayout.x = 0 #Window.width - self.leftlayout.width
        self.leftlayout.y = 0 #Window.width/2 - self.leftlayout.height/2
        
              
        with self.canvas: #sets canvas instructions for the float layout and draws a red rectangle filling the entire layout
            Color(1., 0, 0, .4) #RED
            Rectangle(pos=(self.layout.x, self.y), size=(self.layout.width, self.layout.height))
        
        with self.rightlayout.canvas: #sets canvas instructions for the rightlayout and draws a blue rect. filling the entire layout
            Color(0, 0, 1., .3) #BLUE
            Rectangle(pos=(self.rightlayout.x, self.rightlayout.y), size=(self.rightlayout.width, self.rightlayout.height))
            
        with self.leftlayout.canvas: #sets canvas instruction for the leftlayout and draws a green rectangle filling the entire layout
            Color(0, 1., 0, .2) #GREEN
            Rectangle(pos=(self.leftlayout.x, self.leftlayout.y), size=(self.leftlayout.width, self.leftlayout.height))
        
        
        btn2 = Button(text='Back', size_hint=(.1, .1), pos_hint={'left':0, 'top':1}) #back button to the interaction screen
        btn2.bind(on_press=self.changer) #binds this button to change the screen back to the welcome screen
        self.add_widget(btn2) #adds the button to the float layout
        
        other_btn2 = Button(text='test button 2',size_hint=(.1, .1),pos_hint={'left':1, 'bottom':0}) #arbitrary test button
        other_btn2.bind(on_press=self.test) #binds to the test func
        self.add_widget(other_btn2) #adds button to float layout - this button is the generic and used for debugging
        
        #OBJECT BUTTON (Must be in same order for correct layout)
        objButton = MyButton(text='Object Selector')
        objButton.pos_hint = {'x':0, 'y': .8}
        objButton.size_hint = (.3, .2)
        objButton.background_color = [.4, .4, .4, 1]
        objButton.bind(on_release = self.massSelect)
        self.rightlayout.add_widget(objButton)
        
        #TOPOGRAPHY TOGGLE SWITCH
        topoSwitch = Switch(active = True)
        topoSwitch.pos_hint = {'x':0, 'y': .64}
        topoSwitch.size_hint = (.3, .2)
        topoSwitch.background_color = [.4, .4, .4, 1]
        topoSwitch.bind(active = self.topoChange)
        self.rightlayout.add_widget(topoSwitch)
        
        #SPEED LABEL
        self.spdLabel = Label(text='Speed: 50')
        self.spdLabel.pos_hint = {'x':0, 'y':.57}
        self.spdLabel.size_hint = (.3, .1)
        self.spdLabel.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(self.spdLabel)
        
        #SPEED SLIDER & LABELS
        minLabel = Label(text='0')
        minLabel.pos_hint = {'x':0, 'y':.51}
        minLabel.size_hint = (.1, .1)
        self.rightlayout.add_widget(minLabel)
        
        maxLabel = Label(text='1.0')
        maxLabel.pos_hint = {'x':.2, 'y':.51}
        maxLabel.size_hint = (.1, .1)
        self.rightlayout.add_widget(maxLabel)
        
        spdSlider = Slider(min=0, max=1.0, step=0.01, value=.5)
        spdSlider.pos_hint = {'x':.05, 'y':.51}
        spdSlider.size_hint = (.2, .1)
        spdSlider.bind(value=self.spdSliderChange)
        self.rightlayout.add_widget(spdSlider)
        
        
        #ANGLE LABEL
        self.angLabel = Label(text='Angle: 180')
        self.angLabel.pos_hint = {'x':0, 'y': .33}
        self.angLabel.size_hint = (.3, .1)
        self.angLabel.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(self.angLabel)
        
        #ANGLE SLIDER & LABELS
        min2Label = Label(text='0')
        min2Label.pos_hint = {'x':0, 'y':.27}
        min2Label.size_hint = (.1, .1)
        self.rightlayout.add_widget(min2Label)
        
        max2Label = Label(text='360')
        max2Label.pos_hint = {'x':.2, 'y':.27}
        max2Label.size_hint = (.1, .1)
        self.rightlayout.add_widget(max2Label)
        
        angSlider = Slider(min=0, max=360, step=0.01, value=180)
        angSlider.pos_hint = {'x':.05, 'y':.27}
        angSlider.size_hint = (.2, .1)
        angSlider.bind(value=self.angSliderChange)
        self.rightlayout.add_widget(angSlider)
                        
        #GO BUTTON
        goButton = MyButton(text = 'Go!') #go button
        goButton.pos_hint = {'x':0, 'y':0}
        goButton.size_hint = (.3, .2)
        goButton.background_color = [.4, .4, .4, 1]
        goButton.bind(on_release = self.userInput) #when the button is released the USERINPUT function is called
        self.rightlayout.add_widget(goButton)
        
        #DRAWING FUNCTIONALITY
        global drawUtility
        drawUtility = DrawingApp()
        self.leftlayout.add_widget(drawUtility)                                 
        self.layout.add_widget(self.rightlayout)
        self.layout.add_widget(self.leftlayout)
        self.add_widget(self.layout)
        
        #DEFAULT BACKGROUND IMAGE
        self.bg_image_default = Image(source=assetsdirectory+str('starfield.jpg'))
        self.bg_image_default.allow_stretch = True
        self.bg_image_default.keep_ratio = False
        self.bg_image_default.size_hint_x = .7
        self.bg_image_default.size_hint_y = 1
        self.bg_image_default.pos = (0, 0)
        self.bg_image_default.opacity = 0.4
        self.leftlayout.add_widget(self.bg_image_default) #ADDS DEFAULT BACKGROUND IMAGE
        
        
        #BACKGROUND IMAGE UPDATE FUNCTION
        #if self.manager.current == 'screen2':
        Clock.schedule_interval(self.imageUpdate, 1.0/5.0) #SCHEDULES THE IMAGE UPDATING TO OCCUR
                
        
    def massSelect(self, *args):
        print('Mass Selector Function called')
        
    def userInput(self, *args): #This function to be used when the go button is relased, this will need input data from DrawingApp class
        print('UserInput Function Called')
        name_of_file = 'algorithm_input'                    #USER INPUT FILENAME
        inputFileName = os.path.join(assetsdirectory, name_of_file+'.txt') #TOTAL PATH NAME
        
        with open(inputFileName, 'w') as f:
	    f.write('%f\t%f\t%f\t%f\t%f\t%f' % (drawUtility.x_initial, drawUtility.y_initial, drawUtility.x_final, drawUtility.y_final))#, drawUtility.x_delta, drawUtility.y_delta))
        
        drawUtility.canvas.clear()
        particle = Particle([drawUtility.x_initial, drawUtility.y_initial])
        drawUtility.add_widget(particle)
        
	while os.path.isfile('algorithm_output.npy') == False:
            sleep(1)
	        print "Still no file"
	else:
	    print "File found!"

	    x,y = np.load('algorithm_output.npy') = np.load('mylistx.npy'); 
	    xs = np.split(x, len(x)/200, 0); ys = np.split(y, len(y)/200, 0)

            self.animate(xs, ys, 0, particle)
            
    def animate(self, x_coords, y_coords, index, instance):
        
        if index < len(x_coords):
            
            animation = Animation(pos=(int(x_coords[index][0]), int(y_coords[index][0])), t='linear', duration=.02)
            
            for i in np.arange(0, len(x_coords[index])):
                animation += Animation(pos=(int(x_coords[index][i]), int(y_coords[index][i])), t='linear', duration=.02)
                
            animation.bind(on_complete=lambda x, y: (self.animate(x_coords, y_coords, index+1, instance)))        
        
    def changer(self, *args):
        self.manager.current = 'screen1'
        
    def test(self, instance):
        print('This is another test sc2')
        
    def angSliderChange(self, instance, value):
        self.angLabel.text = 'Angle: ' +str(value)
        
    def spdSliderChange(self, instance, value):
        self.spdLabel.text = 'Speed: ' +str(value)
        
    def topoChange(self, instance, value):
        print('Topography toggled')
        
    def imageUpdate(self, dt):
        
        #TESTING MULTIPLE IMAGE UPDATE
        try:
            self.leftlayout.remove_widget(self.bg_image_default)
            self.leftlayout.remove_widget(self.bg_image)
        except:
            pass
            
        imageNumber = randint(1,4)
        imageStr = assetsdirectory+str('sandstone_')+str(imageNumber)+'.png'
        self.bg_image = Image(source=imageStr)
        self.bg_image.allow_stretch = True
        self.bg_image.keep_ratio = False
        self.bg_image.size_hint_x = .7
        self.bg_image.size_hint_y = 1
        self.bg_image.pos = (0, 0)
        self.bg_image.opacity = 0.6
        #self.bg_image.reload()
        
        self.leftlayout.add_widget(self.bg_image)
        
        #print('The background image has updated')
                
        
class DrawingApp(Widget):
    
    x_bounds = 890 #InteractionScreen.leftlayout.width
    x_initial = NumericProperty(0)
    y_initial = NumericProperty(0)
    x_final = NumericProperty(0)
    y_final = NumericProperty(0)
    #x_delta = NumericProperty(0)
    #y_delta = NumericProperty(0)
    #angle = NumericProperty(0)
    out_of_bounds = ObjectProperty(None)
    #SOMETHING HERE TO REFERENCE INTERACTION SCREEN?
    
    def __init__(self, **kwargs):
        super(DrawingApp, self).__init__(**kwargs)
        
    
    #User Touch Events
    def on_touch_down(self, touch):
        
        with self.canvas:
            
            if touch.x > self.x_bounds:
                self.out_of_bounds = True
                #print ('Touch down event out of bounds with x > %s \n' %(self.x_bounds))
                pass	        
	        
            elif touch.x < self.x_bounds:
                self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                #self.vector_length(touch.ud['line'])
                self.x_initial = touch.x
                self.y_initial = touch.y
                self.out_of_bounds = False
                print ('This is the initial x value: %s, \nThis is the initial y value: %s \n\n' %(self.x_initial, self.y_initial))				

                
    def on_touch_move(self, touch):
        with self.canvas:
            
            length = np.sqrt((touch.x - self.x_initial)**2 + (touch.y - self.y_initial)**2)
            frac_x = (touch.x - self.x_initial) / length
            frac_y = (touch.y - self.y_initial) / length
            
            if touch.x <= self.x_bounds and self.out_of_bounds == False and (length < 200):
                self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = touch.x
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, touch.x, touch.y])
                
            elif touch.x > self.x_bounds and self.out_of_bounds == False and (length < 200):
                self.canvas.clear()
                d = 10
                Ellipse(pos=(self.x_bounds - d/2, touch.y - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = self.x_bounds
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x < self.x_bounds and self.out_of_bounds == False and (length > 200):
                self.canvas.clear()
                d = 10
                self.x_final = self.x_initial + int(round((frac_x * 200))) #PYTHON 3 DEFAULTS TO FLOAT
                self.y_final = self.y_initial + int(round((frac_y * 200))) #PYTHON 2 DOESN'T REQUIRE INT() 
                Ellipse(pos=(self.x_final - d/2, self.y_final - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))                
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x > self.x_bounds and self.out_of_bounds == True:
                print ('Touch move out of bounds')
                pass
                
            elif touch.x <= self.x_bounds and self.out_of_bounds == True:
                pass
                
    def on_touch_up(self, touch):
        
        with self.canvas:
              
            length = np.sqrt((touch.x - self.x_initial)**2 + (touch.y - self.y_initial)**2)
            frac_x = (touch.x - self.x_initial) / length
            frac_y = (touch.y - self.y_initial) / length
                
            if touch.x <= self.x_bounds and self.out_of_bounds == False and (length < 200) :
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                Line(points=[self.x_initial, self.y_initial, touch.x, touch.y])
                
            elif touch.x > self.x_bounds and self.out_of_bounds == False and (length < 200):
                self.canvas.clear()
                d = 10
                Ellipse(pos=(self.x_bounds - d/2, touch.y - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = self.x_bounds
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
            
            elif touch.x < self.x_bounds and self.out_of_bounds == False and (length > 200):
                self.canvas.clear()
                d = 10
                self.x_final = self.x_initial + int(round((frac_x * 200))) #PYTHON 3 DEFAULTS TO FLOATS
                self.y_final = self.y_initial + int(round((frac_y * 200))) #PYTHON 2 DOESN'T REQUIRE INT()
                Ellipse(pos=(self.x_final - d/2, self.y_final - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))                
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x > self.x_bounds and self.out_of_bounds == True:
                print ('Touch up out of bounds')
                pass
                
            elif touch.x <= self.x_bounds and self.out_of_bounds == True:
                pass
                
    
        
class TestApp(App):
    
    def build(self):
        sm = ScreenManager() #screenmanager module used for changing screens
        sc1 = WelcomeScreen(name='screen1')
        sc2 = InteractionScreen(name='screen2')
        sc3 = AboutScreen(name='screen3')
        sc4 = UiowaScreen(name='screen4')
        sm.add_widget(sc1) #builds the app screen by screen
        sm.add_widget(sc2)
        sm.add_widget(sc3)
        sm.add_widget(sc4)
        print (sm.screen_names)
        return sm
        
if __name__ == '__main__':
    TestApp().run()
