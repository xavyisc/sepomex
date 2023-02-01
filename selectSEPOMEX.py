from sqlalchemy import select
from models import Estados
from engine import engine
from sqlalchemy.orm import Session



with Session(engine) as session:
    estados = session.execute(
        select(Estados).order_by(Estados.id)
    )
    print(estados)
    for e in estados:
        print(e)
