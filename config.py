from key_gen import generate_key

class Config(object):
    SECRET_KEY = generate_key()
    DEBUG = True 
    THREADED = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
