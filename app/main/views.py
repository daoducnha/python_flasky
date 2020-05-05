from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from flask_login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

@main.route('/secret')
@login_required
def secret():
    return "Only authenticated users are allowed!"
