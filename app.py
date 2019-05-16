from flask import Flask
import flask
from database.database import db, init_database
import database.models
from sar2019.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.test_request_context():
    init_database()


def get_all_engineers():
    return database.models.Engineer.query.all()


def get_engineer_by_id(engineer_id):
    return database.models.Engineer.query.filter_by(id=engineer_id).first()


def get_engineers_in_site(site_name):
    return database.models.Engineer.query.filter_by(site=site_name).all()


@app.route('/')
def index():
    engineers = get_all_engineers()

    result = "All engineers:\n"

    for engineer in engineers:
        result += " - %s (id:%s)\n" % (engineer.username, engineer.id)

    return flask.Response(result,
                          mimetype="text")


@app.route('/engineer/no_templates/<int:engineer_id>')
def show_engineer_without_templates(engineer_id):
    engineer = get_engineer_by_id(engineer_id)

    result = """<p>Information about \""""
    result += engineer.username
    result += """\"</p>

<dl>
    <dt>id</dt>
    <dd>"""
    result += str(engineer.id)
    result += """</dd>

    <dt>username</dt>
    <dd>"""
    result += engineer.username
    result += """</dd>

    <dt>email</dt>
    <dd>"""
    result += engineer.email
    result += """"</dd>

    <dt>site</dt>
    <dd>"""
    result += engineer.site
    result += """"</dd>
</dl>"""

    return result


@app.route('/engineer/<int:engineer_id>')
def show_engineer(engineer_id):
    engineer = get_engineer_by_id(engineer_id)
    return flask.render_template("show_engineer.html.jinja2",
                                 engineer=engineer)


if __name__ == '__main__':
    app.run()
