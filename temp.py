from cs１robots import *
create_world()

hubo = Robot(beepers = 1)

ami = Robot("yellow")
hubo = Robot("gray")
tim = ami
ami = Robot("gray")
hubo = tim
hubo.move()