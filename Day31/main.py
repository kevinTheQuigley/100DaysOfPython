# Imports
from tkinter import * 
import pandas 
import os
import random
import time


# Globals
BACKGROUND_COLOR = "#B1DDC6"
TOP_FONT_NAME = ("arial",40,"italic")
BOTTOM_FONT_NAME = ("arial",60,"bold")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Setting up the data
data = pandas.read_csv("data/french_words.csv")
print(data)
# Start with card front
canvas = Canvas(height=526, width=800)
canvas.grid(row=0, column=0,columnspan = 2)

card_front = PhotoImage(file="images\\card_front.png")
card_back = PhotoImage(file="images\\card_back.png")
canvas.create_image(426, 300, image=card_front)
bottom_text = canvas.create_text(400,263, text = "French",fill = "black",font =BOTTOM_FONT_NAME )
#canvas.itemconfig(timer_text,text  = time.strftime("%M:%S",time.gmtime(count)))
def refresh_cards():
    global canvas
    global bottom_text
    global card_front
    global card_back
    top_text = canvas.create_text(400,150, text = "French",fill = "black",font =TOP_FONT_NAME )
    rd_data =  data.loc[random.randint(0,100)]
    rd_start = rd_data['French']
    canvas.itemconfig(bottom_text,text =  rd_start)

    time.sleep(3)

    rd_end = rd_data['English']

    canvas.itemconfig(bottom_text,text =  rd_end)

def right_button_click():
    refresh_cards()
    


def wrong_button_click():
    refresh_cards()

right_image = PhotoImage(file = "images\\right.png")
right_button = Button(image=right_image, highlightthickness=0,command= right_button_click)
right_button.grid(row = 1,column = 0)

wrong_image = PhotoImage(file = "images\\wrong.png") 
wrong_button = Button(image=wrong_image, highlightthickness=0, command = wrong_button_click)
wrong_button.grid(row = 1,column = 1)

window.mainloop()