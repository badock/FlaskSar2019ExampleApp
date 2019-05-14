import flask
from sar2019.config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)


def traitement_formulaire_addition(form):
    pass


def afficher_formulaire_addition(form):
    pass


@app.route("/add", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def fonction_formulaire_addition():
    return "TODO: implement me!"


if __name__ == '__main__':
    app.run()
