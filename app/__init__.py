from  flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#needed for RegistrationForm and LoginForm -> protect against modyfing cookies, cross site request forgery attack
app.config['SECRET_KEY'] = '55d102a68a11bdb91578610ca74640a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ddlotpgl:w4Pt-4b-ghnT3B77ln3czUoFcBwJyNfm@horton.elephantsql.com:5432/ddlotpgl'

db = SQLAlchemy(app)

from app import routes