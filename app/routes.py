from flask import render_template, flash, redirect
from app import townsquare
from app.forms import LoginForm

@townsquare.route('/', methods=['GET', 'POST'])
@townsquare.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('index.html', title='Townsquare', form=form)
