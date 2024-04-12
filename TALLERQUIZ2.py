import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sp

#PUNTO 1:
MATRIZ1=np.random.rand(10,10,10,1200)
print(MATRIZ1) 
print("\n")

#PUNTO 2:
MATRIZ2=MATRIZ1[:,:,:,0].copy()
print(MATRIZ2)
print("\n")

#PUNTO 3:
print(f"La forma de la matriz es >>> {MATRIZ2.shape}")
print(f"El total de datos de la matriz es >>> {MATRIZ2.size}")
print(f"Las dimensiones de la matriz son >>> {MATRIZ2.ndim}")
print(f"Tipo de datos de la matriz >>> {MATRIZ2.dtype}")
print(f"itemsize de la matriz >>> {MATRIZ2.itemsize}")
print(f"nbytes de la matriz >>> {MATRIZ2.nbytes}")
print("\n")

#PUNTO 4:
MATRIZ3=MATRIZ2.reshape((10,100))
print(MATRIZ3)
print("\n")

#PUNTO 5:
def dataframe(MATRIZ3):
    M=pd.DataFrame(MATRIZ3)
    return M 
#Llamado de la función
a=dataframe(MATRIZ3)
print(a)

#PUNTO 6:
def archiMatCsv():
    while True:
        usuario=input("Ingrese en mayúscula la letra M , si desea cargar un archivo mat \nIngrese la letra C en mayúscula, si desea cargar un archivo csv \n>>>>>  ")
        if usuario =="M":
            x=input("Ingrese la ruta del archivo MAT >>> ")
            mat=sp.loadmat(x)
            return mat 
        elif usuario == "C":
            y=input("Ingrese la ruta del archivo CSV >>> ")
            csv=pd.read_csv(y)
            return csv
        else:
            print("OPCIÓN INCORRECTA, INGRESE M O C EN MAYÚSCULA")
            continue 
#Llamado de la función      
b=archiMatCsv()
print(b)

#PUNTO 7:
def suma(arreglo,axis):
    sumado=np.sum(arreglo,axis=axis)
    return sumado 

def resta(arreglo,axis):
    resta=np.subtract(arreglo,axis=axis)
    return resta 

def multi(arreglo,axis):
    multi=np.multiply(arreglo,axis=axis)
    return multi

def division(arreglo,axis):
    division=np.divide(arreglo,axis=axis)
    return division 

def log(arreglo,axis):
    log=np.log(arreglo,axis=axis)
    return log 

def promedio(arreglo,axis):
    prom=np.mean(arreglo,axis=axis)
    return prom

def desviacion(arreglo,axis):
    des=np.std(arreglo,axis=axis)
    return des

#PUNTO 8
archivo= pd.read_csv("pacientesRayosX.csv")
print(archivo.head(16))







