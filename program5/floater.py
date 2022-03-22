# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL import PhotoImage
from prey import Prey
from random import random
import math,random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y,width = 2*Floater.radius, height = 2*Floater.radius, angle = 0, speed = 5)
        self._x       = x
        self._y       = y
        self.randomize_angle()
    
    def update(self):
        random_angle = random.uniform(-0.5,0.5)
        random_speed = random.uniform(-0.5,0.5)
        range_init = 3
        range_end = 7
        if random.random() <= 0.3:
            self._speed += random_speed
            self._angle += random_angle
            while not range_init <= self._speed <= range_end:
                self._speed += random_speed
        self.move()
            
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill="red")

