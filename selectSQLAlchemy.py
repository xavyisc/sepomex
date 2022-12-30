from sqlalchemy import (
    select, Table
)

from sqlalchemy.orm import (
    Session
)

from engine import engine, metadata_obj

from models import Sepomex
#
#  sepomex_table = Table("SEPOMEX", metadata_obj, autoload_with=engine)
#  stmt = select(sepomex_table).where(sepomex_table.c.d_codigo=="40270")
#  stmtc = select(sepomex_table.c.d_codigo, sepomex_table.c.d_estado,
#                 sepomex_table.c.c_cve_ciudad,
#                 sepomex_table.c.d_ciudad).where(sepomex_table.c.d_codigo=="40270")
#  print(stmt)
#  print(select(sepomex_table))
#
#  with engine.connect() as conn:
#      for row in conn.execute(stmt):
#          print(row)
#      for row in conn.execute(stmtc):
#          print(row)


#  print(select(Sepomex))
with Session(engine) as session:
    row = session.execute(select(Sepomex)).first()
    print(row)
    sepo = session.scalars(select(Sepomex)).first()
    print(sepo)
    i = session.execute(select(Sepomex.d_codigo,
                               Sepomex.c_cve_ciudad,
                               Sepomex.d_ciudad,
                               Sepomex.c_estado,
                               Sepomex.d_estado)).first()
    print(i)
#  stmt = select(Sepomex).where(Sepomex.d_codigo=="40270")
#  with Session(engine) as session:
#      for row in session.execute(stmt):
#          print(row)
#

