from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hellow_world():
    return("hello, world")


@app.route("/<name>")
def hellow_name(name):
    return(f"hello, {name+12}")


if __name__ == "__main__":
    app.run(debug = True)


if __name__ == "__main__":
    app.debug= True