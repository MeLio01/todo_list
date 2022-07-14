from datetime import datetime

from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class Task(ResourceMixin, db.Model):
    __tablename__ = "task"

    id = db.Column(db.String(120), unique=True, primary_key=True, index=True, nullable=False, default=generate_uuid)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)