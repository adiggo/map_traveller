""" database handler """
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../conf')
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../lib')

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base

engine = None

def init_engine(uri, **kwargs):
    """ create the engine when needed """
    global engine
    engine = create_engine(uri, **kwargs)
    return engine
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#TODO: Potentially write this
# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     import yourapplication.models
#     Base.metadata.create_all(bind=engine)