from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class NewTaskForm(Form):
    label = StringField('Label', validators=[DataRequired()])
