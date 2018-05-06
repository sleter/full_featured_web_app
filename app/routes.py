from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #warning it works only with python 3.6.5 (use .format for older versions)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if(form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user, remember=form.remember.data)
            #if we want to access page only for logged in users it will redirect after loggin
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('You fucked up logging in x-D', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)
