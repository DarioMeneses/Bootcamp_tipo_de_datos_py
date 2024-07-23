to_do = ["Alistar la pelicula",
         "Freir crispetas",
         "Preparar pasabocas"]

print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print (type(numbers))
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print (len(mix))
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("tercer elemento", mix[2])
print("cuarto elemento", mix[3])
print("quinto elemento", mix[4])
print("ultimo elemento", mix[-1])
print(mix[0:2]) #Imprime desde el elemento cero hasta el elemento anterior al elemento de la posicion 2
print(mix[:2])
print(mix[2:])
mix.append("Dario Meneses") #Agegar un elemento a la lista
print(mix)
mix.insert(1,["a", "b"]) 
print(mix)
print(mix.index(["a", "b"]))
numbers1 = [1, 2, 100, 90.45, 3, 4, 5]
print(numbers1)
print("Mayor:", max(numbers1)) #Numero mayor
print("Menor:", min(numbers1)) #Numero menor
del numbers1 [-1] #Eliminar el ultimo elemento
print(numbers1)
del numbers1 [:3] #Eliminar desde el primer elemento hasta el elemento 2
print(numbers1)
del numbers1 #Eliminar una lista
#print(numbers1)