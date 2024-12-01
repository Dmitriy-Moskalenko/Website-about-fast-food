from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение URL СУБД
SQL_DB_URL = 'sqlite:///./database.db'

# Создаём движок SqlAlcheme
engine = create_engine(SQL_DB_URL, connect_args={'check_same_thread': False})

# Создаём сессию, убираем автомат. синхронизиацю с БД и подкл. движок
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Создаём базовый класс для моделй
base = declarative_base()

# Создаём таблицы
base.metadata.create_all(bind=engine)

