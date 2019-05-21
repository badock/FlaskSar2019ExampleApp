from flask import Flask
import flask
from database.database import db, init_database

from database.models import Task
from misc.forms import NewTaskForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

db.init_app(app)

with app.test_request_context():
    init_database()


def process_new_task(form):
    print("Adding task '%s'" % form.label.data)
    new_task = Task(label=form.label.data,
                    isDone=False)
    db.session.add(new_task)
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def homepage():
    form = NewTaskForm()

    if form.validate_on_submit():
        process_new_task(form)
        return flask.redirect(flask.url_for("homepage"))

    tasks = Task.query.all()
    return flask.render_template("show_tasks.html.jinja2",
                                 tasks=tasks,
                                 form=form)


@app.route("/toggle_task/<int:task_id>")
def toggle_task(task_id):
    existing_task = Task.query.filter_by(id=task_id).first()
    existing_task.isDone = not existing_task.isDone

    db.session.add(existing_task)
    db.session.commit()

    return flask.redirect(flask.url_for("homepage"))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    existing_task = Task.query.filter_by(id=task_id).first()
    existing_task.isDone = not existing_task.isDone

    db.session.delete(existing_task)
    db.session.commit()

    return flask.redirect(flask.url_for("homepage"))


if __name__ == '__main__':
    app.run()
