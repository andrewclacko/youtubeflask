from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Andrew Clark',
        'title': 'Blog Post 1',
        'content': 'This is my first post',
        'date_posted': 'January 15, 2019'  
    },
    {
        'author': 'Lewis Clark',
        'title': 'Blog Post 2',
        'content': 'This is my second post',
        'date_posted': 'January 16, 2019' 
    },
        {
        'author': 'Kelly Clark',
        'title': 'Blog Post 4',
        'content': 'This is my fourth post',
        'date_posted': 'January 10, 2019' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)