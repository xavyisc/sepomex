

from models import (
    Sepomex, Estados, Municipios, Ciudades, TiposAsentamiento, Asentamientos,
    createData
)

from getData import (
    getDatosLIst, getEstados, getCiudades, getMunicipios, getTiposAsentamiento,
    getAsentamientos
)

from engine import engineLuaMedicDeploy as engine

from sqlalchemy import (
    insert, select, null
)

from sqlalchemy.orm import (
    Session, aliased
)

def procesaSEPOMEX():
    datos = getDatosLIst()

    with engine.connect() as conn:
        allDatos = conn.execute(
            insert(Sepomex), datos
        )
        conn.commit()

# se obtienes los datos que se almacenaran en la base de datos y anormalizada
def begin():
    createData()

    print("="*100)
    print("Copiando información a las tablas normalizadas")
    print("="*100)

    procesaSEPOMEX()

    estados = getEstados()
    municipios = getMunicipios()
    ciudades = getCiudades()
    tiposAsentamientos = getTiposAsentamiento()
    asentamientos = getAsentamientos()


    with Session(engine) as session:
       """ se insertan estados a partir de insert into select """
       estados = session.execute(
           insert(Estados).from_select(["id","nomEstado", "claveAlfaNumerica"], estados)
       )

       """ se insertan municipios a partir del insert into  con los valores  de
       municipios """
       municipios = session.execute(
           insert(Municipios).from_select(["id",
                                           "id_estado",
                                           "nomMunicipio",
                                           "id_Sepomex"],
                                          municipios)
       )

       """ se insertan ciudades a partir del insert into con los valores  de
       ciudades"""
       ciudades = session.execute(
           insert(Ciudades).from_select(["id", "id_estado", "nomCiudad",
                                         "id_sepomex"], ciudades)
       )

       """Inserta tipos de asentamiento a partir de insert into con los valores de
       los tipos de asentamiento"""
       tiposAsentamiento = session.execute(
           insert(TiposAsentamiento).from_select(["id", "nomTipoAsentamiento"],
                                                  tiposAsentamientos)
       )

       """ serta tipos de Asentamiento a partir de insert into select con los
       valoresores de asentamientos """
       Asentamiento = session.execute(
           insert(Asentamientos).from_select(["id",
                                              "id_tipoAsentamiento",
                                              "id_municipio",
                                              "id_ciudad",
                                              "id_estado",
                                              "nomAsentamiento",
                                              "codigoPostal"],
                                              asentamientos)
       )
       session.commit()

       print("="*100)
       print("la informacion del archivo SEPOMEX se ha procesado con exito")
       print("="*100)

