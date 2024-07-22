from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

print("Running application in " + __name__)

'''
@app.route("/")
def returnHomepage():
    t1 = datetime.now()
    year1 = t1.strftime("%Y")
    #return("<h1>Hello World</h1>")
    return(render_template("index.html",year = year1))

'''
@app.route("/guess/<string:name>")
def returnGuess(name):
    nameGender= requests.get(f"https://api.genderize.io?name={name}")
    nameGender = nameGender.json()["gender"]

    nameAge= requests.get(f"https://api.agify.io?name={name}")
    nameAge = nameAge.json()["age"]
    
    return(render_template("guessName.html",name = name,age = nameAge, gender = nameGender))

@app.route("/blog")
def returnBlog():
    request = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = request.json()
    print(blogs[0]['id'])
    return(render_template("blog.html",blogs = blogs))

if __name__=="__main__":
    app.run(debug = True)

    
