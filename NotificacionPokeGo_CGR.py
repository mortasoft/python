#!/usr/bin/python
import gi
import sys
import time,os
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def leerArchivo():
    try:
        file = open("/home/mortasoft2/Desarrollo/PokemonGo-BotCGR/data/caught-mario.andres.zamora@cgr.go.cr.json","r")
        line = file.readlines()
        return line[-1:]
    except:
        return file

def monitorear():

    modificado=""

    while True:
        moddate = os.stat("/home/mortasoft2/Desarrollo/PokemonGo-BotCGR/data/caught-mario.andres.zamora@cgr.go.cr.json")[8]
        #print(time.ctime(moddate))
        if moddate!=modificado and modificado!="":
            imprimir()
            modificado=""
        else:
            modificado = moddate

def imprimir():
    pokemon = leerArchivo()
    nombre = pokemon[0].split(",")[2].split('"')[3]
    cp = pokemon[0].split(",")[1].split(":")[1]
    msg = "Se atrapó un "+ nombre
    msg += "\nCP: "+cp
    print(msg)
    notificacion(msg)

def notificacion(msg):
    Notify.init("Hello world")
    Hello = Notify.Notification.new("Pokemon Atrapado", msg, "dialog-information")
    Hello.show()

monitorear()
#print(leerArchivo())
