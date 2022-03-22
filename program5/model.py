import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball      import Ball
from blackhole import Black_Hole
from floater   import Floater
from hunter    import Hunter
from pulsator  import Pulsator 
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simultons       = set()
k = ""



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    simultons   = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running
    if running == True:
        update_all()
        stop()
    else:
        start()
        update_all()
        stop()
        
        
    
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global k 
    k = kind
    
#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if k == "Remove":
        for z in find(lambda z:z.contains((x,y))):
            simultons.remove(z)
    elif k == "Floater":
        simultons.add(Floater(x,y))
    elif k == "Ball":
        simultons.add(Ball(x,y))
    elif k == "Black_Hole":
        simultons.add(Black_Hole(x,y))
    elif k == "Hunter":
        simultons.add(Hunter(x,y))
    elif k == "Special":
        simultons.add(Special(x,y))
    elif k == "Pulsator":
        simultons.add(Pulsator(x,y))
        
        

#add simulton s to the simulation
def add(s):
    global balls
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    s = set()
    for x in simultons:
        if p(x) == True:
            s.add(x)
    return s


#For each simulton in model's simulation, call update on it, passing along model
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton's update do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in list(simultons):
            b.update()
    
        

#Animation: (a) delete all simultons on the canvas; (b) call display on all
#  simultons being simulated, adding back each to the canvas, often in a new
#  location; (c) update the label defined in the controller showing progress 
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in simultons:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" balls/"+str(cycle_count)+" cycles")
