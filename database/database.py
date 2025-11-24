from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings

settings = Settings()

engine = create_engine(settings.db_url)

Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session


# settings = Settings()
#
# def get_db_connect() -> sqlite3.Connection:
#     return sqlite3.connect(settings.SQLITE_DB_NAME)
