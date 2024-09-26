from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)

DATABASE_URL = 'sqlite:///./company.db'

def get_engine():
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_database():
    engine = get_engine()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_database()
