from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/engineers')
def display_engineer():
    engineers = []
    return render_template("show_engineers.html.jinja2",
                           engineers=engineers)


if __name__ == '__main__':
    app.run()
