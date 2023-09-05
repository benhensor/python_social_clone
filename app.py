from flask import Flask, render_template, request
from flask_cors import CORS
# import the create_post and get_posts functions from the models.py file
from models import create_post, get_posts

# create the flask app
app = Flask(__name__)

# define the route for the app and the methods it accepts
@app.route('/', methods=['GET', 'POST'])
# define the index function
def index():
    # if the request method is GET, then pass because we don't need to do anything
    if request.method == 'GET':
        
        pass
    
    # if the request method is POST, then get the name and post from the form and create a post
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    # get the posts from the database
    posts = get_posts()

    # render the index.html template and pass the posts to it
    return render_template('index.html', posts=posts)

# run the app
if __name__ == '__main__':
    app.run(debug=True)