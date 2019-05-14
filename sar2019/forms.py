from flask_wtf import Form

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def operator_check(form, field):
    authorized_operator = ["+", "-", "*", "/", "%"]
    if field.data not in authorized_operator:
        raise ValidationError('Field must be in %s' % authorized_operator)


class AdditionForm(Form):
    number_a = IntegerField('Number A', validators=[DataRequired()])
    number_b = IntegerField('Number B', validators=[DataRequired()])
    operator = StringField('Operator', validators=[DataRequired(), operator_check])
