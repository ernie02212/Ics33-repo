from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree
import random

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
x = 0
def create_random(y):
    global x 
    x = random_graph(y, lambda y:y*10)

y = 1000
while y <= 128000:
    p = Performance(lambda: spanning_tree(x), lambda: create_random(y), 5, "\nSpanning Tree of size {}".format(y))
    p.evaluate()
    p.analyze()
    y*=2