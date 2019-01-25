#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sqlite3 as dbapi
from datetime import datetime, date

db = dbapi.connect("pyDb.dat")
cursor = db.cursor()

try:
    # Se crea la base de datos
    cursor.execute("""create table empleados (dni text,nombre text,departamento text, fechaCreación date)""")
except:
    print("La tabla ya existe")

insertar = True

# Se insertan los datos en la base de datos
for i in range(1):
    if insertar:
        cursor.execute("""insert into empleados values('AAA-01','Mario Zamora','Secretaria Técnica',?) """,(datetime.now(),))

#Se hace un commit de los datos
db.commit()

if insertar:
    cursor.execute("""select * from empleados""")
else:
    cursor.execute("""select count(*) from empleados""")

cant = 0

for tupla in cursor.fetchall():
    print(tupla)
    cant = cant +1

print("La base de datos tiene",cant,"elementos...")

cursor.close()
db.close()
