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


@app.route('/')
def index():
    posts = database.models.Post.query.all()
    return flask.render_template("homepage.html.jinja2",
                                 posts=posts)


def save_post_and_redirect_to_homepage(post, form):
    # TODO: implement this function
    pass


def display_post_form(post, form):
    # TODO: implement this function
    pass


@app.route("/posts/edit/", methods=["GET", "POST"])
@app.route("/posts/edit/<post_id>", methods=["GET", "POST"])
def create_or_process_post(post_id=None):

    # Fetch the corresponding post from the database. If no ID is provided,
    # then post will be 'None', and the form will consider this value
    # as a sign that a new post should be created
    post = database.models.Post.query.filter_by(id=post_id).first()

    # TODO: Replace the following line!!
    form = None

    if form.validate_on_submit():
        return save_post_and_redirect_to_homepage(post, form)
    else:
        return display_post_form(post, form)


@app.route("/posts/delete/<post_id>")
def delete_post(post_id=None):
    post = database.models.Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return flask.redirect(flask.url_for('index'))


if __name__ == '__main__':
    app.run()
