theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def verificar(item):
    a = ""
    if item==0:
        a="woko"
    else:
        a="wiki"
    return a        
new_list = list(map(verificar,theBools))
print(new_list)


