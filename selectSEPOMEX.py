from sqlalchemy import select
from models import Estados, Ciudades
from engine import engine
from sqlalchemy.orm import Session, aliased



with Session(engine) as session:
    # estados = session.execute(
        # select(Estados).order_by(Estados.id)
    # )
    # for estado in estados:
        # print(estado)



    e = aliased(Estados)
    c = aliased(Ciudades)

    # listaPacientes = session.execute(
    #     select(e.id,
    #            e.nomEstado,
    #            c.id,
    #            c.nomCiudad,
    #            ).join_from(e, c).where(e.id == 12)
    # )
    #
    # for l in listaPacientes:
    #     print('Codigo: {} Estado: {} Codigo: {} Ciudad: {}'.format(
    #         l[0], l[1], l[2], l[3]
    #     ))
    #

    estados = session.execute(
        select(e).order_by(e.id)
    ).scalars()

    for e in estados:
        print(e)


