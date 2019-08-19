from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    title = Column(String(50), nullable=True, comment='标题')
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    isbn = Column(String(15), nullable=True, unique=True)
    summary = Column(Text)
    image = Column(String(50))
