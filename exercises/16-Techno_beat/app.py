def lyrics_generator(list):
    cadena=""
    contador=0
    for i in list:
        if i==0:
            cadena+="Boom "
            contador=0
        if i==1:
            cadena+="Drop the base "    
            contador+=1
            if contador==3:
                cadena+="!!!Break the base!!! "
                contador=0
    return cadena

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))