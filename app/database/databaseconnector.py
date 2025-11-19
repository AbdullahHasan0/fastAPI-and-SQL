
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


from app.database.databaseschema import Base

class DatabaseConector:
    def __init__(self, DB_URL: str):
        self.DB_URL = DB_URL
        self.engine = create_engine(self.DB_URL, connect_args= {'check_same_thread': False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base = declarative_base()
        Base.metadata.create_all(bind=self.engine)


    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()



