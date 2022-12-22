from models import Sepomex as s
from engine import engine
from sqlalchemy import (
    insert, select, cast, Integer, null
)
from sqlalchemy.orm import (
    Session
)

def getDatosLIst(file):
    lDatos = []
    for linea in file:
        l = linea.split('|')
        cp = {"d_codigo": l[0], "d_asenta": l[1], "d_tipo_asenta": l[2],
              "D_mnpio": l[3], "d_estado": l[4], "d_ciudad": l[5],
              "d_CP": l[6], "c_estado": l[7], "c_oficina": l[8],
              "c_CP": l[9], "c_tipo_asenta": l[10], "c_mnpio": l[11],
              "id_asenta_cpcons": l[12], "d_zona": l[13],
              "c_cve_ciudad": l[14].rstrip('\n')
              }
        lDatos.append(cp)

    return lDatos


def getEstados():
    return select(cast(s.c_estado, Integer()),
                  s.d_estado).distinct().order_by(cast(s.c_estado, Integer))


def getMunicipios():
    # municipios = []
    # sMunicipios = select(s.c_mnpio,
    #                      s.c_estado,
    #                      s.D_mnpio).distinct().order_by(s.c_estado)

    return select(null().label('id'),
                  s.c_estado,
                  s.D_mnpio,
                  s.c_mnpio,
                  ).distinct().order_by(s.c_estado, s.c_mnpio)

    # with engine.connect() as conn:
    #     rMunicipios = conn.execute(
    #         sMunicipios
    #     )
    #     for i, m in enumerate(rMunicipios, 1):
    #         municipios.append({"id": i, "id_estado": m[1],
    #                            "nomMunicipio": m[2]})
    #
    # return municipios

def getCiudades():
    ciudades = []
    sCiudades = select(s.c_cve_ciudad,
                       s.c_estado,
                       s.d_ciudad).distinct().where(s.c_cve_ciudad!='',
                                                    s.d_ciudad!='').order_by(
                                                        s.c_estado
                                                    )
    with engine.connect() as conn:
        rCiudades = conn.execute(
            sCiudades
        )
        for i, c in enumerate(rCiudades, 1):
            ciudades.append({"id": i, "id_estado": c[1], "nomCiudad": c[2]})

    return ciudades


def getAsentamientosTipo():
    return select(s.c_tipo_asenta,
                  s.d_tipo_asenta).distinct().order_by(s.c_tipo_asenta)
