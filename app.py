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


def save_object_to_db(db_object):
    db.session.add(db_object)
    db.session.commit()


def remove_object_from_db(db_object):
    db.session.delete(db_object)
    db.session.commit()


def add_task_to_tasks_list(form, tasks_list):
    # TODO: implement me
    return None


def create_tasks_list(tasks_list_name):
    # TODO: implement me
    return None


def find_tasks_list_by_name(tasks_list_name):
    # TODO: implement me
    return None


def find_task_by_id(task_id):
    # TODO: implement me
    return None


@app.route("/<tasks_list_name>", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def homepage(tasks_list_name="default"):
    form = NewTaskForm()

    tasks_list = find_tasks_list_by_name(tasks_list_name)

    if tasks_list is None:
        tasks_list = create_tasks_list(tasks_list_name)

    if form.validate_on_submit():
        add_task_to_tasks_list(form, tasks_list)
        return flask.redirect(flask.url_for("homepage",
                                            tasks_list_name=tasks_list.name))

    return flask.render_template("show_tasks.html.jinja2",
                                 tasks_list=tasks_list,
                                 form=form)


@app.route("/toggle_task/<int:task_id>")
def toggle_task(task_id):
    existing_task = find_task_by_id(task_id)
    tasks_list = existing_task.tasks_list

    existing_task.isDone = not existing_task.isDone

    save_object_to_db(existing_task)

    return flask.redirect(flask.url_for("homepage",
                                        tasks_list_name=tasks_list.name))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    existing_task = find_task_by_id(task_id)

    tasks_list = existing_task.tasks_list

    remove_object_from_db(existing_task)

    return flask.redirect(flask.url_for("homepage",
                                        tasks_list_name=tasks_list.name))


if __name__ == '__main__':
    app.run()
