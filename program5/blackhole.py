# This Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class Prey derived class) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and it displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter
import model
from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, width = 2*Black_Hole.radius , height= 2*Black_Hole.radius)

    def update(self):
        z = model.find(lambda x: self.contains(x.get_location()) and isinstance(x,Prey))
        for i in z:
            model.remove(i)
        return z
    def contains(self,xy):
        if self.distance(xy) <= self.get_dimension()[1]/2:
            return self.distance(xy) <= self.get_dimension()[1]/2
    
    def display(self, canvas):
        rad  = self.get_dimension()[1]/2
        canvas.create_oval(self._x-rad, self._y-rad,
                                self._x+rad, self._y+rad,
                                fill="black")
