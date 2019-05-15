import flask
from sar2019.config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)


@app.route("/complex_view")
@app.route("/")
def complex_view():
    colors = ["red", "blue", "green", "purple", "dark", "white"]
    boolean_value = False
    msg_if_boolean_value = "[boolean_value is true]"
    msg_if_not_boolean_value = "[boolean_value is false]"

    result = ""

    for color in colors:
        result += "* "
        result += color
        result += "\n"

    if boolean_value:
        result += msg_if_boolean_value
    else:
        result += msg_if_not_boolean_value

    return flask.Response(result,
                          mimetype="text")


@app.route("/complex_view_template")
def complex_view_template():
    colors = ["red", "blue", "green", "purple", "dark", "white"]
    boolean_value = False
    msg_if_boolean_value = "[boolean_value is true]"
    msg_if_not_boolean_value = "[boolean_value is false]"

    return flask.Response(flask.render_template("complex_view.jinja2",
                                 colors=colors,
                                 boolean_value=boolean_value,
                                 msg_if_boolean_value=msg_if_boolean_value,
                                 msg_if_not_boolean_value=msg_if_not_boolean_value),
                          mimetype="text")


if __name__ == '__main__':
    app.run()
