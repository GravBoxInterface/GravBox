#######################################
'''
This code is based off the tutorial from:
    https://kivyspacegame.wordpress.com/author/kivyspacegame/
'''



import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.graphics import Rectangle, Color#, Canvas
from functools import partial
from random import randint


from kivy.config import Config
Config.set('graphics', 'resizeable', 0)
#Window.size = (1280, 800)
Window.clearcolor = (0, 0, 0, 1.)

class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.018

class SmartMenu(Widget):
    buttonList = []
    
    def __init__(self, **kwargs):
        self.register_event_type('on_button_release')
        
        super(SmartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
    def on_button_release(self, *args):
            pass
            
    def callback(self, instance):
        self.buttonText = instance.text
        self.dispatch('on_button_release')
            
    def addButtons(self):
        for k in self.buttonList:
            tmpBtn = MyButton(text = k)
            tmpBtn.background_color = [.4, .4, .4, .4]
            tmpBtn.bind(on_release = self.callback)
            self.layout.add_widget(tmpBtn)
            
    def buildUp(self):
        self.addButtons()


class SmartStartMenu(SmartMenu):
    buttonList = ['start', 'about']
    
    def __init__(self, **kwargs):
        super(SmartStartMenu, self).__init__(**kwargs)
        
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
        
        self.msg = Label(text='Asteroid Avoid')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.45, Window.height*0.75)
        self.add_widget(self.msg)
        self.img = Image(source = 'C://Users/Mason/Desktop/Sandbox Kivy/lens2.png')
        self.img.size = (Window.width*1.5, Window.height*1.5)
        self.img.pos = (-Window.width*0.2, -Window.height*0.2)
        self.img.opacity = 0.35
        self.add_widget(self.img)
        

class WidgetDrawer(Widget):

    def __init__(self, imageStr, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)
        with self.canvas:
            self.size = (Window.width*.002*25, Window.width*.002*25)
            self.rect_bg=Rectangle(source=imageStr, pos=self.pos, size=self.size)
            
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x, self.y)
            self.rect_bg.pos = self.pos
            
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value
        
    def setSize(self, width, height):
        self.size = (width, height)
        
    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        

class Asteroid(WidgetDrawer):
    imgStr = 'C://Users/Mason/Desktop/Sandbox Kivy/sandstone_1.png'
    rect_bg= Rectangle(source=imgStr)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y
        
    def update(self):
        self.move()
        
        
class Ship(WidgetDrawer):
    
    impulse = 3
    grav = -0.1
    
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    flameSize = (Window.width*.03, Window.width*.03)
    
    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y
        
        if self.y < Window.height*0.05:
            self.impulse = 1
            self.grav = -0.1
        if self.y > Window.height*0.95:
            self.impulse = -3
            
    def checkBulletNPCCollision(self,j):
        if self.k.collide_widget(j):
            j.health = j.health - self.k.bulletDamage
            j.attackFlag = 'True'
            self.k.age = self.k.lifespan+10
        
    def checkBulletStageCollision(self, q):
        if self.k.collide_widget(q):
            try:
                if q.type == 'asteroid':
                    q.health = q.health - self.k.bulletDamage
                    self.k.age = self.k.lifespan+10
            except:
                print ('couldnt hit asteroid')
        
            
    def determineVelocity(self):
        self.grav = self.grav*1.05
        
        if self.grav < -4:
            self.grav = -4
            
        self.velocity_y = self.impulse + self.grav
        self.impulse = 0.95*self.impulse
        
        
    def drawArrow(self, *largs):
        with self.canvas:
            flamePos = (self.pos[0]-Window.width*0.02, self.pos[1]+Window.width*.01)
            
            flameRect = Rectangle(source='C://Users/Mason/Desktop/Sandbox Kivy/flame1.png', pos=flamePos, size=self.flameSize)
            
            def removeArrows(arrow, *largs):
                self.canvas.remove(arrow)
            Clock.schedule_once(partial(removeArrows, flameRect), .5)
            Clock.schedule_once(partial(self.updateArrows, flameRect), 0.1)
    
    def updateArrows(self, arrow, dt):
        with self.canvas:
            arrow.pos = (arrow.pos[0]-10, arrow.pos[1])
            
            Clock.schedule_once(partial(self.updateArrows, arrow), 0.1)
        return
        
    def explode(self):
        tmpSize = Window.width*0.25, Window.width*0.2
        tmpPos = (self.x-Window.width*0.095, self.y-Window.width*0.08)
        with self.canvas:
            self.explosionRect = Rectangle(source= 'C://Users/Mason/Desktop/Sandbox Kivy/explosion1.png', pos= tmpPos, size= tmpSize)
    
        def changeExplosion(rect, newSource, *largs):
            rect.source = newSource
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, 'C://Users/Mason/Desktop/Sandbox Kivy/explosion2.png'), 0.2)
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, 'C://Users/Mason/Desktop/Sandbox Kivy/explosion3.png'), 0.4)
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, 'C://Users/Mason/Desktop/Sandbox Kivy/explosion4.png'), 0.6)
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, 'C://Users/Mason/Desktop/Sandbox Kivy/explosion5.png'), 0.8)
            
        def removeExplosion(rect, *largs):
            self.canvas.remove(rect)
        Clock.schedule_once(partial(removeExplosion, self.explosionRect), 1)
        
    def update(self):
        self.determineVelocity()
        self.move()
        
                
                                
class GUI(Widget):

    asteroidList = []
    asteroidScore = NumericProperty(0)
    minProb = 1780
    
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        
        self.score = Label(text='0')
        self.score.y = Window.height*0.8
        self.score.x = Window.width*0.2
        
        def check_score(self, obj):
            self.score.text = str(self.asteroidScore)
            self.bind(asteroidScore = check_score)
            self.add_widget(self.score)
        
        self.ship = Ship(imageStr = 'C://Users/Mason/Desktop/Sandbox Kivy/ship.png')
        self.ship.x = Window.width/4
        self.ship.y = Window.height/2
        self.add_widget(self.ship)
        self.ship.drawArrow()
        Clock.schedule_interval((self.ship.drawArrow), 0.1)
        
    def addAsteroid(self):
        imageNumber = randint(1,4)
        imageStr = 'C://Users/Mason/Desktop/Sandbox Kivy/sandstone_'+str(imageNumber)+'.png'
        tmpAsteroid = Asteroid(imageStr)
        tmpAsteroid.x = Window.width*0.99
        
        ypos = randint(1, 16)
        ypos = ypos*Window.height*.0625
        
        tmpAsteroid.y = ypos
        tmpAsteroid.velocity_y = 0
        vel = 55 #random.rand(10,25)
        tmpAsteroid.velocity_x = -0.1*vel
        
        self.asteroidList.append(tmpAsteroid)
        self.add_widget(tmpAsteroid)
        
  
    def drawTouchResponse(self, x, y):
        pass
        '''
        with self.canvas:
            tmpSize = Window.width*0.07, Window.width*0.07
            tmpPos = (x-self.width/4, y-self.height/4)
            self.arrowRect = Rectangle(source='C://Users/Mason/Desktop/Sandbox Kivy/flame1.png', pos=tmpPos, size=tmpSize)
        
        def removeArrows(arrow, *largs):
             self.canvas.remove(arrow)
             
        def changeExplosion(rect, newSource, *largs):
             rect.source = newSource
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame2.png'), 0.15)
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame3.png'), 0.3)
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, 'C://Users/Mason/Desktop/Sandbox Kivy/flame4.png'), 0.45)
        Clock.schedule_once(partial(removeArrows, self.arrowRect), 0.46)
        '''
    
    def on_touch_down(self, touch):
        self.ship.impulse = 3 
        self.ship.grav = -0.1
        self.drawTouchResponse(touch.x, touch.y)
        
    def showScore(self):
        self.scoreWidget = ScoreWidget()
        self.scoreWidget.asteroidScore = self.asteroidScore
        self.scoreWidget.prepare()
        self.add_widget(self.scoreWidget)
        
    def removeScore(self):
        self.remove_widget(self.scoreWidget)
        
    def gameOver(self):
        restartButton = MyButton(text='Restart')
        
        def restart_button(obj):
            self.removeScore()
            print ('restart button pushed')
            for k in self.asteroidList:
                self.remove_widget(k)
                self.ship.xpos = Window.width*0.25
                self.ship.ypos = Window.height*0.8
                self.minProp = 1700
                self.asteroidScore = 0
                self.asteroidList = []
            
            self.parent.remove_widget(restartButton)
            
            Clock.unschedule(self.update)
            Clock.schedule_interval(self.update, 1.0/60.0)
        restartButton.size = (Window.width*.3, Window.width*.1)
        restartButton.pos = Window.width*0.5 - restartButton.width/2, Window.height*0.5
        restartButton.bind(on_release=restart_button)
        
        self.parent.add_widget(restartButton)
        self.showScore()
        
    def update(self, dt):
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
            
class ScoreWidget(Widget):
    def __init__(self, **kwargs):
        super(ScoreWidget, self).__init__(**kwargs)
        self.asteroidScore = 0
        self.currentScore = 0
        with self.canvas:
            tmpPos = (Window.width*0.25, Window.height*0.25)
            tmpSize = (Window.height*0.5, Window.height*0.5)
            Color(0.1, .1, .1)
            self.scoreRect = Rectangle(pos=tmpPos, size= tmpSize)
            
    def prepare(self):
        try:
            self.finalScore = self.asteroidScore*100
        except:
            print ('problems getting score')
        self.animateScore()
        
    def animateScore(self):
        scoreText = 'Score: 0'+str(self.finalScore)
        self.scoreLabel = Label(text=scoreText, font_size = '20sp')
        self.scoreLabel.x = Window.width*0.3
        self.scoreLabel.y = Window.height*0.3
        self.add_widget(self.scoreLabel)
        Clock.schedule_once(self.updateScore, .1)
        self.drawStars()
        
    def updateScore(self, dt):
        self.currentScore = self.currentScore +100
        self.scoreLabel.text = 'Score: ' + str(self.currentScore)
        if self.currentScore < self.finalScore:
            Clock.schedule_once(self.updateScore, 0.1)
            
    def drawStars(self):
        starNumber = 0
        if self.asteroidScore > 10:
            starNumber = 1
        if self.asteroidScore > 50:
            starNumber = 2
        if self.asteroidScore > 75:
            starNumber = 3
        if self.asteroidScore > 100:
            starNumber = 4
        if self.asteroidScore > 150:
            starNumber = 5
            
        with self.canvas:
            starPos = Window.width*0.27, Window.height*0.42
            starSize = Window.width*0.06, Window.width*0.06
            starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gold_star.png'
            if starNumber < 1:
                starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gray_star.png'
            starRectOne = Rectangle(source=starString, pos=starPos, size= starSize)
            
            starPos = Window.width*0.37, Window.height*0.42
            if starNumber < 2:
                starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gray_star.png'
            starRectTwo = Rectangle(source=starString, pos=starPos, size= starSize)
            
            starPos = Window.width*0.47, Window.height*0.42
            if starNumber < 3:
                starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gray_star.png'
            starRectThree = Rectangle(source=starString, pos=starPos, size= starSize)
            
            starPos = Window.width*0.57, Window.height*0.42
            if starNumber < 4:
                starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gray_star.png'
            starRectFour = Rectangle(source= starString, pos= starPos, size= starSize)
            
            starPos = Window.width*0.67, Window.height*0.42
            if starNumber < 5:
                starString = 'C://Users/Mason/Desktop/Sandbox Kivy/gray_star.png'
            starRectFive = Rectangle(source= starString, pos= starPos, size= starSize)
            
            
            
class ClientApp(App):
    
    def build(self):
        self.parent = Widget()
        self.app = GUI()
        #Clock.schedule_interval(app.update, 1.0/60.0)
        #parent.add_widget(app)
        self.sm = SmartStartMenu()
        self.sm.buildUp()
        def check_button(obj):
            if self.sm.buttonText == 'start':
                self.parent.remove_widget(self.sm)
                
                print ('start the game already')
                Clock.unschedule(self.app.update)
                Clock.schedule_interval(self.app.update, 1.0/60.0)
                
                try:
                    self.parent.remove_widget(self.aboutText)
                except:
                    pass

            if self.sm.buttonText == 'about':
                self.aboutText = Label(text= 'ABOUT INFO HERE')
                self.aboutText.pos = (Window.width*0.45, Window.height*0.35)
                self.parent.add_widget(self.aboutText)
        self.sm.bind(on_button_release = check_button)
        self.parent.add_widget(self.sm)
        self.parent.add_widget(self.app)
        return self.parent
        
if __name__=='__main__':
    ClientApp().run()