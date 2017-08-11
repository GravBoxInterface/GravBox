from kivy.config import Config
Config.set('graphics', 'resizeable', 0) #don't make the app resizeable
Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # remove multitouch (red circle on right click, now both clicks draw vectors)
Config.set('graphics', 'position', 'custom')

from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty, BoundedNumericProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.spinner import Spinner

from time import sleep
import os
import os.path
import numpy as np

# Configuration values
#Graphics fix
Window.size = (1920, 1200)
#Window.fullscreen = True
Window.clearcolor = (0, 0, 0, 1.) #fixes drawing issues on some phones

#CURRENT FILEPATH FOR ALL IMAGES/ASSETS -- Comment the ones you don't need
assetsdirectory = r''   #Mason PC
#assetsdirectory = r'C://Users/Erin/Destop/GravBox-master/'  #Erin PC
#assetsdirectory = r'/home/SOMETHING HERE '                  #LINUX BUILDOZER
#assetsdirectory = r'SOMETHING/EMULATED/0?'                  #TABLET

#os.chdir(assetsdirectory)

class MyButton(Button): #use for uniform button styles

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.015 #setting font size
        
class Particle(Widget): #Particle object
    
    def __init__(self, pos, size):
        super(Particle, self).__init__(pos=pos, size=size)
        with self.canvas:
            Color(1,1,1)
            self.ellipse = Ellipse(pos=pos, size=size) #particle is a white ellipse
        self.bind(pos = self.updatePosition) #binds the updatePosition function to the canvas position
        
    def updatePosition(self, *args):    #updatePosition function to change the position of the particle
        self.ellipse.pos = self.pos
        
class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, 0, .5, 0.25)
            Rectangle(pos=self.pos, size=self.size)   

class WelcomeScreen(Screen):
    
    buttonList = ['START YOUR JOURNEY', 'ABOUT', 'UIOWA', 'BACK'] #list of buttons, used for naming 
    
    welcomeImage = assetsdirectory+str('Gravity-Sandbox-homescreen_1_1920x1200.jpg') #WELCOME SCREEN BACKGROUND IMAGE PATH
    #welcomeImage = assetsdirectory+str('Gravity-Sandbox-homescreen.jpg') #WELCOME SCREEN BACKGROUND IMAGE PATH
    
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        layout = FloatLayout() #Float Layout for positioning buttons and image anywhere on the screen
        layout.width = Window.width #the float layout is the size of the window
        layout.height = Window.height
        layout.x = Window.width/2 - layout.width/2 #sets the x position of the layout to 0
        layout.y = Window.height/2 - layout.height/2 #sets the y position of the layout to 0
        self.add_widget(layout) #adds the layout to the screen
        
        img = Image(source = self.welcomeImage) #BACKGROUND IMAGE
        img.size = (Window.width*1.0, Window.height*1.0)
        img.pos = (-Window.width*0.0, -Window.height*0.0)
        img.opacity = 1.0 #alpha value between 0.0 - 1.0
        self.add_widget(img) #adds the image to the screen
                
        startBtn = MyButton(text = '') #start button
        startBtn.size_hint = (.21, .09)
        startBtn.pos_hint ={'x': .395, 'y': .24}
        startBtn.background_color = [.4, .4, .4, .4] #backgroundcolor of the button (this is grayish)
        startBtn.bind(on_release = self.changer) #when the button is released the changer function is called
        self.add_widget(startBtn) #adds the button called startButton to the floatlayout

        aboutBtn = MyButton(text = '') #about button
        aboutBtn.size_hint = (.08, .095)
        aboutBtn.pos_hint ={'x': .618, 'y': 0}
        aboutBtn.background_color = [.4, .4, .4, .4]
        aboutBtn.bind(on_release = self.about) #when the button is released the about function is called
        self.add_widget(aboutBtn) #adds the button called aboutBtn to the floatlayout
               
        uiowaBtn = MyButton(text = '') #uiowa button
        uiowaBtn.size_hint = (.08, .095)
        uiowaBtn.pos_hint = {'x':.7, 'y': 0}
        uiowaBtn.background_color = [.4, .4, .4, .4]
        uiowaBtn.bind(on_release = self.uiowa) #when the button is released the uiowa function is called
        self.add_widget(uiowaBtn) #adds the button called uiowaBtn to the floatlayout
        
    def changer(self, *args): #the changer function
        self.manager.current = 'screen2' #sets the current screen to screen2 - the interaction screen
        self.manager.transition.direction = 'left'

    def about(self, instance): #the about function
        self.manager.current = 'screen3' #sets the current screen to screen3 - the about screen
        self.manager.transition.direction = 'left'
        
    def uiowa(self, instance): #the uiowa function
        self.manager.current = 'screen4' #sets the current screen to screen4 - the uiowa screen
        self.manager.transition.direction = 'left'       
    
class AboutScreen(Screen):
    
    aboutImage = assetsdirectory+str('gray_star.png') #ABOUT SCREEN BACKGROUND IMAGE 
    
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        layout.width = Window.width
        layout.height = Window.height
        layout.x = Window.width/2 - layout.width/2
        layout.y = Window.height/2 - layout.height/2
        self.add_widget(layout)
        
        img = Image(source = self.aboutImage)
        img.size = (Window.width*1.0, Window.height*1.0)
        img.pos = (-Window.width*0.0, -Window.height*0.0)
        img.opacity = 0.4
        self.add_widget(img)
        
        aboutText = Label(text= 'GravBox is the interface application for the Augmented Reality (AR) Sandbox for gravitational dynamics simulations designed and built\nby Dr. Hai Fu\'s Introduction to Astrophysics class during the 2016-2017 academic year and beyond.\nGravBox itself was designed by Zachary Luppen, Erin Maier, and Mason Reed.\n\nAR Sandbox is the result of an NSF-funded project on informal science education for freshwater lake and watershed science developed by the\nUC Davis\' W.M. Keck Center for Active Visualization in the Earth Sciences (KeckCAVES),\ntogether with the UC Davis Tahoe Environmental Research Center, Lawrence Hall of Science, and ECHO Lake Aquarium and Science Center.', halign='center', valign='middle')
        aboutText.pos = (.25, .25)
        self.add_widget(aboutText)
                
        backBtn = MyButton(text = 'BACK') # back button
        backBtn.size_hint = (.1, .1)
        backBtn.pos_hint ={'x': 0, 'y': .90}
        backBtn.background_color = [.4, .4, .4, 1]
        backBtn.bind(on_release = self.backButton) #when the button is released the callback function is called
        self.add_widget(backBtn)
        
    def backButton(self, *args): # returns to screen1 - interaction screen     
        self.manager.current = 'screen1'
        self.manager.transition.direction = 'right'     
        
class UiowaScreen(Screen):
    
    uiowaImage = assetsdirectory+str('gold_star.png') #UIOWA SCREEN BACKGROUND IMAGE

    def __init__(self, **kwargs):
        super(UiowaScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        layout.width = Window.width
        layout.height = Window.height
        layout.x = Window.width/2 - layout.width/2
        layout.y = Window.height/2 - layout.height/2
        self.add_widget(layout)
        
        img = Image(source = self.uiowaImage)
        img.size = (Window.width*1.0, Window.height*1.0)
        img.pos = (-Window.width*0.0, -Window.height*0.0)
        img.opacity = 0.4
        self.add_widget(img)
        
        aboutText = Label(text='UIOWA INFO HERE')
        aboutText.pos = (.25, .25)
        self.add_widget(aboutText)
                
        backBtn = MyButton(text = 'BACK') #start button
        backBtn.size_hint = (.1, .1)
        backBtn.pos_hint ={'x': 0, 'y': .9}
        backBtn.background_color = [.4, .4, .4, 1]
        backBtn.bind(on_release = self.backButton) #when the button is released the backButton function is called
        layout.add_widget(backBtn)
        
    def backButton(self, *args):
        self.manager.current = 'screen1'   
        self.manager.transition.direction = 'right'    
        
class InteractionScreen(Screen): #This is the main screen for drawing and user input. Next steps include nesting layouts and adding/binding buttons
    
    def __init__(self, **kwargs):
        super(InteractionScreen, self).__init__(**kwargs)
        
        ### CREATE LAYOUTS
        
        self.layout = FloatLayout() #creates a Float Layout called self.layout  (self. allows reference for entire class?)
        self.layout.width = Window.width
        self.layout.height = Window.height
        self.layout.x = 0
        self.layout.y = 0

        self.rightlayout = FloatLayout() #creates Float Layout for object selector, speed and angle labels, go button
        self.rightlayout.width = self.layout.width*(1./6.)
        self.rightlayout.height = self.layout.height
        self.rightlayout.x = Window.width - self.rightlayout.width
        self.rightlayout.y = Window.height/2 - self.rightlayout.height/2
        
        self.leftlayout = FloatLayout() # float layout for drawing area and background images
        self.leftlayout.width = self.layout.width * (5./6.)
        self.leftlayout.height = self.layout.height
        self.leftlayout.x = 0  #Window.width - self.centerlayout.width
        self.leftlayout.y = 0 #Window.width/2 - self.centerlayout.height/2         
            
        with self.rightlayout.canvas: #sets canvas instructions for the rightlayout and draws a blue rect. filling the entire layout
            Color(0, 0, .5, 1) #BLUE
            Rectangle(pos=(self.rightlayout.x, self.rightlayout.y), size=(self.rightlayout.width, self.rightlayout.height))    

        ### LEFT LAYOUT CONTENT 
        
        # DRAWING FUNCTIONALITY
        global drawUtility
        drawUtility = DrawingApp()
        drawUtility.size_hint = (5./6., 1)
        self.leftlayout.add_widget(drawUtility, 0)
        self.layout.add_widget(self.leftlayout, 2)                                 
        self.layout.add_widget(self.rightlayout)
        self.add_widget(self.layout)
        
        # DEFAULT BACKGROUND IMAGE
        self.bg_image_default = Image(source=assetsdirectory+str('starfield.jpg'))
        self.bg_image_default.allow_stretch = True
        self.bg_image_default.keep_ratio = False
        self.bg_image_default.size_hint = ((5./6.), 1)
        self.bg_image_default.pos = (0,0)
        self.bg_image_default.opacity = 1.0
        self.leftlayout.add_widget(self.bg_image_default, 1) #ADDS DEFAULT BACKGROUND IMAGE
        
        # BACKGROUND IMAGE UPDATE FUNCTION
        self.imageNumber = 1    #default image number 
        self.event = Clock.schedule_interval(self.imageUpdate, 1.0/5.0) #SCHEDULES THE IMAGE UPDATING TO OCCUR
        
        # HOME BUTTON AND IMAGE
        homeBtn = Button(text='', size_hint=((1./24.), (.06)), pos_hint={'x':0, 'y':.94}, opacity=.5) #back button to the interaction screen
        homeBtn.bind(on_press=self.changer) #binds this button to change the screen back to the welcome screen
        self.layout.add_widget(homeBtn, 0) #adds the button to the float layout
        
        self.homeImage = Image(source=assetsdirectory+str('home.png')) # adds slightly transparent home icon over the back button 
        self.homeImage.size_hint = ((1./24.), .06)
        self.homeImage.pos_hint = {'x': 0, 'y': .94}
        self.homeImage.opacity = .5
        self.layout.add_widget(self.homeImage)
        
        ### RIGHT LAYOUT CONTENT
                
        # OBJECT BUTTON (Must be in same order for correct layout)       
        objButton = Spinner(text='PLEASE SELECT\nAN OBJECT', halign='center', values=('Particle', 'Planet', 'Comet', 'Star', 'Black Hole', 'Elephant')) # object spinner
        objButton.pos_hint = {'x':0, 'y': .8}
        objButton.size_hint = ((1./6.), .2)
        objButton.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(objButton, 0)
        
        # TOPOGRAPHY TOGGLE SWITCH
        self.topoSwitch = Switch(active = True) # switch to toggle between updating topography and static star field
        self.topoSwitch.pos_hint = {'x': 0, 'y':.6}
        self.topoSwitch.size_hint = ((1./6.),.15)
        self.topoSwitch.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(self.topoSwitch)
        
        self.topoSwitch.bind(active = self.topoChange) # bind switch to topoChange function
        
        # SPEED LABEL
        self.spdLabel = Label(text= 'Speed:\n' + str(drawUtility.speed), halign='center') # label showing current speed
        self.spdLabel.pos_hint = {'x': 0, 'y': .4}
        self.spdLabel.size_hint = ((.1/.6), .2)
        self.spdLabel.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(self.spdLabel)
        
        def update_speed(value, instance): # callback function to bind speed to vector
            self.spdLabel.text = 'Speed:\n' + str(drawUtility.speed)
            
        drawUtility.bind(speed = update_speed) # bind speed to vector length    
        
        # ANGLE LABEL
        self.angLabel = Label(text='Angle:\n' + str(drawUtility.angle), halign='center') # label showing current angle
        self.angLabel.pos_hint = {'x': 0, 'y':.2}
        self.angLabel.size_hint = ((1./6.), .2)
        self.angLabel.background_color = [.4, .4, .4, 1]
        self.rightlayout.add_widget(self.angLabel)
        
        def update_angle(value, instance): # callback function to bind angle to vector
            self.angLabel.text = 'Angle:\n' + str(drawUtility.angle)
            
        drawUtility.bind(angle = update_angle)  # bind angle to vector                
                        
        # GO BUTTON
        self.goButton = MyButton(text = 'Go!') # go button to send user input to algorithm
        self.goButton.pos_hint = {'x':0, 'y':0}
        self.goButton.size_hint = ((1./6.), .2)
        self.goButton.background_color = [.4, .4, .4, 1]
        self.goButton.bind(on_release = self.userInput) # when the button is released the USERINPUT function is called
        self.rightlayout.add_widget(self.goButton) 
        
    ### FUNCTIONS  
                        
    def massSelect(self, *args):
        print('Mass Selector Function called')
        
    def userInput(self, *args): # function to save user input and take output from algorithm
        
        name_of_file = 'algorithm_input'# USER INPUT FILENAME
        inputFileName = os.path.join(assetsdirectory, name_of_file+'.txt') #TOTAL PATH NAME
        
        with open(inputFileName, 'w') as f: # create file and write initial and final coordinate positions
            f.write('%f\t%f\t%f\t%f' % (drawUtility.x_initial, drawUtility.y_initial, drawUtility.x_final, drawUtility.y_final))
	            
        drawUtility.canvas.clear()
        particle = Particle(pos = (drawUtility.x_initial, drawUtility.y_initial), size = (10, 10)) # draw a particle at chosen initial position
        drawUtility.add_widget(particle)    
	
        while os.path.isfile('algorithm_output.npy') == False: # search for output file
            sleep(1)
            print ("Still no file")
        else:
            x = np.load('mylistx.npy'); xs = np.split(x, len(x)/200, 0) # test data
            y = np.load('mylisty.npy'); ys = np.split(y, len(y)/200, 0)
            print ("File found!")
	    
	    #x,y = np.load('algorithm_output.npy') # load in algorithm output
	    #xs = np.split(x, len(x)/200, 0); ys = np.split(y, len(y)/200, 0) # split x and y arrays into manageable chunks for animation

            self.animate(xs, ys, 0, particle) # call animation function with output data
            
    def animate(self, x_coords, y_coords, index, instance): # function to animate particle through orbit
        
        if index < len(x_coords): # check if reached last coordinate chunk
            
            animation = Animation(pos=(int(x_coords[index][0]), int(y_coords[index][0])), t='linear', duration=.02) # create animation instance beginning at first coordinate of chunk
            
            for i in np.arange(1, len(x_coords[index])): # add all points in chunk to animation instance in sequence
                animation += Animation(pos=(int(x_coords[index][i]), int(y_coords[index][i])), t='linear', duration=.02)
                
            animation.bind(on_complete=lambda x, y: (self.animate(x_coords, y_coords, index+1, instance))) # once one chunk is animated, animate next
            animation.start(instance) # begin animation     
        
    def changer(self, *args): # function to go back to home screen
        self.manager.current = 'screen1'
        self.manager.transition.direction = 'right'
        
    def topoChange(self, instance, value): # function for turning updating topography on and off
        
        if self.topoSwitch.active == True: # if topography active, call image update function once every .2 seconds
            self.event = Clock.schedule_interval(self.imageUpdate, 1.0/5.0)
        elif self.topoSwitch.active == False: # if topography not active, 
            self.event.cancel() # cancel clock event
            self.leftlayout.remove_widget(self.bg_image) # remove the updating background image widget
            self.leftlayout.add_widget(self.bg_image_default, 1) # add default image widget

    def imageUpdate(self, dt): # function for live topography updating
        
        #TESTING MULTIPLE IMAGE UPDATE
        try:
            self.leftlayout.remove_widget(self.bg_image_default) # try to remove both image widgets, ensures proper layering of widgets
            self.leftlayout.remove_widget(self.bg_image)
        except:
            pass
            
        self.imageNumber ^= 1
        imageStr = assetsdirectory+str('app_test_')+str(self.imageNumber)+'.jpg' # randomly choose sandstone image
        #print('imageNumber: %s' % self.imageNumber)
        
        self.bg_image = Image(source=imageStr)
        self.bg_image.allow_stretch = True
        self.bg_image.keep_ratio = False
        self.bg_image.size_hint = ((5./6.),1)
        self.bg_image.pos = (0,0)
        self.bg_image.opacity = 1.0
        #self.bg_image.reload()
        
        self.leftlayout.add_widget(self.bg_image, 1) # add topography image widget    
        
class DrawingApp(Widget):
        
    vector_length = NumericProperty(0)
    speed = NumericProperty(0)
    x_bounds = NumericProperty(Window.width * (5./6.))
    x_initial = NumericProperty(0)
    y_initial = NumericProperty(0)
    x_final = BoundedNumericProperty(0, min=0, max=(Window.width * (5./6.)), errorhandler=lambda x: (Window.width * (5./6.)) if x > (Window.width * (5./6.)) else 0)
    y_final = NumericProperty(0)
    angle = NumericProperty(0)
    d = NumericProperty(10)
    out_of_bounds = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DrawingApp, self).__init__(**kwargs)
    
    #User Touch Events
    
    def on_touch_down(self, touch):
        with self.canvas:
            
            if touch.x > self.x_bounds:
                self.out_of_bounds = True	        
            else:
                self.canvas.clear()
                self.out_of_bounds = False
		
                self.x_initial = touch.x
                self.y_initial = touch.y
                
                Ellipse(pos=(self.x_initial - self.d/2, self.y_initial - self.d/2), size=(self.d,self.d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                
                
    def on_touch_move(self, touch):
        with self.canvas:
            
            self.vector_length = round(np.sqrt((touch.x - self.x_initial)**2 + (touch.y - self.y_initial)**2))
            
            if self.vector_length != 0:
                frac_x = (touch.x - self.x_initial) / self.vector_length         
                frac_y = (touch.y - self.y_initial) / self.vector_length
            else:
                frac_x = 0
                frac_y = 0
                
            self.x_final = touch.x
            self.y_final = touch.y
            
            if touch.x <= self.x_bounds and self.out_of_bounds == False and (self.vector_length < 400):
                self.canvas.clear()
                self.x_final = touch.x
                self.y_final = touch.y
                self.speed = round(self.vector_length / 400, 2)

                Ellipse(pos=(self.x_final - self.d/2, self.y_final - self.d/2), size=(self.d,self.d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
                self.angle_calc(self.x_initial, self.y_initial, self.x_final, self.y_final)
                
            elif touch.x > self.x_bounds and self.out_of_bounds == False and (self.vector_length < 400):
                self.canvas.clear()
                
                self.x_final = self.x_bounds
                self.y_final = touch.y
                self.speed = round(self.vector_length / 400, 2)

                Ellipse(pos=(self.x_final - self.d/2, self.y_final- self.d/2), size = (self.d,self.d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
                self.angle_calc(self.x_initial, self.y_initial, self.x_final, self.y_final)
                       
            elif touch.x < self.x_bounds and self.out_of_bounds == False and (self.vector_length > 400):
                self.canvas.clear()
                
                self.x_final = self.x_initial + round((frac_x * 400))
                self.y_final = self.y_initial + round((frac_y * 400))
                self.speed = 1.00
                
                Ellipse(pos=(self.x_final - self.d/2, self.y_final - self.d/2), size = (self.d,self.d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))                
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
                self.angle_calc(self.x_initial, self.y_initial, self.x_final, self.y_final)             
                
            else:
                pass
        
    def angle_calc(self, x1, y1, x2, y2):
        if np.arctan2((y2 - y1), (x2 - x1)) < 0:
            self.angle = int(round(np.rad2deg(np.arctan2((y2 - y1), (x2 - x1))))) + 360
        else: 
            self.angle = int(round(np.rad2deg(np.arctan2((y2 - y1), (x2 - x1)))))  

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
        return sm
        
if __name__ == '__main__':
    TestApp().run()
