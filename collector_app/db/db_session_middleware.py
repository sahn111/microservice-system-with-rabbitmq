from sqlalchemy.orm.session import sessionmaker

from .db_config import sqlalchemy_engine

def db_session_middleware():
    Session = sessionmaker(bind=sqlalchemy_engine)
    session = Session()
    yield session
    session.close()