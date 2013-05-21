import swampy
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001  # Speed the little fella

import polygon
from polygon import *

def petals(t, arc_angle, turn_centre, petals):
	turn_tip = 180-arc_angle
	radius = 10000 / arc_angle
	for i in range(petals):
		arc(t, r=radius, angle=arc_angle)
		lt(t, turn_tip)
		arc(t, r=radius, angle=arc_angle)
		lt(t, turn_centre)

def flower1(t):
	petals = 7
	arc_angle = 360/petals
	turn_centre = 180/petals
	petals(t, arc_angle, turn_centre, petals)

def flower2(t):
	petals = 10
	arc_angle = 360/(petals/2) # Petals don't overlap
	turn_centre = 0
	petals(t, arc_angle, turn_centre, petals)
		
def flower3(t):
	petals = 20
	arc_angle = int(360/petals)
	turn_centre = 180
	petals(t, arc_angle, turn_centre, petals)		

flower3(bob)

world.canvas.dump() # Note way of printing screen

wait_for_user()