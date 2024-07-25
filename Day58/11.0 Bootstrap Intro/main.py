from flask import Flask, render_template
import requests

app = Flask(__name__)
print("Running application in " + __name__)

@app.route("/")
def home():
    return(render_template("index.html"))

if __name__ == "__main__":
    print("Running application")
    app.run(debug = True)
