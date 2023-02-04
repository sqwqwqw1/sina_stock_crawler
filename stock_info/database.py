from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'mysql://user:password@127.0.0.1:3306/stock'  #连接mysql数据库


engin = create_engine(
        SQLALCHEMY_DATABASE_URL, encoding='utf-8',
    )

SessionLocal = sessionmaker(bind=engin, autoflush=False, autocommit=False, expire_on_commit=True)

Base = declarative_base(bind=engin, name='Base')