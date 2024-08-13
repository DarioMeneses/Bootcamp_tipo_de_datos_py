lista = list (["Hola", "Dario", 1995, 25, 8, True])
print(lista)
cadena = "Hola"
resultado = len(cadena) # Nos devuelve la longitud de la lista (la cantidad de caracteres)
print(resultado)
print(len(lista))
#Append
lista.append("28 años") #Agrega un elemento al final de la lista
# Insert
lista.insert(2, "Meneses")
# Extend
lista.extend(["Instagram: dario_asbeel", "Electricista residencial e industrial"])

print(lista)
print(len(lista), " Elementos")
#Pop eliminar elemetos de la lista
lista.pop(-1)
print((lista), len(lista), " elementos")
# Remove eliminar elementos por su valor
lista.remove("Instagram: dario_asbeel")
print((lista), len(lista), " elementos")

# Sort odena los elementos en orden ascendente y reverse invierte ese orden
lista2 = list([1995, 8, 25, 28, True])
lista2.append(2024)
lista2.insert(0, False)
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
Buscar_elemento = lista2.index(25)
print(Buscar_elemento)