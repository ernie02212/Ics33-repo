# The Hunter class is derived from Pulsator first and then Mobile_Simulton.
#   It inherits updating/displaying from Pusator and Mobile_Simulton: it pursues
#   close prey, or moves in a straight line, like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model

class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y,self._width, self._height, angle = 0 , speed = 5)
        self.randomize_angle()

        
    def update(self):
        ate = Pulsator.update(self)
        find = model.find(lambda x: isinstance(x, Prey) and self.distance(x.get_location()) <= 200)
        if find:
            closest = min([i.get_location() for i in find], key = lambda x: self.distance(x))
            x,y = closest
            self.set_angle(atan2(y-self._y, x-self._x))
        self.move()
        return ate
                
            
