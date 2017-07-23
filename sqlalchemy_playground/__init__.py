from .app import app, db

@app.cli.command()
def init_schema():
    db.create_all()

@app.cli.command()
def init_test_data():
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
