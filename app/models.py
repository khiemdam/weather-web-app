from .extensions import db

class User(db.Model):
    id = id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000), nullable = False)
    
    tasks = db.relationship("Task", back_populates="user")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.ForeignKey("user.id"))
    name = db.Column(db.String(1000), nullable = False)
    categ = db.Column(db.String(20), nullable = True)
    month = db.Column(db.Integer, nullable = True)
    day = db.Column(db.Integer, nullable = True)
    year = db.Column(db.Integer, nullable = True)

    user = db.relationship("User", back_populates="tasks")