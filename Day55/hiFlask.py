from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hellow_world():
    return("hello, world")


def emphaziser(func):
    def wrapper(name):
        return f"<h1><em>{func(name)}</em></h1>"
    return wrapper

@app.route("/<name>")
@emphaziser
def hellow_name(name):
    return(f"hello, {name}")


if __name__ == "__main__":
    app.run(debug = True)


if __name__ == "__main__":
    app.debug= True