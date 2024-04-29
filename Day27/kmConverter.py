import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width = 500, height=300)
window.config(padx=30,pady=30)

userIn = tkinter.Entry(width = 10)
userIn.grid(column = 2,row  = 1)

mi_label = tkinter.Label(text= "Miles", font= ("Arial", 12))
mi_label.grid(column = 3,row  = 1)

#Secong line
eq_label = tkinter.Label(text= "is equal to ", font= ("Arial", 12))
eq_label.grid(column = 1,row  = 2)

my_label = tkinter.Label(text= "0", font= ("Arial",12))
my_label.grid(column = 2,row  = 2)

km_label = tkinter.Label(text= "Km", font= ("Arial", 12))
km_label.grid(column = 3,row  = 2)

print(userIn.get())

def button_clicked():
    Mi = int(userIn.get())
    km = round(Mi * 1.6)
    

    my_label.config(text= km)
    
#my_label.pack(expand = 1)




button = tkinter.Button(text= "Convert", command = button_clicked)
button.grid(column = 2,row  = 3)

window.mainloop()