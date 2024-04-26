import turtle
import pandas as pd
from states import StateHeader

IMAGE_PATH =  "blank_states_img.gif"
CSV_PATH = "./50_states.csv"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
screen.listen()


def get_mouse_click_coor(x,y):
    print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)

statesCsv = pd.read_csv(CSV_PATH)

    
statesUpper = statesCsv["state"]
states = []
for state in statesUpper:
    states.append(state.lower())

statesCsv.insert(3, "statesLower", states, True)



GAME_ON = True
print(statesCsv["statesLower"])

while GAME_ON == True:
    answer_state = screen.textinput(title = "Guess the States", prompt = "Guess a state name").lower()
    if answer_state in states:
        print("Well done")
        xPos = int(statesCsv.loc[statesCsv["statesLower"]==answer_state]['x'])
        yPos = int(statesCsv.loc[statesCsv["statesLower"]==answer_state]['y'])

        stateHeader  = StateHeader()
        stateHeader.setPosition(answer_state,xPos,yPos)
    screen.update()
        




turtle.mainloop()

#screen.exitonclick()