from app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(64))
    captain = db.Column(db.String(64))
    player1 = db.Column(db.String(64))
    player2 = db.Column(db.String(64))
    medic = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    guild = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024))

    place = db.Column(db.String(64))
    time = db.Column(db.String(64))

    ask_medic = db.Column(db.Boolean())
    ask_guild = db.Column(db.Boolean())
    ask_mail = db.Column(db.Boolean())


    alcoholdisclaimer = db.Column(db.Boolean())

    form_open = db.Column(db.DateTime())
    form_close = db.Column(db.DateTime())

    teams_needed = db.Column(db.Integer)

