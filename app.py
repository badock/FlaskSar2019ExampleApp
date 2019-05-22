from flask import Flask
import flask
from database.database import db, init_database

from database.models import Task, TaskList
from misc.forms import NewTaskForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

db.init_app(app)

with app.test_request_context():
    init_database()


def process_new_task(form, task_list):
    print("Adding task '%s' to '%s'" % (form.label.data, task_list.name))
    new_task = Task(label=form.label.data,
                    isDone=False,
                    task_list_id=task_list.id)
    db.session.add(new_task)
    db.session.commit()


@app.route("/<tasks_list_name>", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def homepage(tasks_list_name="default"):
    form = NewTaskForm()

    tasks_list = TaskList.query.filter_by(name=tasks_list_name).first()

    if tasks_list is None:
        tasks_list = TaskList(name=tasks_list_name)
        db.session.add(tasks_list)
        db.session.commit()

    if form.validate_on_submit():
        process_new_task(form, tasks_list)
        return flask.redirect(flask.url_for("homepage",
                                            tasks_list_name=tasks_list.name))

    return flask.render_template("show_tasks.html.jinja2",
                                 tasks_list=tasks_list,
                                 form=form)


@app.route("/toggle_task/<int:task_id>")
def toggle_task(task_id):
    existing_task = Task.query.filter_by(id=task_id).first()
    tasks_list = existing_task.tasks_list

    existing_task.isDone = not existing_task.isDone

    db.session.add(existing_task)
    db.session.commit()

    return flask.redirect(flask.url_for("homepage",
                                        tasks_list_name=tasks_list.name))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    existing_task = Task.query.filter_by(id=task_id).first()

    tasks_list = existing_task.tasks_list

    db.session.delete(existing_task)
    db.session.commit()

    return flask.redirect(flask.url_for("homepage",
                                        tasks_list_name=tasks_list.name))


if __name__ == '__main__':
    app.run()
