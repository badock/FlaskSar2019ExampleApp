from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/view/a')
def view_a():
    return render_template("template_a.html.jinja2")


@app.route('/view/b')
def view_b():
    return render_template("template_b.html.jinja2")


@app.route('/view/c')
def view_c():
    return render_template("template_c.html.jinja2")


@app.route('/static_resources_view')
def static_resources_view():
    return render_template("static_resources.html.jinja2")


if __name__ == '__main__':
    app.run()
