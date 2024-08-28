# Ejemplo de como funcionan los iteradores
my_list = [1, 2, 3, 4] 
my_iter = iter(my_list) # Un iterador es un objeto que nos permite recorrer una coleccion (como una lista) uno por uno
# Next() nos da el siguiente elemento de la coleccion cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# Iterando cadenas de texto con iter
print()
text = "Hola mundo soy Dario"
iter_texto = iter(text)
for char in iter_texto:
    print(char)
print()    
# Iterador que genere numeros impares desde el 1 hasta el limite
odd_iter = iter(range(1, 10, 2)) # Genera numeros comenzando en 1, con salto de 2 hasta llegar a 9 el limite no se incluye
for num in odd_iter:
    print(num)
print()    
numb = (range(1,10,2))
for numero in numb:
    print(numero)    
print()    
def my_generator(): #Yield nos permite devolver un valor y pausar la funcion en ese punto
    yield 1
    yield "Dos"
    yield 3
for value in my_generator():
    print(value)
print()

#Fibonacci hace referencia a que vamos a obtener un valor sumando los 2 anteriores
def fibonacci(limit):
    a, b = 0, 1 # Inicia los dos primeros numeros de la secuencia de fibonacci
    while a < limit: # Continua generando numeros hasta llegar el limite
        yield a # Devuelve el valor actual de "a" y pausa la ejecuccion de la funcion
        a, b = b, a + b
for num in fibonacci(10):
    print(num)
  