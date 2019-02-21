from key_gen import generate_key
import json

class Config(object):
    SECRET_KEY = generate_key()
    DEBUG = True 
    THREADED = True
    MAIL_SERVER = ""
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_RECIEVE = ''

def get_config():
    json_data = open('config.json').read()
    conf = json.loads(json_data)
    Config.MAIL_USERNAME = conf['email']
    Config.MAIL_PASSWORD = conf['password']
    Config.MAIL_RECIEVE = conf['r_email']
    Config.MAIL_SERVER = conf['serv']