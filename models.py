from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import base


# Таблица с пользователями
class User(base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    password = Column(String)


# Таблица с категориями
class Category(base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)


# Таблица с продуктами
class Product(base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')


