
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mysql+pymysql://root:123456@127.0.0.1:3306/sztornado'
engine = create_engine(url)

Base = declarative_base(bind=engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
