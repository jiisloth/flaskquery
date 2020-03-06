from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Team_form, Settings_form, Reset_form
from app.models import Settings, Team
from datetime import datetime
from flask_basicauth import BasicAuth
import os

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else
appurl = os.environ.get("URL")
basic_auth = BasicAuth(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    team_form = Team_form()

    teams = Team.query.all()
    settings = Settings.query.first()

    nowtime = datetime.now()

    open = True
    if settings:
        if settings.form_open:
            if settings.form_open > nowtime:
                open = False
        if settings.form_close:
            if settings.form_close < nowtime:
                open = False
    else:
        return render_template('empty.html',
                           appurl=appurl)


    if team_form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Team(
            team=team_form.team.data,
            captain=team_form.captain.data,
            player1=team_form.player1.data,
            player2=team_form.player2.data,
            medic=team_form.medic.data,
            mail=team_form.mail.data,
            guild=team_form.guild.data,
            timestamp=nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)



    return render_template('index.html',
                           appurl=appurl,
                           teams=teams,
                           open=open,
                           settings=settings,
                           team_form=team_form)


@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    team_form = Team_form()
    settings_form = Settings_form()
    reset = Reset_form()

    teams = Team.query.all()
    settings = Settings.query.first()


    nowtime = datetime.now()

    if reset.submit_reset.data and reset.validate_on_submit():
        flash('ILMO NOLLATTU')
        db.session.query(Settings).delete()
        db.session.query(Team).delete()
        db.session.commit()
        return redirect(appurl + "/admin")


    if settings_form.submit_settings.data and settings_form.validate_on_submit():
        flash('ASETUKSET MUOKATTU!')
        db.session.query(Settings).delete()
        sub = Settings(
            text=settings_form.text.data,
            place=settings_form.place.data,
            time=settings_form.time.data,
            ask_medic=settings_form.ask_medic.data,
            ask_guild=settings_form.ask_guild.data,
            ask_mail=settings_form.ask_mail.data,
            form_open=settings_form.form_open.data,
            form_close=settings_form.form_close.data,
            alcoholdisclaimer=settings_form.alcoholdisclaimer.data,
            teams_needed=settings_form.teams_needed.data
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl + "/admin")

    if team_form.submit_team.data and team_form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Team(
            team=team_form.team.data,
            captain=team_form.captain.data,
            player1=team_form.player1.data,
            player2=team_form.player2.data,
            medic=team_form.medic.data,
            mail=team_form.mail.data,
            guild=team_form.guild.data,
            timestamp=nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)

    return render_template('admin.html',
                           appurl=appurl,
                           teams=teams,
                           settings=settings,
                           reset=reset,
                           settings_form=settings_form,
                           team_form=team_form,
                           nowtime=nowtime)