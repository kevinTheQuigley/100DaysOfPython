#Built for the maze here:- https://reeborg.ca/reeborg.html
#Following the "Always turn left principal"

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if (wall_in_front() and right_is_clear()):
        turn_right()
        move()
    elif (right_is_clear()):
        turn_right()
        move()
    elif(wall_in_front()):
        turn_left()

    else:
        move()