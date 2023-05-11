from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')


engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    published_date = Column(DateTime, nullable=True)
    author = Column(String, nullable=True)
    author_link = Column(String, nullable=True)
    url = Column(String, nullable=True)

# Create all tables if they do not exist
Base.metadata.create_all(engine)

# sessionmaker factory
Session = sessionmaker(bind=engine)

# Pydantic model to use it with FastAPI
class ArticleCreate(BaseModel):
    title: str
    published_date: str = None
    author: str = None
    author_link: str = None
    url: str = None
