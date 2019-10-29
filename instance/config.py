'''set up environment confugurations'''

class Config(object):
    '''parent configuration class'''
    DEBUG = False
    CSRF_ENABLED = True
    

class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
    DEBUG = True


class Production(Config):
    TESTING = False
    DEBUG = False


configuration = {
    'development' : Development,
    'testing' : Testing,
    'production' : Production
}
