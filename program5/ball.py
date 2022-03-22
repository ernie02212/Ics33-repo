# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y,width =2*Ball.radius, height = 2*Ball.radius,angle = 0, speed = 5)
        self._x       = x
        self._y       = y
        self.randomize_angle()
    
    def update(self):
        self.move()
        
    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius, self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill="blue")
