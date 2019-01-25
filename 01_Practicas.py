#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

# Manejo de Strings
def manejoStrings():
    prueba = "Hola Mundo" #
    print(prueba)    #Imprime hola mundo
    print(prueba[0]) # Imprime el primer char del string
    print(prueba[:-2]) # Imprime todo el string menos los ultimos 2 chars
    print(prueba[2:-2]) # Imprime el string empezando desde el segundo char y le resta los ultimos 2 chars


def listas():
    lista1 = ["Mario", "Andrés", "Zamora", "Madriz", "una lista", [1, 2]]
    print(lista1)   #
    print("El nombre es: " + lista1[0])
    lista1[0] = "Keren"
    print("Ahora el nombre es: " + lista1[0])
    # El menos 3 funciona para contar de atras para adelante
    print("El apellido es: " + lista1[-3])
    # Hace una sublista con los elementos sin incluir el ultimo elemento
    print("Nombre Completo: " + ' '.join(lista1[0:4]))
    # Convertir un STR a UTF-8
    print(lista1[-1])


def diccionarios():
    diccionario = {"Informe Auditoria": "DFOE-01-07-2016",
                   "Contratacion": "DCA-1519489.pdf",
                   "Informe Auditoria1": "DFOE-01-07-2000"}

    print(diccionario["Informe Auditoria"])
    print(diccionario["Informe Auditoria1"])

    # Asignacion de valores
    diccionario["Informe Auditoria1"] = "Mortadela"

    print(diccionario["Informe Auditoria1"])
    print(diccionario.items())


def condicionales():
    """Muestra los tipos de IF Y ELSE"""
    texto = "www.mortasoft.com"
    num = 10

    # Un IF Normal
    if texto == "www.mortasoft.com":
        print
        "Son iguales"
    else:
        print
        "No son iguales"

    # Un if con Elif
    if num > 10:
        print
        "Mayor a 10"
    elif num < 10:
        print
        "Menor a 10"
    else:
        print
        "Es 10"

    # Un if corto
    var = "El numero es par" if (num % 2 == 0) else "El numero es impar"
    print(var)


def ciclos():
    """Crea 2 ciclos"""
    veces = 1
    while veces <= 10:
        print("Voy por: " + str(veces))
        veces = veces + 1

    elem = ["Uno", "Dos", "Tres", "Cuatro"]
    for i in elem:
        print(i)


def funciones1(*param):
    """Suma todos los numeros que le pasemos por parametros"""
    sum = 0
    for i in param:
        sum += i
    return str(sum)


def funciones2(x, y):
    """Devuelve x+2 y y+3"""
    return x + 2, y + 3


class Biblioteca_funciones:
    def __init__(self, prueba):
        self.prueba = prueba
        print(prueba)

    def funcion1(self):
        print("El numero es:" + str(self.prueba))


class Biblio(Biblioteca_funciones):
    pass

class ErrorPersonalizado(Exception):

    def __init__(self,valor):
        self.valor = valor

    def __str__(self):
        return "Error "+ str(self.valor)


def excepciones():
    try:
        a = 50/0
    except:
        print("No se puede dividir entre 0")

    # Se pueden definir distintos except para cada una de las excepciones
    try:
        a = 0/0
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except (ValueError,NameError):
        print("Error de valor")
    else:
        print("Todo bien!!!")

def leerArchivoLineaPorLinea():
    file = open("archivo.txt", "r")
    for line in file.read().split('\n'):
        print(line)

def leerArchivo():
    file = open("archivo.txt","r")
    line = file.readlines()
    return line


def escribirArchivo():
    file = open("archivo2.txt","w")

    lista = leerArchivo()

    for linea in lista:
        print(linea)
        file.write("Viene desde el otro laddo " + linea)


##excepciones()

#leerArchivo()
#leerArchivoLineaPorLinea()
#escribirArchivo()


#import Modulo1

#manejoStrings()
listas()
#diccionarios()
#condicionales()
#ciclos()

#print("La suma es:" + funciones1(1, 2, 23, 3, 123, 23, 4, 5, 3, 2, 3, 5, 3))
#print(funciones2(1, 2)[0])
#print(funciones2(1, 2)[1])
#print(funciones2(1, 2))

#func = Biblioteca_funciones(6)
#func.funcion1()
