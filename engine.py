import os
from sqlalchemy import create_engine, MetaData

from sqlalchemy.orm import declarative_base

os.environ['FLASK_DATABASE_CONNECTOR'] = 'mysql+pymysql'
os.environ['FLASK_DATABASE_USER'] = 'xvy'
os.environ['FLASK_DATABASE_PASSWORD'] = '}Jj312816{}Jsma{'
os.environ['FLASK_DATABASE_HOST'] = 'localhost'
os.environ['FLASK_DATABASE_PORT'] = '3306'
os.environ['FLASK_DATABASE'] = 'SEPOMEX'
os.environ['FILE_SEPOMEX']= '/home/xvy/Documentos/workspace/python/sepomex/CPdescarga.txt'
# export FILE_SEPOMEX='/home/xvy/Documentos/workspace/python/sepomex/CPdescarga.txt'
os.environ['DATABASE_CONNECTOR'] = 'mysql+pymysql'
os.environ['DATABASE_USER'] = 'xvy'
os.environ['DATABASE_PASSWORD'] = '}Jj312816{}Jsma{'
os.environ['DATABASE_HOST'] = 'localhost'
os.environ['DATABASE_PORT'] = '3306'
os.environ['DATABASE_DB'] = 'hgap'


# servidor
# os.environ['FLASK_APP']='appLuaMedic'
# os.environ['FLASK_DEBUG'] = 'True'
os.environ['FLASK_DATABASE_HOST_D'] = 'xavyisc.mysql.pythonanywhere-services.com'
os.environ['FLASK_DATABASE_USER_D'] = 'xavyisc'
os.environ['FLASK_DATABASE_PASSWORD_D'] = '[{JazJavJah31281607}]'
os.environ['FLASK_DATABASE_D'] = 'xavyisc$LuaMedicPrueba'
os.environ['FLASK_DATABASE_CONNECTOR_D'] = 'mysql+pymysql'
os.environ['FLASK_DATABASE_PORT_D'] = '3306'

dEngine = {
    "connector": os.environ.get('DATABASE_CONNECTOR'),
    "user": os.environ.get('DATABASE_USER'),
    "password": os.environ.get('DATABASE_PASSWORD'),
    "host": os.environ.get('DATABASE_HOST'),
    "port": os.environ.get('DATABASE_PORT'),
    "db": os.environ.get('DATABASE_DB')
}

sDialect = f"{dEngine['connector']}://{dEngine['user']}:"\
    f"{dEngine['password']}@{dEngine['host']}:{dEngine['port']}/{dEngine['db']}"

dEngineLuaMedic = {
    "connector": os.environ.get('FLASK_DATABASE_CONNECTOR'),
    "user": os.environ.get('FLASK_DATABASE_USER'),
    "password": os.environ.get('FLASK_DATABASE_PASSWORD'),
    "host": os.environ.get('FLASK_DATABASE_HOST'),
    "port": os.environ.get('FLASK_DATABASE_PORT'),
    "db": os.environ.get('FLASK_DATABASE')
}

sDialectLuaMedic = f"{dEngineLuaMedic['connector']}://{dEngineLuaMedic['user']}:"\
    f"{dEngineLuaMedic['password']}@{dEngineLuaMedic['host']}:{dEngineLuaMedic['port']}/{dEngineLuaMedic['db']}"


dEngineLuaMedicDeploy = {
    "connector": os.environ.get('FLASK_DATABASE_CONNECTOR_D'),
    "user": os.environ.get('FLASK_DATABASE_USER_D'),
    "password": os.environ.get('FLASK_DATABASE_PASSWORD_D'),
    "host": os.environ.get('FLASK_DATABASE_HOST_D'),
    "port": os.environ.get('FLASK_DATABASE_PORT_D'),
    "db": os.environ.get('FLASK_DATABASE_D')
}


sDialectLuaMedicDeploy = f"{dEngineLuaMedicDeploy['connector']}://{dEngineLuaMedicDeploy['user']}:"\
    f"{dEngineLuaMedicDeploy['password']}@{dEngineLuaMedicDeploy['host']}:{dEngineLuaMedicDeploy['port']}/{dEngineLuaMedicDeploy['db']}"



print(sDialectLuaMedic)
metadata_obj = MetaData()
engine = create_engine(sDialect, echo=True, future=True)
engineLuaMedic =  create_engine(sDialectLuaMedic, echo=True, future=True)
Base = declarative_base()
