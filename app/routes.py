from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from app import app

#test_data
posts = [
    {
        'author': 'me',
        'title': 'blog post 1',
        'content': 'first post',
        'date_posted': 'date1'

    },
    {
        'author': 'me2',
        'title': 'blog post 2',
        'content': 'second post',
        'date_posted': 'date2'

    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        #warning it works only with python 3.6.5 (use .format for older versions)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == 'admin@wp.pl' and form.password.data == '12345'):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('You fucked up logging in x-D', 'danger')
    return render_template('login.html', title='Login', form=form)
