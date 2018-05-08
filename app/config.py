

class Config:
    # needed for RegistrationForm and LoginForm -> protect against modyfing cookies, cross site request forgery attack
    SECRET_KEY = '55d102a68a11bdb91578610ca74640a3'
    SQLALCHEMY_DATABASE_URI = ''
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # REMEMBER TO CHANGE
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
