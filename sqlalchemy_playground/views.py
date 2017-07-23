from flask import escape

from .app import app, db
from .models import User, Post, Category

@app.route('/')
def index():
    users = User.query.all()
    admin = User.query.filter_by(username='admin').first()
    return escape(str(users)) + '<br>' + escape(str(admin))

@app.route('/posts/')
@app.route('/posts/<category_name>')
def posts(category_name=None):
    if category_name is None:
        posts = Post.query.all()
        return escape(str(posts))
    else:
        category = Category.query.filter_by(name=category_name).first()
        if category is None:
            return 'No Posts'
        else:
            return escape(str(category.posts.all()))
