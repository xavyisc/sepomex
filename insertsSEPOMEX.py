from cpSEPOMEX import (
    getDatosLIst, getEstados, getCiudades, getMunicipios, getAsentamientosTipo
)

from models import (
    #  Estados, Ciudades, Municipios, AsentamientosTipo,
    Sepomex, Estados, Municipios
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
tiposAsentamientos =getAsentamientosTipo()

with Session(engine) as session:
    """ se insertan estados a partir de insert into select """
    estados = session.execute(
        insert(Estados).from_select(["id","nomEstado"], estados)
    )

    """ se insertan municipios a partir de lista con los valores de municipios """
    municipios = session.execute(
       # insert(Municipios), municipios
        insert(Municipios).from_select(["id", "id_estado", "nomMunicipio",
                                        "id_Sepomex"], municipios)
    )

#      """ se insertan ciudades a partir de lista con os valores de ciudades """
#      ciudades = session.execute(
#          insert(Ciudades), ciudades
#      )
#
#
#      """ inserta tipos de Asentamiento a partir de insert into select """
#      tiposAsentamiento = session.execute(
#          insert(AsentamientosTipo).from_select(["id", "nomTipoAsentamiento"],
#                                           tiposAsentamientos)
#      )
    session.commit()

