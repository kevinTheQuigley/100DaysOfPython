from tkinter import *
from question_model import Question
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
TOP_FONT_NAME = ("arial",20,"italic")
import html


class QuizInterface:
    def __init__(self,question_data,quiz_brain):
        self.question_data = question_data
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)

        self.canvas = Canvas(bg = THEME_COLOR,height=250,width=300)
        self.canvas.grid(column=0,row = 1,columnspan=2)
        self.canvas.config(highlightthickness=0)
        self.mid_text_start = self.canvas.create_text(150,150, text = "Fill",fill = "black",font =TOP_FONT_NAME,width = 280 )
        
        self.top_text = Label(text = "Score:0",font = ("arial",15,"italic"),fg= "white",bg=THEME_COLOR)
        
        self.top_text.grid(column=1,row = 0)

        self.trueImage = PhotoImage(file = "./QuizzlerApp/images/true.png")
        self.true_button = Button(image=self.trueImage, highlightthickness=0,command= self.true_button_click)
        self.true_button.grid(row = 2,column = 0)
        self.falseImage = PhotoImage(file = "./QuizzlerApp/images/false.png")
        self.false_button = Button(image=self.falseImage, highlightthickness=0,command= self.false_button_click)
        self.false_button.grid(row = 2,column = 1)   
        self.get_next_question()




        self.window.mainloop()
        #self.window.config(bg=THEME_COLOR)

    def get_next_question(self):
        self.canvas.config(bg = THEME_COLOR )
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.mid_text_start,text = q_text)

    def false_button_click(self):
        
        res= self.quiz.check_answer("False")
        self.top_text.config(text = f"Score:{self.quiz.score}")
        self.update_score(res)

        #self.get_next_question()

    def update_score(self,boo):
        if boo:
            #self.quiz.score +=1
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.get_next_question)


    def true_button_click(self):
        res= self.quiz.check_answer("True")
        self.top_text.config(text = f"Score:{self.quiz.score}")
        self.update_score(res)
