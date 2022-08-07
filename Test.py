# This is a sample Python script.

from cs１robots import *
create_world()


# create a robot with one beeper
hubo = Robot(beepers = 1)

# move one step forward
#hubo.move()

# turn left 90 degrees
#hubo.turn_left()

# turn right 90 degrees
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

# climb up 4 stairs, climb down 4 stairs, drop beeper, turn around
def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()

def climb_down_one_stair():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

# climb up 4 stairs 1. 2
#def climb_up_four_stairs():
#    climb_up_one_stair()
#    climb_up_one_stair()
#    climb_up_one_stair()
#    climb_up_one_stair()

def climb_up_four_stairs():
    for i in range(4):
        climb_up_one_stair()
        for i in range(1000):
            turn_around()


def climb_down_four_stairs():
    for i in range(4):
        climb_down_one_stair()
        for i in range(1000):
            turn_around()


climb_up_four_stairs()
hubo.drop_beeper()

turn_around()

for i in range(1000):
    turn_around()

climb_down_four_stairs()

