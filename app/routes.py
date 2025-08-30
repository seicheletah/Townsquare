from flask import render_template
from app import townsquare
from app.forms import LoginForm

@townsquare.route('/')
@townsquare.route('/index')

def index():
    form = LoginForm()
    return render_template('index.html', title='Townsquare', form=form)
