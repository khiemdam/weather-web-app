from flask_restx import fields

from .extensions import api

task_model = api.model("Task", {
    "id": fields.Integer,
    "name": fields.String,
    "categ": fields.String,
    "month": fields.Integer,
    "day": fields.Integer,
    "year": fields.Integer,
    # "user": fields.Nested(user_model)
})

task_input_model = api.model("TaskInput", {
    "name": fields.String,
    "user_id": fields.Integer,
    "categ": fields.String,
    "month": fields.Integer,
    "day": fields.Integer,
    "year": fields.Integer,
})

user_model = api.model("User", {
    "id": fields.Integer,
    "name": fields.String,
    "tasks": fields.List(fields.Nested(task_model))
})

user_input_model = api.model("UserInput", {
    "name": fields.String
})