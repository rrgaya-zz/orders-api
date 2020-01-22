from decouple import config
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper
from .models import Orders


SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

metadata = MetaData(engine)
ec_orders = Table("ec_orders", metadata, autoload=True)
mapper(Orders, ec_orders)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
