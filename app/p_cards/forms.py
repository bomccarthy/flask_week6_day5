from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChoosePokemonForm(FlaskForm):
    # name = StringField('Name', validators=[DataRequired()])
    chosen_pokemon = StringField('Pokemon', validators=[DataRequired()])
    submit = SubmitField()

class KeepPokemonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField()