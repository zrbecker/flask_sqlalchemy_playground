from .app import app, db
from .models import User, Post, Category

@app.cli.command()
def init_schema():
    db.drop_all()
    db.create_all()

@app.cli.command()
def init_test_data():
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')

    db.session.add(admin)
    db.session.add(guest)

    cat1 = Category('python')
    cat2 = Category('c++')
    p1 = Post('Hello Python!', 'Python is pretty cool', cat1)
    p2 = Post('Hello Python Again!', 'Python is pretty cool', cat1)
    p3 = Post('Hello C++!', 'C++ is pretty cool', cat2)

    db.session.add(cat1)
    db.session.add(cat2)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)

    db.session.commit()
