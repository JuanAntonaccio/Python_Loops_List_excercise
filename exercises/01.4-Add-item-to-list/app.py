import random
#Remember import random function here:

my_list = [4,5,734,43,45]

#The magic is here:

for i in range(0,10):
    numero=random.randint(1, 100)
    my_list.append(numero)

print(my_list)    
