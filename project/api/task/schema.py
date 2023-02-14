from marshmallow import Schema, fields

class TaskSchema(Schema):
    content = fields.String(required=True)
    completed = fields.Integer(required=True)

class TaskIdSchema(Schema):
    id = fields.String(required=True)
    content = fields.String()

class TaskDateSchema(Schema):
    date_created = fields.String(required=True)

class TaskOutSchema(TaskIdSchema, TaskSchema):
    date_created = fields.String(required=True)

task_schema = TaskSchema()
task_out_schema = TaskOutSchema()
task_id_schema  = TaskIdSchema()
task_date_schema = TaskDateSchema()