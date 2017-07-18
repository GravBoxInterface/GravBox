class DrawingApp(Widget):
    
    x_initial = NumericProperty(0)
    y_initial = NumericProperty(0)
    x_final = NumericProperty(0)
    y_final = NumericProperty(0)
    out_of_bounds = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DrawingApp, self).__init__(**kwargs)
    
    #User Touch Events
    
    def on_touch_down(self, touch):
        with self.canvas:
            if touch.x > 890:
                self.out_of_bounds = True
                print ("Touch down out of bounds")
                pass
	        
            else:
		self.canvas.clear()
		self.out_of_bounds = False
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_initial = touch.x
                self.y_initial = touch.y			

                
    def on_touch_move(self, touch):
        with self.canvas:
            
            length = np.sqrt((touch.x - self.x_initial)**2 + (touch.y - self.y_initial)**2)
            frac_x = (touch.x - self.x_initial) / length
            frac_y = (touch.y - self.y_initial) / length
            
            if touch.x <= 890 and self.out_of_bounds == False and (length < 200):
		self.canvas.clear()
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = touch.x
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, touch.x, touch.y])
                
            elif touch.x > 890 and self.out_of_bounds == False and (length < 200):
                self.canvas.clear()
                d = 10
                Ellipse(pos=(890 - d/2, touch.y - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = 890
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x < 890 and self.out_of_bounds == False and (length > 200):
                self.canvas.clear()
                d = 10
                self.x_final = self.x_initial + round((frac_x * 200))
                self.y_final = self.y_initial + round((frac_y * 200))
                Ellipse(pos=(self.x_final - d/2, self.y_final - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))                
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x > 890 and self.out_of_bounds == True:
                print ('Touch move out of bounds')
                pass
                
            elif touch.x <= 890 and self.out_of_bounds == True:
                pass
                
    def on_touch_up(self, touch):
        with self.canvas:
            
            length = np.sqrt((touch.x - self.x_initial)**2 + (touch.y - self.y_initial)**2)
            frac_x = (touch.x - self.x_initial) / length
            frac_y = (touch.y - self.y_initial) / length
                
            if touch.x <= 890 and self.out_of_bounds == False and (length < 200) :
                d = 10
                Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                Line(points=[self.x_initial, self.y_initial, touch.x, touch.y])
                
            elif touch.x > 890 and self.out_of_bounds == False and (length < 200):
                self.canvas.clear()
                d = 10
                Ellipse(pos=(890 - d/2, touch.y - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))
                self.x_final = 890
                self.y_final = touch.y
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
            
            elif touch.x < 890 and self.out_of_bounds == False and (length > 200):
                self.canvas.clear()
                d = 10
                self.x_final = self.x_initial + round((frac_x * 200))
                self.y_final = self.y_initial + round((frac_y * 200))
                Ellipse(pos=(self.x_final - d/2, self.y_final - d/2), size = (d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))                
                Line(points=[self.x_initial, self.y_initial, self.x_final, self.y_final])
                
            elif touch.x > 890 and self.out_of_bounds == True:
                print ('Touch up out of bounds')
                pass
                
            elif touch.x <= 890 and self.out_of_bounds == True:
                pass
