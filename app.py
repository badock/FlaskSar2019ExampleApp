from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/greetings')
def some_function():
    return "Helloworld!"


@app.route('/greetings_with_html')
def some_function_html():
    return """
<html>
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <b>Hello world!</b>
    </body>
</html>
    """


@app.route('/greetings_with_html_and_template')
def some_function_html_with_template():

    colors = ["red", "blue", "green", "purple", "dark", "white"]
    boolean_value = False
    msg_if_boolean_value = "[boolean_value is true]"
    msg_if_not_boolean_value = "[boolean_value is false]"

    return render_template("first_template.html",
                           colors_arg=colors,
                           boolean_value_arg=boolean_value,
                           msg_if_boolean_value_arg=msg_if_boolean_value,
                           msg_if_not_boolean_value_arg=msg_if_not_boolean_value)


@app.route("/sum/<lang>/<int:a>/<int:b>")
def compute_sum(lang, a, b):
    c = a + b
    if lang == "fr":
        return "La somme de %d et %d est %d" % (a, b, c)
    else:
        return "The sum of %d and %d is %d" % (a, b, c)


if __name__ == '__main__':
    app.run()
