from flask import Flask
import flask
from database.database import db, init_database
from database.functions import get_all_engineers, get_engineer_by_id
from sar2019.config import Config
from database.models import Mission

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.test_request_context():
    init_database()


@app.route('/')
@app.route('/engineers')
def index():
    engineers = get_all_engineers()
    return flask.render_template("list_engineers.html.jinja2",
                                 engineers=engineers)


@app.route('/missions')
def missions():
    missions = Mission.query.all()
    return flask.render_template("list_missions.html.jinja2",
                                 missions=missions)


@app.route('/engineer/id/<int:engineer_id>')
def show_engineer_by_id(engineer_id):
    engineer = get_engineer_by_id(engineer_id)
    return flask.render_template("show_engineer.html.jinja2",
                                 engineer=engineer)


if __name__ == '__main__':
    app.run()
