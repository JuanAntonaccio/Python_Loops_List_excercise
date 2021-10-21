
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }
#spanish_translations["love"]="amor"
#spanish_translations["code"]="codigo"
#spanish_translations["smart"]="inteligente"
otro_dict = {"love":"amor","code":"codigo","smart":"inteligente"}
for key in otro_dict:
    spanish_translations[key]=otro_dict[key]
    
    
     
print("Translation", spanish_translations["dog"])
print("All", spanish_translations)

