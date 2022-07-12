from flask import Flask

def register_blueprint(app: Flask):

	from project.api.task import task_blueprint
	app.register_blueprint(task_blueprint, url_prefix="/api")