from flask import Flask,render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def hellow_world():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)


if __name__ == "__main__":
    app.debug= True