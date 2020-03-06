from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Optional

class Team_form(FlaskForm):
    team = StringField('Tiimin nimi', validators=[DataRequired()])
    captain = StringField('Kapteeni', validators=[DataRequired()])
    player1 = StringField('Pelaaja', validators=[DataRequired()])
    player2 = StringField('Pelaaja', validators=[DataRequired()])

    medic = StringField('Avustaja (Medic)', validators=[DataRequired()])
    mail = StringField('Kapteenin sähköpostiosoite', validators=[DataRequired()])
    guild = StringField('Edustettu taho', validators=[DataRequired()])

    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])

    submit_team = SubmitField('Lähetä')


class Settings_form(FlaskForm):

    text = TextAreaField('Leipäteksti')

    place = StringField('Paikka')
    time = StringField('Aika')

    ask_medic = BooleanField('Kysy medic')
    ask_guild = BooleanField('Kysy edustettu taho')
    ask_mail = BooleanField('Kysy sähköpostiosoite')

    alcoholdisclaimer = BooleanField('Näytä alkoholi disclaimeri')

    form_open = DateTimeField('Lomake aukeaa (%Y-%m-%d %H:%M:%S)', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])
    form_close = DateTimeField('Lomake sulkeutuu (%Y-%m-%d %H:%M:%S)', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])

    teams_needed = IntegerField('Tarvittavien tiimien määrä', validators=[Optional()])

    submit_settings = SubmitField('Tallenna')

class Reset_form(FlaskForm):

    submit_reset = SubmitField('TYHJENNÄ TIIMIT JA ASETUKSET')


