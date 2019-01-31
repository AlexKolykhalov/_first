import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # form 
    # see in launch.json
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail
    MAIL_SERVER     = 'smtp.rambler.ru'     #os.environ.get('MAIL_SERVER')
    MAIL_PORT       = 465                   #int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_SSL    = True                  #os.environ.get('MAIL_USE_SSL') is not None    
    MAIL_USE_TLS    = False                 #os.environ.get('MAIL_USE_TLS') is not None    
    MAIL_USERNAME   = 'ak8647'              #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD   = 'e2_e4_New_Champion'  #os.environ.get('MAIL_PASSWORD')
    
    ADMINS          = ['ak8647@rambler.ru']
    # paginations
    POST_PER_PAGE = 10
    # languages
    LANGUAGES = ['en', 'ru']
    MS_TRANSLATOR_KEY = 'trnsl.1.1.20190115T060601Z.ec80cbb4e9456b34.c02d70d921ada6b08db8131853c37515a40c3923'
    # search
    ELASTICSEARCH_URL = 'http://localhost:9200'    
    # redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'