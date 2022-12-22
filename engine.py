import os
from sqlalchemy import create_engine, MetaData

from sqlalchemy.orm import declarative_base

dEngine = {
    "connector": os.environ.get('DATABASE_CONNECTOR'),
    "user": os.environ.get('DATABASE_USER'),
    "password": os.environ.get('DATABASE_PASSWORD'),
    "host": os.environ.get('DATABASE_HOST'),
    "port": os.environ.get('DATABASE_PORT'),
    "db": os.environ.get('DATABASE_DB')
}

sDialect = f"{dEngine['connector']}://{dEngine['user']}:"\
    f"{dEngine['password']}@{dEngine['host']}:{dEngine['port']}/{dEngine['db']}"

metadata_obj = MetaData()
engine = create_engine(sDialect, echo=True, future=True)
Base = declarative_base()
