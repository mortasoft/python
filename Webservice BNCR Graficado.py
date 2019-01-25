import matplotlib.pyplot as plt
import requests
import xml.etree.ElementTree as ET
import numpy as np
from scipy.interpolate import spline

def obtenerTipoCambio(tipo,fecha_inicio,fecha_final):
  if tipo == "compra":
    tcIndicador = 317 # Indicador del banco
  
  if tipo == "venta":
    tcIndicador = 318 # Indicador del banco
    
  tcFechaInicio = fecha_inicio
  tcFechaFinal = fecha_final
  tcNombre = 'persona'
  tnSubNiveles ='N'

  r = requests.post("http://indicadoreseconomicos.bccr.fi.cr/indicadoreseconomicos/WebServices/wsIndicadoresEconomicos.asmx/ObtenerIndicadoresEconomicos",
                    data={'tcIndicador': tcIndicador, 'tcFechaInicio': tcFechaInicio, 
                    'tcFechaFinal': tcFechaFinal, 'tcNombre': tcNombre, 'tnSubNiveles': tnSubNiveles })

  root = ET.fromstring( r.text )

  matrix = []
  for i in range( len( root[1][0] )):
      fila = []
      try: 
           fila.append( root[1][0][i][0].text )
      except: fila.append( "NA" )
      try:
         fila.append(  root[1][0][i][1].text )
      except: fila.append(  "NA" )
      try:

         fila.append(  root[1][0][i][2].text )
      except: fila.append( "NA" )
      matrix.append( fila )

  lista_graficar = []
  for i in range( len( matrix ) ) :
      if matrix[i][2] != "NA" and matrix[i][2] != "0.00000000" :
          lista_graficar.append( matrix[i][2] )
  
  return lista_graficar;

def mostrarGrafico(lista_graficar,linea_de_tendencia):
  if linea_de_tendencia == "si":
    a=np.float64(lista_graficar)
    b=np.array(range(len(a)))
    c=np.linspace(0,len(b),1000)
    d=np.polyfit(b,a,3)
    e=np.polyval(d,c)

    plt.plot(b,a,color="black")
    plt.plot(c,e,"-", color="red")
    plt.ylabel('Tipo de cambio')
    plt.legend(["Linea de tipo de cambio","Linea de Tendencia"])
    plt.show()
  
  if linea_de_tendencia == "no": 
    a=np.float64(lista_graficar)
    b=np.array(range(len(a)))
    plt.plot(b,a,color="green")
    plt.ylabel('Tipo de cambio')
    plt.xscale("linear")
    plt.show()
    
def mostrarGraficoAmbos(lista_graficar,lista_graficar2,linea_de_tendencia):
  
  # Esto es para el grafico de compra
  a=np.float64(lista_graficar)
  b=np.array(range(len(a)))
  c=np.linspace(0,len(b),1000)
  d=np.polyfit(b,a,3)
  e=np.polyval(d,c)

  # Esto es para el grafico de venta
  a2=np.float64(lista_graficar2)
  b2=np.array(range(len(a2)))
  c2=np.linspace(0,len(b2),1000)
  d2=np.polyfit(b2,a2,3)
  e2=np.polyval(d2,c2)

  plt.plot(b2,a2,color="blue") # Compra 
  plt.plot(b,a,color="black")  # Venta

  if linea_de_tendencia == "si":
    plt.plot(c,e,"-", color="red")
    plt.legend(["Linea de tipo de cambio compra","Linea de tipo de cambio venta","Linea de Tendencia"])
  if linea_de_tendencia == "no":
    plt.legend(["Linea de tipo de cambio compra","Linea de tipo de cambio venta"])

  plt.ylabel('Tipo de cambio')
  plt.show()
  
graficar=input(" Desea graficar compra,venta o ambos ")
fecha_inicio=input(" Ingrese la fecha de inicio (dia/mes/año):  ")
fecha_final=input(" Ingrese la fecha de final (dia/mes/año):  ")
linea_de_tendencia=input(" desea linea de tendencia si o no:  ")

if graficar == "compra":
  lista_graficar = obtenerTipoCambio("compra",fecha_inicio,fecha_final)
  mostrarGrafico(lista_graficar,linea_de_tendencia)
  
if graficar == "venta":
  lista_graficar = obtenerTipoCambio("venta",fecha_inicio,fecha_final)
  mostrarGrafico(lista_graficar,linea_de_tendencia)
  
if graficar == "ambos":
  lista_graficar = obtenerTipoCambio("compra",fecha_inicio,fecha_final)
  lista_graficar2 = obtenerTipoCambio("venta",fecha_inicio,fecha_final)
  mostrarGraficoAmbos(lista_graficar,lista_graficar2,linea_de_tendencia)
  