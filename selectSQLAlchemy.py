from sqlalchemy import (
    select, Table
)

from sqlalchemy.orm import (
    Session
)

from engine import engine, metadata_obj

from models import Sepomex


sepomex_table = Table("SEPOMEX", metadata_obj, autoload_with=engine)

stmt = select(sepomex_table).where(sepomex_table.c.d_codigo=="40270")

print(stmt)

with engine.connect() as conn:
   for row in conn.execute(stmt):
       print(row)


stmt = select(Sepomex).where(Sepomex.d_codigo=="40270")
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)


