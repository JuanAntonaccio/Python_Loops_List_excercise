
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
hello=[]

#your code go here:
for i in my_list:
    if isinstance(i, dict) or isinstance(i,list):
       hello.append(i)
    
    
    

print(hello)
