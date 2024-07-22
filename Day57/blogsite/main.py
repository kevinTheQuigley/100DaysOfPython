from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    request = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = request.json()
    print(blogs[0]['id'])
    return(render_template("index.html",blogs = blogs))

@app.route('/blogPost/<int:id>')
def get_blog(id):
    request = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = request.json()

    for blog in blogs:
        if blog['id'] == id:
            blog_post = blog
            break

    print(blogs[0]['id'])
    return render_template("post.html",blog = blog, id= id)

if __name__ == "__main__":
    app.run(debug=True)
