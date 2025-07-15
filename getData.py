#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import (
    Sepomex, TiposAsentamiento, Municipios, Ciudades, Asentamientos
)

from sqlalchemy import (
    select, cast, Integer, null, case
)

from sqlalchemy.orm import (
    aliased
)

import os

fileSEPOMEX = os.environ.get("FILE_SEPOMEX")

def fileToList(file):
    """
    recibe archivo de texto descargado de SEPOMEX
    y retorna una lista
    """
    with open(file, 'r', encoding='latin-1') as cpFile:
        listCPFile = cpFile.readlines()
        del listCPFile[0:2]
        return listCPFile

estados_clave_alfanumerica = [
    {"id_estado": 1, "nomEstado":  "Aguascalientes", "claveAlfaNumerica": "AS"},
    {"id_estado": 2, "nomEstado":  "Baja California", "claveAlfaNumerica": "BC"},
    {"id_estado": 3, "nomEstado":  "Baja California Sur", "claveAlfaNumerica": "BS"},
    {"id_estado": 4, "nomEstado":  "Campeche", "claveAlfaNumerica": "CC"},
    {"id_estado": 5, "nomEstado":  "Coahuila", "claveAlfaNumerica": "CL"},
    {"id_estado": 6, "nomEstado":  "Colima", "claveAlfaNumerica": "CM"},
    {"id_estado": 7, "nomEstado":  "Chiapas", "claveAlfaNumerica": "CS"},
    {"id_estado": 8, "nomEstado":  "Chihuahua", "claveAlfaNumerica": "CH"},
    {"id_estado": 9, "nomEstado":  "Ciudad de México / CDMX", "claveAlfaNumerica": "DF"},
    {"id_estado": 10, "nomEstado": "Durango", "claveAlfaNumerica": "DG"},
    {"id_estado": 11, "nomEstado": "Guanajuato", "claveAlfaNumerica": "GT"},
    {"id_estado": 12, "nomEstado": "Guerrero", "claveAlfaNumerica": "GR"},
    {"id_estado": 13, "nomEstado": "Hidalgo", "claveAlfaNumerica": "HG"},
    {"id_estado": 14, "nomEstado": "Jalisco", "claveAlfaNumerica": "JC"},
    {"id_estado": 15, "nomEstado": "Estado de México", "claveAlfaNumerica": "MC"},
    {"id_estado": 16, "nomEstado": "Michoacán", "claveAlfaNumerica": "MN"},
    {"id_estado": 17, "nomEstado": "Morelos", "claveAlfaNumerica": "MS"},
    {"id_estado": 18, "nomEstado": "Nayarit", "claveAlfaNumerica": "NT"},
    {"id_estado": 19, "nomEstado": "Nuevo León", "claveAlfaNumerica": "NL"},
    {"id_estado": 20, "nomEstado": "Oaxaca", "claveAlfaNumerica": "OC"},
    {"id_estado": 21, "nomEstado": "Puebla", "claveAlfaNumerica": "PL"},
    {"id_estado": 22, "nomEstado": "Querétaro", "claveAlfaNumerica": "QT"},
    {"id_estado": 23, "nomEstado": "Quintana Roo", "claveAlfaNumerica": "QR"},
    {"id_estado": 24, "nomEstado": "San Luis Potosí", "claveAlfaNumerica": "SP"},
    {"id_estado": 25, "nomEstado": "Sinaloa", "claveAlfaNumerica": "SL"},
    {"id_estado": 26, "nomEstado": "Sonora", "claveAlfaNumerica": "SR"},
    {"id_estado": 27, "nomEstado": "Tabasco", "claveAlfaNumerica": "TC"},
    {"id_estado": 28, "nomEstado": "Tamaulipas", "claveAlfaNumerica": "TS"},
    {"id_estado": 29, "nomEstado": "Tlaxcala", "claveAlfaNumerica": "TL"},
    {"id_estado": 30, "nomEstado": "Veracruz", "claveAlfaNumerica": "VZ"},
    {"id_estado": 31, "nomEstado": "Yucatán", "claveAlfaNumerica": "YN"},
    {"id_estado": 32, "nomEstado": "Zacatecas", "claveAlfaNumerica": "ZS"},
    {"id_estado": 33, "nomEstado": "No especificado", "claveAlfaNumerica": "NE"}
]

# key = "id_estado"
# value = 9
# clave_alfanumerica = next((e for e in estados_clave_alfanumerica if e.get(key) == value), None)
# print(clave_alfanumerica)

# cp = {"d_codigo": l[0], "d_asenta": l[1], "d_tipo_asenta": l[2],
#               "D_mnpio": l[3], "d_estado": l[4], "d_ciudad": l[5],
#               "d_CP": l[6], "c_estado": l[7], "c_oficina": l[8],
#               "c_CP": l[9], "c_tipo_asenta": l[10], "c_mnpio": l[11],
#               "id_asenta_cpcons": l[12], "d_zona": l[13],
#               "c_cve_ciudad": "0" if l[14] == '' else l[14].rstrip('\n')
#               }
def getDatosLIst():
    file = fileToList(fileSEPOMEX)
    lDatos = []
    for linea in file:
        l = linea.split('|')
        key = "id_estado"
        value = int(l[7])
        estado = next((e for e in estados_clave_alfanumerica if e.get(key) == value), None)
        cp = {
            "d_codigo": l[0],
            "d_asenta": l[1],
            "d_tipo_asenta": l[2],
            "D_mnpio": l[3],
            "d_estado": estado["nomEstado"],
            "d_ciudad": l[5],
            "d_CP": l[6],
            "c_estado": estado["id_estado"],
            "c_oficina": l[8],
            "c_CP": l[9],
            "c_tipo_asenta": l[10],
            "c_mnpio": l[11],
            "id_asenta_cpcons": l[12],
            "d_zona": l[13],
            "c_cve_ciudad": "0" if l[14] == '' else l[14].rstrip('\n'),
            "cve_alfa_numerica": estado["claveAlfaNumerica"]
        }
        lDatos.append(cp)
    return lDatos



s = aliased(Sepomex)

def getEstados():
    return select(cast(s.c_estado, Integer()),
                  s.d_estado,
                  s.cve_alfa_numerica).distinct().order_by(cast(s.c_estado,
                                                                Integer()))


def getMunicipios():
    # return select(null().label('id'),
    return select(null().label('id'),
                  s.c_estado,
                  s.D_mnpio,
                  s.c_mnpio
                  ).distinct().order_by(s.c_estado, s.c_mnpio)


def getCiudades():
    return select(null().label('id'),
                  s.c_estado,
                  s.d_ciudad,
                  s.c_cve_ciudad,
                  ).distinct().where(s.d_ciudad!="").order_by(s.c_estado,
                                                              s.c_cve_ciudad)

def getTiposAsentamiento():
    return select(s.c_tipo_asenta,
                  s.d_tipo_asenta).distinct().order_by(s.c_tipo_asenta)


def getAsentamientos():
    return select(null().label('id'),
                  s.c_tipo_asenta.label('id_tipoAsentamiento'),
                  s.c_mnpio.label('id_municipio'),
                  s.c_cve_ciudad.label('id_ciudad'),
                  s.c_estado.label('id_estado'),
                  s.d_asenta.label('nomTipoAsentamiento'),
                  s.d_codigo.label('codigoPostal'),
                  )

