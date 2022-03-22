
from prey import Prey
import random

class Special(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y,width = 2*Special.radius, height = 2*Special.radius,angle = 0, speed = 5)
        self._x = x 
        self._y = y
        self.randomize_angle()
        
    def update(self):
        rand_color = random.choices(range(256), k =3)
        if self.wall_bounce():
            self._color = rand_color
        self.move()
            
    def display(self, canvas):
        canvas.create_oval(self._x-Special.radius, self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill="orange")
