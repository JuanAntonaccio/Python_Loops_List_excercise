Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
   valor = (x*9/5)+32
   return valor
result = list(map(fahrenheit_values, Celsius_values))
print(result)
