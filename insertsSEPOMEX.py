from cpSEPOMEX import (
    getDatosLIst, getEstados, getCiudades, getMunicipios, getTiposAsentamiento
)

from models import (
    Sepomex, Estados, Municipios, Ciudades, tiposAsentamiento
)

from engine import engine
from fileToList import listCPFile

from sqlalchemy import (
    insert
)

from sqlalchemy.orm import (
    Session
)

datos = getDatosLIst(listCPFile)

with engine.connect() as conn:
    allDatos = conn.execute(
        insert(Sepomex), datos
    )
    conn.commit()

# se obtienes los datos que se almacenaran en la base de datos y anormalizada
estados = getEstados()
municipios = getMunicipios()
ciudades = getCiudades()
tiposAsentamientos = getTiposAsentamiento()

with Session(engine) as session:
    """ se insertan estados a partir de insert into select """
    estados = session.execute(
        insert(Estados).from_select(["id","nomEstado"], estados)
    )

    """ se insertan municipios a partir del insert into  con los valores  de
    municipios """
    municipios = session.execute(
        insert(Municipios).from_select(["id", "id_estado", "nomMunicipio",
                                        "id_Sepomex"], municipios)
    )

    """ se insertan ciudades a partir del insert into con los valores  de
    ciudades"""
    ciudades = session.execute(
        insert(Ciudades).from_select(["id", "id_estado", "nomCiudad",
                                      "id_Sepomex"], ciudades)
    )

    """Inserta tipos de asentamiento a partir de insert into con los valores de
    los tipos de asentamiento"""
    tiposAsentamiento = session.execute(
        insert(tiposAsentamiento).from_select(["id", "nomTipoAsentamiento"],
                                              tiposAsentamientos)
    )

#      """ inserta tipos de Asentamiento a partir de insert into select """
#      tiposAsentamiento = session.execute(
#          insert(AsentamientosTipo).from_select(["id", "nomTipoAsentamiento"],
#                                           tiposAsentamientos)
#      )
    session.commit()

