from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("name", type=str, help="Name of task is required", required=True)
task_put_args.add_argument("month", type=int, help="Month task is due")
task_put_args.add_argument("day", type=int, help="Day task is due")
task_put_args.add_argument("year", type=int, help="Year task is due")

tasks = {}

# if id is not in tasks dictionary, cannot use get
def abort_if_no_id(task_id):
    if task_id not in tasks:
        abort("Task id is not valid :(")

# request handling
class Task(Resource):
    def get(self, task_id):
        abort_if_no_id(task_id)
        return tasks[task_id]
    def put(self, task_id):
        args = task_put_args.parse_args()
        tasks[task_id] = args
        return tasks[task_id], 201 # 201 means created

# resources    
api.add_resource(Task, "/task/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)