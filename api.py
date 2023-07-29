from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
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

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("name", type = str, help = "Name of task is required", required = True)
task_put_args.add_argument("categ", type = str, help = "Category of task (assignment, event, etc.)")
task_put_args.add_argument("month", type = int, help = "Month task is due")
task_put_args.add_argument("day", type = int, help = "Day task is due")
task_put_args.add_argument("year", type = int, help = "Year task is due")

task_update_args = reqparse.RequestParser()
task_update_args.add_argument("name", type = str, help = "Name of task is required")
task_update_args.add_argument("categ", type = str, help = "Category of task (assignment, event, etc.)")
task_update_args.add_argument("month", type = int, help = "Month task is due")
task_update_args.add_argument("day", type = int, help = "Day task is due")
task_update_args.add_argument("year", type = int, help = "Year task is due")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'categ': fields.String,
    'month': fields.Integer,
    'day': fields.Integer,
    'year': fields.Integer
}

# request handling: endpoints
class Task(Resource):
    @marshal_with(resource_fields)
    def get(self, task_id):
        result = TaskModel.query.filter_by(id=task_id).first()
        if not result:
            abort(404, message="Could not find task with that id...")
        return result
    
    @marshal_with(resource_fields)
    def put(self, task_id):
        args = task_put_args.parse_args()
        result = TaskModel.query.filter_by(id=task_id).first()
        if result:
            abort(409, message="Task id taken...")
        task = TaskModel(id=task_id, name=args['name'], categ=args['categ'], 
                         month=args['month'], day=args['day'], year=args['year'])
        db.session.add(task)
        db.session.commit()
        return task, 201 # 201 means created successfully
    
    @marshal_with(resource_fields)
    def patch(self, task_id):
        args = task_update_args.parse_args()
        result = TaskModel.query.filter_by(id=task_id).first()
        if not result:
            abort(404, message="Cannot update task that doesn't exist...")
        
        if args['name']:
            result.name = args['name']
        if args['categ']:
            result.categ = args['categ']
        if args['month']:
            result.month = args['month']
        if args['day']:
            result.day = args['day']
        if args['year']:
            result.year = args['year']
        
        db.session.commit()

        return result

    def delete(self, task_id):
        result = TaskModel.query.filter_by(id=task_id).first()
        if not result:
            abort(404, message="Cannot delete task that doesn't exist...")
        db.session.delete(result)
        db.session.commit()

# resources    
api.add_resource(Task, "/task/<int:task_id>")

if __name__ == "__main__":
    app.run(debug = True)