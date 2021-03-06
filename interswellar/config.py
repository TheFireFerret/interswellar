''' The different application configs'''
import os

# pylint:disable=too-few-public-methods


class DefaultConfig(object):

    ''' The default configuration '''
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_CLIENT_ID = os.environ.get('GH_CID')
    GITHUB_CLIENT_SECRET = os.environ.get('GH_CSEC')

# pylint:disable=too-few-public-methods


class IntegrationConfig(DefaultConfig):

    ''' Configuration for Travis CI'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/interswellar'

# pylint:disable=too-few-public-methods


class DevelopmentConfig(DefaultConfig):

    ''' Configuration for local development '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        os.environ.get('RDS_USERNAME'),
        os.environ.get('RDS_PASSWORD'),
        os.environ.get('RDS_HOSTNAME'),
        os.environ.get('RDS_PORT'),
        os.environ.get('RDS_DB_NAME')
    )


class TestingConfig(DefaultConfig):

    ''' Configuration for local testing '''
    TESTING = True
    DEBUG = True

# pylint:disable=too-few-public-methods


class ProductionConfig(DefaultConfig):

    ''' Configuration for production '''
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        os.environ.get('RDS_USERNAME'),
        os.environ.get('RDS_PASSWORD'),
        os.environ.get('RDS_HOSTNAME'),
        os.environ.get('RDS_PORT'),
        os.environ.get('RDS_DB_NAME')
    )
