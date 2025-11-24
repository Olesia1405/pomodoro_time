from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/pomodoro')

Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session


# settings = Settings()
#
# def get_db_connect() -> sqlite3.Connection:
#     return sqlite3.connect(settings.SQLITE_DB_NAME)
