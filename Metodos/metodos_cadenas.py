cadena1 = "Hola,Soy,Dario"
cadena2 = "Gracias por aprender python con nosotros"
#print(dir(cadena1))

resultado = "nuevo Texto"
print(resultado.lower()) #Minusculas
print(resultado.upper()) #Mayusculas
print(resultado.capitalize()) #Letra inicial en mayuscula

busqueda_find = cadena1.find("Hola") #Busca la posicion de un caracter incuido los espacios
print(busqueda_find)

busqueda_index = cadena1.index("a")
print(busqueda_index)

es_numerico = cadena1.isnumeric()
print(es_numerico)

es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)
print(len(cadena1))

empieza_con = cadena1.startswith("H")
termina_con = cadena1.endswith("o")
print(empieza_con, termina_con)

cadena_nueva = cadena1.replace("Hola","Mucho Gusto")
print(cadena_nueva)

cadena_separada = cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])