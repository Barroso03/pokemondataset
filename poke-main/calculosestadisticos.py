
from math import * #Este módulo proporciona acceso a las funciones matemáticas
import pandas as pd # Libreria para trabajar con dataframes (tablas)
import matplotlib as plt #Para graficar (no se importa bien la librería)

datos= pd.read_csv('C:/pokemondataset/Pokemon.csv') #Leer el archivo csv

class Calculo:
    def __init__(self, n, lista_producto, media, lista_opiniones, lista_producto2,varianza, intervalo, limite_inferior, limite_superior,desviacion_tipica,amplitud):
        
        self.n=n
        self.lista_producto=lista_producto
        self.media=media
        self.lista_opiniones=lista_opiniones
        self.lista_producto2=lista_producto2
        self.varianza=varianza
        self.intervalo=intervalo
        self.limite_inferior=limite_inferior
        self.limite_superior=limite_superior
        self.desviacion_tipica=desviacion_tipica
        self.amplitud=amplitud

    def grafica_datos_excell():
        #grafica de criticas_peliculas.csv
        lista_producto = list(datos['Total'])
        eje_x = list(datos['Name'])
        eje_y = lista_producto 
        plt.bar(eje_x,eje_y, color= 'blue')
        plt.xlabel('Nombre pokemon')
        plt.ylabel('Puntos')
        plt.title('Grafica pokemon de peliculas')
        plt.show()

 
    def Operaciones_estadística(self):
        lista_producto = list(datos['Total']) #Seleccionar la columna del producto
        media = sum(lista_producto)/len(lista_producto) #Calculamos la media
        
        
        #A continuación se calcula la varianza
        # calcula la varianza con a media hallada antes
        varianza = 0
        for i in lista_producto:
            varianza += (i-media)**2
        varianza = varianza/len(lista_producto)
        #Calculamos la desviación típica
        desviacion_tipica = sqrt(varianza)
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")
        #SI QUISIESEMOS RESONDEAR LOS VALORES TAN SOLO AÑADIMO ''ROUND'' DELANTE DE LOS VALORES
        #print(f"\n La media es {round(media,2)}, la varianza {round(varianza,2)} y la desviación típica {round(desviacion_tipica,2)} \n ")
    def percentil_68(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        lista_producto = list(datos['Total']) #Seleccionar la columna del product
        n = len(lista_producto) #Seleccionar la columna de la cantidad de votos
        total = 0
        for i in n:
            total += i
        k = 68
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 1 #Datos de la tabla
        limite_superior = 2 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 136 #Datos de la tabla
        frecuencia_relativa_intervalo = 133 #Datos de la tabla
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_68 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 68 es {percentil_68} \n ")
    def percentil_95(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        lista_producto = list(datos['Total']) #Seleccionar la columna del product
        n =  len(lista_producto) #Seleccionar la columna del product 
        total = 0
        for i in n:
            total += i
        k = 95
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 3 #Datos de la tabla
        limite_superior = 4 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 414 #Datos de la tabla 
        frecuencia_relativa_intervalo = 99 #Datos de la tabla
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_95 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 95 es {percentil_95} \n ")
    def percentil_97(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        lista_producto = list(datos['Total']) #Seleccionar la columna del product
        n =  len(lista_producto) #Seleccionar la columna del product
        total = 0
        for i in n:
            total += i
        k = 97
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 4 #Datos de la tabla
        limite_superior = 5 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 513
        frecuencia_relativa_intervalo = 40
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_97 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 97 es {percentil_97} \n ")
# printeamos todas las funciones
print(Calculo.Operaciones_estadística('media','varianza','desviacion_tipica'))
print(Calculo.percentil_68('percentil_68'))
print(Calculo.percentil_95('percentil_95'))
print(Calculo.percentil_97('percentil_97'))
#grafica_datos_excell()
print(Calculo.Operaciones_estadística('eje_x','eje_y'))

