from  flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#needed for RegistrationForm and LoginForm -> protect against modyfing cookies, cross site request forgery attack
app.config['SECRET_KEY'] = '55d102a68a11bdb91578610ca74640a3'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)







