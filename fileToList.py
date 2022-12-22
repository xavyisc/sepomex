#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def fileToList(file):
    """
    recibe archivo de texto descargado de SEPOMEX
    y retorna una lista
    """
    with open(file, 'r', encoding='latin-1') as cpFile:
        listCPFile = cpFile.readlines()
        del listCPFile[0:2]
        return listCPFile

fileSEPOMEX = os.environ.get("FILE_SEPOMEX")
listCPFile = fileToList(fileSEPOMEX)
