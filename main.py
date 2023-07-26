from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000), nullable = False)
    categ = db.Column(db.String(20), nullable = True)
    month = db.Column(db.Integer, nullable = True)
    day = db.Column(db.Integer, nullable = True)
    year = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f"Video(name = {self.name}, categ = {self.categ}, month = {self.month}, day = {self.day}, year = {self.year})"

db.create_all()

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("name", type = str, help = "Name of task is required", required = True)
task_put_args.add_argument("categ", type = str, help = "Category of task (assignment, event, etc.)")
task_put_args.add_argument("month", type = int, help = "Month task is due")
task_put_args.add_argument("day", type = int, help = "Day task is due")
task_put_args.add_argument("year", type = int, help = "Year task is due")

tasks = {}

# if id is not in tasks dictionary, cannot use get
def abort_if_no_id(task_id):
    if task_id not in tasks:
        abort(404, message = "Task does not exist with that id :(")

def abort_if_is_id(task_id):
    if task_id in tasks:
        abort(404, message = "Task already exists with that id :(")

# request handling
class Task(Resource):
    def get(self, task_id):
        abort_if_no_id(task_id)
        return tasks[task_id]
    def put(self, task_id):
        abort_if_is_id(task_id)
        args = task_put_args.parse_args()
        tasks[task_id] = args
        return tasks[task_id], 201 # 201 means created successfully
    def delete(self, task_id):
        abort_if_no_id(task_id)
        del(tasks[task_id])
        return '', 204 # deleted successfully


# resources    
api.add_resource(Task, "/task/<int:task_id>")

if __name__ == "__main__":
    app.run(debug = True)