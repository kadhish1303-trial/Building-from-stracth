from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:root1234@localhost:5432/login_info"
engine= create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)