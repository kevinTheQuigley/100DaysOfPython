import tkinter

window = tkinter.Tk()

window.title("le first gui")

window.minsize(width = 500, height=300)
window.config(padx=30,pady=30)
#label 
my_label = tkinter.Label(text= "De label", font= ("Arial", 24, "italic"))
my_label.grid(column = 1,row  = 1)

userIn = tkinter.Entry(width = 10)
userIn.grid(column = 3,row  = 1)

print(userIn.get())

def button_clicked():
    inText = userIn.get()

    my_label.config(text= inText)
    
#my_label.pack(expand = 1)




button = tkinter.Button(text= "Click Me", command = button_clicked)
button.grid(column = 2,row  = 2)

button2 = tkinter.Button(text= "Click Me too", command = button_clicked)
button2.grid(column = 4,row  = 3)
window.mainloop()