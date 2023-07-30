from flask_restx import Resource, Namespace
from .api_models import user_model, task_model, user_input_model, task_input_model
from .models import Task, User
from .extensions import db

ns = Namespace("api")

@ns.route("/users")
class UserListAPI(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        return User.query.all()
    
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def post(self):
        user = User(name=ns.payload["name"])
        db.session.add(user)
        db.session.commit()
        return user, 201

@ns.route("/users/<int:id>")
class UserAPI(Resource):
    @ns.marshal_with(user_model)
    def get(self, id):
        user = User.query.get(id)
        return user
    
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        user = User.query.get(id)
        user.name = ns.payload["name"]
        db.session.commit()
        return user
    
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {}, 204


@ns.route("/tasks")
class TaskListAPI(Resource):
    @ns.marshal_list_with(task_model)
    def get(self):
        return Task.query.all()
    
    @ns.expect(task_input_model)
    @ns.marshal_with(task_model)
    def post(self):
        task = Task(name=ns.payload["name"], user_id=ns.payload["user_id"],
                    categ=ns.payload["categ"], month=ns.payload["month"],
                    day=ns.payload["day"], year=ns.payload["year"])
        db.session.add(task)
        db.session.commit()
        return task, 201
    
@ns.route("/task/<int:id>")
class TaskAPI(Resource):
    @ns.marshal_with(task_model)
    def get(self, id):
        task = Task.query.get(id)
        return task
    
    @ns.expect(task_input_model)
    @ns.marshal_with(task_model)
    def put(self, id):
        task = Task.query.get(id)
        if ns.payload["name"]:
            task.name = ns.payload["name"]
        if ns.payload["user_id"]:
            task.user_id = ns.payload["user_id"]
        if ns.payload["categ"]:
            task.categ = ns.payload["categ"]
        if ns.payload["month"]:
            task.month = ns.payload["month"]
        if ns.payload["day"]:
            task.day = ns.payload["day"]
        if ns.payload["year"]:
            task.year = ns.payload["year"]
        db.session.commit()
        return task
    
    def delete(self, id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return {}, 204