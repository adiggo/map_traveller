#default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'map_traveller' #TODO: This needs to be researched and changed
    DB_SCHEMA = 'map_traveller'
    DB_USER = 'map_traveller_rw'
    DB_PASSWD = 'map_traveller'
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (DB_USER, DB_PASSWD, DB_HOST, DB_SCHEMA)
    SQLALCHEMY_MIGRATE_REPO = os.path.dirname(os.path.realpath(__file__)) + \
    '/../db/migrations'
    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '**',
            'secret': '*'
        },
        'twitter': {
            'id': '*',
            'secret': '*'
        }
    }

class DevelopmentConfig(BaseConfig):
    DEBUG = True    