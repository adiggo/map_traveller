from flask import current_app
class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials =  current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.app_id = credentials['id']
        self.app_secret = credentials['secret']

