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


@app.route("/sum/<label>/<int:a>/<int:b>")
def compute_sum(label, a, b):
    c = a + b
    return label+" "+str(a)+" et "+str(b)+" est "+str(c)


if __name__ == '__main__':
    app.run()
