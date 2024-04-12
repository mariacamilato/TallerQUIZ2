import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sp

#PUNTO1:
MATRIZ1=np.random.rand(10,10,10,1200)
print(MATRIZ1) 
print("\n")

#PUNTO2:
MATRIZ2=MATRIZ1[:,:,:,0].copy()
print(MATRIZ2)
print("\n")

#PUNTO3:
print(f"La forma de la matriz es >>> {MATRIZ2.shape}")
print(f"El total de datos de la matriz es >>> {MATRIZ2.size}")
print(f"Las dimensiones de la matriz son >>> {MATRIZ2.ndim}")
print(f"Tipo de datos de la matriz >>> {MATRIZ2.dtype}")
print(f"itemsize de la matriz >>> {MATRIZ2.itemsize}")
print(f"nbytes de la matriz >>> {MATRIZ2.nbytes}")
print("\n")

#PUNTO4:
MATRIZ3=MATRIZ2.reshape((10,100))
print(MATRIZ3)
print("\n")

#PUNTO5:
def dataframe(MATRIZ3):
    M=pd.DataFrame(MATRIZ3)
    return M 
dataframe(MATRIZ3)
print("\n")
