from engine import Base, engineLuaMedic as engine

from sqlalchemy.orm import (
    relationship
)
from sqlalchemy import (
    Column, String, Integer, ForeignKey, text
)

class Estados(Base):
    __tablename__ = "SEPOMEX_estados"

    id = Column(Integer, primary_key=True)
    nomEstado = Column(String(60), nullable=False)
    claveAlfaNumerica = Column(String(5), nullable=False)
    ciudades = relationship("Ciudades", back_populates="estadosCiudades")
    municipios = relationship('Municipios', back_populates='estadosMunicipios')

    def __repr__(self):
        return f"[id={self.id!r}, nomEstado={self.nomEstado!r}, claveAlfaNumerica={self.claveAlfaNumerica!r}"


class Municipios(Base):
    __tablename__ = 'SEPOMEX_municipios'

    id = Column(Integer, primary_key=True)
    id_estado = Column(Integer, ForeignKey('SEPOMEX_estados.id'))
    nomMunicipio = Column(String(100), nullable=True)
    id_Sepomex = Column(String(100), nullable=True)

    estadosMunicipios = relationship('Estados', back_populates='municipios')
    # asentamientosMunicipios = relationship("Asentamientos",
    #                                        back_populates="municipiosa")

    def __repr__(self):
        return f"Municipios(id={self.id!r}, id_estado={self.id_estado!r},"\
            f"nomMunicipio={self.nomMunicipio!r}, id_Sepomex={self.id_Sepomex!r})"


class Ciudades(Base):
    __tablename__ = "SEPOMEX_ciudades"

    id = Column(Integer, primary_key=True)
    id_estado = Column(Integer, ForeignKey("SEPOMEX_estados.id"))
    nomCiudad = Column(String(100), nullable=True)
    id_sepomex = Column (String(100), nullable=True)

    estadosCiudades = relationship("Estados", back_populates="ciudades")
    # asentamientosCiudades = relationship("Asentamientos",
    #                              back_populates="ciudadesa")

    def __repr__(self):
        return f"Ciudades(id={self.id!r}, id_estado={self.id_estado!r}),"\
            f"nomCiudad={self.nomCiudad!r}, id_sepomex={self.id_sepomex!r})"

class TiposAsentamiento(Base):
    __tablename__ = "SEPOMEX_tiposAsentamiento"

    id = Column(Integer, primary_key=True) 
    nomTipoAsentamiento = Column(String(100), nullable=False)

    asentamientos = relationship("Asentamientos",
                                 back_populates="asentamientosTipo")

    def __repr__(self):
        return f"tiposAsentamiento(id={self.id!r},"\
            f"nomTipoAsentamiento={self.nomTipoAsentamiento!r})"


class Asentamientos(Base):
    __tablename__ = "SEPOMEX_asentamientos"

    id = Column(Integer, primary_key=True)

    id_tipoAsentamiento = Column(Integer,
                                 ForeignKey("SEPOMEX_tiposAsentamiento.id"))
    id_municipio = Column(Integer, nullable=True)
    id_ciudad = Column(String(20), nullable=True)
    id_estado = Column(Integer, nullable=True)
    nomAsentamiento = Column(String(140), nullable=False)
    codigoPostal = Column(Integer, nullable=False)

    asentamientosTipo = relationship("TiposAsentamiento",
                                    back_populates="asentamientos")
    # ciudadesa = relationship("Ciudades",
                           # back_populates="asentamientosCiudades")
    # municipiosa = relationship("Municipios",
                              # back_populates="asentamientosMunicipios")

    def __repr__(self):
        return f"Aentamientos(id={self.id!r},"\
            f"id_tipoAsentamiento={self.id_tipoAsentamiento},"\
            f"id_municipio={self.id_municipio!r},"\
            f"id_ciudad={self.id_ciudadi!r},"\
            f"nomAsentamiento={self.nomAsentamiento!r})"

class Sepomex(Base):
    __tablename__ = "SEPOMEX"

    # se agrega un id primary key sin funcion ya que abliga sqlalchemy
    id = Column(Integer, primary_key=True)

    d_codigo = Column(Integer, nullable=False, server_default=text('00000'))
    d_asenta = Column(String(100), nullable=False)
    d_tipo_asenta = Column(String(100), nullable=False)
    D_mnpio = Column(String(100), nullable=False)
    d_estado = Column(String(100), nullable=False)
    d_ciudad = Column(String(100), nullable=False)
    d_CP = Column(String(20), nullable=True)
    c_estado = Column(Integer, nullable=False)
    c_oficina = Column(String(100), nullable=False)
    c_CP = Column(String(20), nullable=False)
    c_tipo_asenta = Column(Integer, nullable=False)
    c_mnpio = Column(String(20), nullable=True)
    id_asenta_cpcons = Column(Integer, nullable=False)
    d_zona = Column(String(100), nullable=True)
    c_cve_ciudad = Column(String(10), nullable=True)
    cve_alfa_numerica = Column(String(5), nullable=False)

    def __repr__(self):
        return f"Sepomex(id={self.id!r}, d_codigo={self.d_codigo!r},"\
            f"d_aseta={self.d_asenta!r},"\
            f"d_tipo_asenta={self.d_tipo_asenta!r},"\
            f"D_mnpio={self.D_mnpio!r},"\
            f"d_estado={self.d_estado!r},"\
            f"d_ciudad={self.d_ciudad!r},"\
            f"d_CP={self.d_CP!r},"\
            f"c_estado={self.c_estado!r},"\
            f"c_oficina={self.c_oficina!r},"\
            f"c_CP={self.c_CP!r},"\
            f"c_tipo_asenta={self.c_tipo_asenta!r},"\
            f"c_mnpio={self.c_mnpio!r},"\
            f"id_asenta_cpcons={self.id_asenta_cpcons!r},"\
            f"d_zona={self.d_zona!r}"\
            f"c_cve_ciudad={self.c_cve_ciudad!r})"


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
def createData():
    print("="*100)
    print("Iniciando...")
    print("="*100)

    print("="*100)
    print("Eliminando Base de datos si existe...")
    print("="*100)
    Base.metadata.drop_all(engine)

    print("="*100)
    print("Creando estructura de Base de datos...")
    print("="*100)
    Base.metadata.create_all(engine)


