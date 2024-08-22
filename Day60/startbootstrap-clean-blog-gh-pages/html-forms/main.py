from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['name']) and (request.form['password']):
            return "<h1> Username:" + request.form['name'] + "Password: "+request.form['password'] +"</h1>"
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
    return "submitted"
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
