import swampy
from swampy.TurtleWorld import *

import math

world = TurtleWorld()
bob = Turtle()
#bob.delay = 0.01  # Speed the little fella

slices = 7
radius = 150
side = 2 * math.pi * radius / slices
angle = 360 / slices / 2
lt(bob, angle)
fd(bob, radius)
lt(bob, angle+90)
fd(bob, side)
lt(bob, angle+90)
fd(bob, radius)

# Doesn't quite return to start but right idea, moving on
wait_for_user()