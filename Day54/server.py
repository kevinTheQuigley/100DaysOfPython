from flask import Flask, render_template
app = Flask(__name__)
from random import randint

daNum = randint(0,9)

print(__name__)


introStr = "<h1>Guess a number between 0 and 9!</h1>"\
    "<p><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></p>"

@app.route('/')
def hellow_world():
    return(introStr)


@app.route('/<int:num>')
def check_num(num):
    if daNum == int(num):
        return("<h1>Correct! You win!</h1>")
    else:
        return("<h1>Wrong! You lose!</h1>")
    
if __name__ == "__main__":
    app.run(debug = True)