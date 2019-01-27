from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2018, 1, 19, 12, 00, 00)
    endtime = datetime(3018, 2, 2, 23, 59, 00)
    nowtime = datetime.now()

    otitlimit = 38
    communicalimit = 38

    entrys = Model.query.all()
    count = Model.query.count()


    otits = []
    communicas = []

    maxlimit = 500


    for entry in entrys:
        if entry.guild == "otit":
            otits.append({"name": entry.name, "avec": False})
            if entry.avec:
                otits.append({"name": entry.avec_name, "avec": True})
        elif entry.guild == "communica":
            communicas.append({"name": entry.name, "avec": False})
            if entry.avec:
                communicas.append({"name": entry.avec_name, "avec": True})


    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(
            name=form.name.data,
            mail = form.mail.data,
            guild = form.guild.data,
            alcohol = form.alcohol.data,
            wine = form.wine.data,
            beer = form.beer.data,
            specialneeds = form.specialneeds.data,
            avec = form.avec.data,
            avec_name = form.avec_name.data,
            avec_alcohol = form.avec_alcohol.data,
            avec_wine = form.avec_wine.data,
            avec_beer = form.avec_beer.data,
            avec_specialneeds = form.avec_specialneeds.data,
            datetime = nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('index'))

    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen täynnä!')

    return render_template('index.html',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           otitlimit=otitlimit,
                           otits=otits,
                           otitcount=len(otits),
                           communicalimit=communicalimit,
                           communicas=communicas,
                           communicacount=len(communicas),
                           form=form)
