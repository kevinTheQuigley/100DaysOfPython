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
data = pandas.read_csv("data/words_to_learn.csv")
# Start with card front
canvas = Canvas(height=526, width=800)
canvas.grid(row=0, column=0,columnspan = 2)

card_front = PhotoImage(file="images\\card_front.png")
card_back = PhotoImage(file="images\\card_back.png")

#asdf
canvas_image = canvas.create_image(426, 300, image=card_front)
#rd_data =  data.loc[random.randint(0,100)]
#rd_start = rd_data['French']


#bottom_text = canvas.create_text(400,263, text = rd_start,fill = "black",font =BOTTOM_FONT_NAME )
top_text_start = canvas.create_text(400,150, text = "French",fill = "black",font =TOP_FONT_NAME )
#top_text_end = canvas.create_text(400,150, text = "English",fill = "black",font =TOP_FONT_NAME )

bottom_text = canvas.create_text(400,263, text = "start",fill = "black",font =BOTTOM_FONT_NAME )

#canvas.itemconfig(timer_text,text  = time.strftime("%M:%S",time.gmtime(count)))
data_dict = {}
rd_data = {}
def refresh_cards():
    global canvas
    global top_text_start
    global card_front
    global card_back
    global canvas_image	
    global window
    global data_dict
    if 'window_after' in globals():
        window.after_cancel(window_after)
    global flip_back
    rd_data =  data.loc[random.randint(0,100)]
    data_dict = rd_data
    rd_start = rd_data['French']
    canvas.itemconfig(bottom_text,text =  rd_start, fill = "black")
    canvas.itemconfig(top_text_start,text =  "French", fill = "black")
    canvas.itemconfig(canvas_image,image =card_front   )

    window_after = window.after(3000,flip_back,rd_data)
    #global window_after

#refresh_cards()
def flip_back(rd_data):
    global canvas
    global bottom_text
    canvas.itemconfig(canvas_image,image =card_back)
    try: 
        rd_end = rd_data['English']
    except(KeyError):
        pass
        

    canvas.itemconfig(bottom_text,text =  rd_end,fill = "white")
    canvas.itemconfig(top_text_start,text =  "English", fill = "white")

    #window.after_cancel()

def right_button_click():
    global data
    global rd_data
    try:
        data =data.drop(index = rd_data["French"] )
        data.to_csv("data/words_to_lean.csv",index = False)
        print(len(data))
    except(KeyError):
        pass
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