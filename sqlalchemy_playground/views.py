from flask import escape

from .app import app, db
from .models import User

@app.route('/')
def index():
    users = User.query.all()
    admin = User.query.filter_by(username='admin').first()
    return escape(str(users)) + '<br>' + escape(str(admin))
