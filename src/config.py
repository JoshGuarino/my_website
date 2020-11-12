import random
import string
import yaml
import os

class Config(object):
    SECRET_KEY = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(22))
    DEBUG = False 
    THREADED = True
    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_RECIEVE = ''
    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY = ''
    RECAPTCHA_OPTIONS = {'theme':'black'}
    def get_config():
        Config.MAIL_USERNAME = os.environ['EMAIL']
        Config.MAIL_PASSWORD = os.environ['PASSWORD']
        Config.MAIL_RECIEVE = os.environ['R_MAIL']
        Config.MAIL_SERVER = os.environ['SERV']
        Config.RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
        Config.RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
        Config.GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
        Config.GITHUB_URL = os.environ['GITHUB_URL']
        Config.PA_TOKEN = os.environ['PA_TOKEN']
        Config.PA_RELOAD = os.environ['PA_RELOAD']