# El primer tipo de dato compuesto sera la lista

lista = ["Dario Meneses","tecnotutoriales Jheyson Galvis", True, 1.64]
print(lista[3])
lista[3] = "Asbeel"
print(lista[3])

# La tupla es una lista que no se puede modificar

tupla = ("Dario Meneses","tecnotutoriales Jheyson Galvis", True, 1.64)
print(tupla[1])
#tupla[0] = "Ruben"
#print(tupla[0])

# Conjunto o set, los conjuntos no permiten datos duplicados 

conjunto = {"Dario Meneses","tecnotutoriales Jheyson Galvis", True, 1.64, 1.64}
print(conjunto)

# Diccionario o map 

diccionario = {
    "nombre" : "Dario",
    "apellido" : "Meneses",
    "estatura" : 1.64,
    "estar en clase" : True
}
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])
print(diccionario["estar en clase"])
