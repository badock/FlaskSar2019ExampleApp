import flask
from sar2019.config import Config
from sar2019.forms import AdditionForm

app = flask.Flask(__name__)
app.config.from_object(Config)


def traitement_formulaire_addition(form):
    expression = "%s %s %s" % (form.number_a.data,
                               form.operator.data,
                               form.number_b.data)
    resultat = "%s" % eval(expression)
    return resultat


def afficher_formulaire_addition(form):
    return flask.render_template("form_addition.html.jinja2", form=form)


@app.route("/add", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def fonction_formulaire_addition():

    form = AdditionForm()

    if form.validate_on_submit():
        return traitement_formulaire_addition(form)
    else:
        return afficher_formulaire_addition(form)


if __name__ == '__main__':
    app.run()
