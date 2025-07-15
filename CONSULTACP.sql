select * from hgap.SEPOMEX where d_codigo = 39715;
SELECT 
	ta.id as "id_tipoAsentamiento",
    ta.nomTipoAsentamiento,
    e.id as "id_estado",
    e.nomEstado,
    m.id_Sepomex as "id_municipio",
    m.nomMunicipio,
    c.id_Sepomex as "id_ciudad",
    c.nomCiudad,
    a.id,
    a.id as "id_asentamiento"
    a.nomAsentamiento,
    a.codigoPostal
FROM SEPOMEX_asentamientos a
LEFT JOIN SEPOMEX_tiposAsentamiento ta
ON a.id_tipoAsentamiento = ta.id
LEFT JOIN SEPOMEX_estados e
ON a.id_estado = e.id
LEFT JOIN SEPOMEX_municipios m
ON a.id_municipio = m.id_Sepomex and a.id_estado = m.id_estado
LEFT JOIN SEPOMEX_ciudades c
ON a.id_ciudad = c.id_Sepomex and a.id_estado = c.id_estado
WHERE a.codigoPostal = 40360;

-- SELECT * FROM SEPOMEX_municipios;
-- SELECT * FROM SEPOMEX_ciudades where id_Sepomex= 4;