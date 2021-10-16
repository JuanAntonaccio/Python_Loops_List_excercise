arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumar_odd(lista):
    suma=0
    for i in lista:
        if i%2==1:
            suma+=i
    return suma

print(sumar_odd(arr))    

