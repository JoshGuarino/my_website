from key_gen import generate_key
import yaml

class Config(object):
    SECRET_KEY = generate_key()
    DEBUG = True 
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
        with open('config.yaml') as f:
            data = yaml.safe_load(f)
        Config.MAIL_USERNAME = data['email']
        Config.MAIL_PASSWORD = data['password']
        Config.MAIL_RECIEVE = data['r_email']
        Config.MAIL_SERVER = data['serv']
        Config.RECAPTCHA_PUBLIC_KEY = data['RECAPTCHA_PUBLIC_KEY']
        Config.RECAPTCHA_PRIVATE_KEY = data['RECAPTCHA_PRIVATE_KEY']