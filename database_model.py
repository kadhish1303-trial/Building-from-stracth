from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger 

Base = declarative_base()

class login_info(Base):

    __tablename__ = "student_credentials"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    phone = Column(BigInteger)
    email_id = Column(String)
    password = Column(String)