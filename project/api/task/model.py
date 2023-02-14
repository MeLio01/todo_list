from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

# Define the Task model
class Task(ResourceMixin, db.Model):
    # Define the table name
    __tablename__ = "task"

    # Define the columns
    id = db.Column(db.String(120), unique=True, primary_key=True, index=True, nullable=False, default=generate_uuid)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=0)