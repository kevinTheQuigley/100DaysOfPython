from tkinter import *

# ---------------------------- GLOBALS ------------------------------- #
IMAGE_LOCATION = "./logo.png"
WINDOW_TITLE = "Password Manager"
PASSWORD_LENGTH = 20
FILE_NAME = "passwords.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
# There are 71 characters
def generate_password():
    global password_input
    global CHARACTERS
    global PASSWORD_LENGTH
    char_list = ""
    for i in range(PASSWORD_LENGTH):
        char_list += random.choice(CHARACTERS)
    password_input.insert(0,char_list)

#TODO Save password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_new_password():
    global FILE_NAME
    site= website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_row = site + " | " + email  + " | " + password 
    with open (FILE_NAME,"a") as file:
        file.write(new_row)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(WINDOW_TITLE)
window.config(padx = 20)
window.config(pady = 20)

canvas = Canvas()
theLock = PhotoImage(file = IMAGE_LOCATION )
canvas = Canvas(width = 200,height=200,highlightthickness= 0)
canvas.create_image(100,112,image = theLock)
canvas.grid(column = 1,row = 0)

# ---------------------------- Labels ------------------------------- #
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)


email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# ---------------------------- Inputs ------------------------------- #

website_input = Entry(width =39)
website_input.grid(column = 1,row = 1,columnspan=2)
website_input.focus()

email_input = Entry(width =39)
email_input.grid(column = 1,row = 2,columnspan=2)
email_input.insert(0,"kevinthomassssquigley@gmail.com")

password_input = Entry(width =21)
password_input.grid(column = 1,row = 3)

# ---------------------------- Buttons ------------------------------- #

gen_password = Button(text = "Generate Password",command = generate_password)
gen_password.grid(column = 2,row = 3)

add_password = Button(text = "Add Password",width = 36, command = add_new_password)
add_password.grid(column = 1,row = 4,columnspan=2)

window.mainloop()

