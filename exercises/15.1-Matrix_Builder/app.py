import random

def matrixBuilder(dato):
    matriz=[1] * dato 
    for i in range(dato):
        matriz[i]= [1]*dato

    return matriz

a = random.randint(1,5)
nueva=matrixBuilder(a)
#print(a)
print(nueva)

