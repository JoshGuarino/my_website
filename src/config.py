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
        Config.MAIL_USERNAME = os.getenv('EMAIL')
        Config.MAIL_PASSWORD = os.getenv('PASSWORD')
        Config.MAIL_RECIEVE = os.getenv('R_MAIL')
        Config.MAIL_SERVER = os.getenv('SERV')
        Config.RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
        Config.RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
        Config.GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
        Config.GITHUB_URL = os.getenv('GITHUB_URL')
        Config.PA_TOKEN = os.getenv('PA_TOKEN')
        Config.PA_RELOAD = os.getenv('PA_RELOAD')
        Config.WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')