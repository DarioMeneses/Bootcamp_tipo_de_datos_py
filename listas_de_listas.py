def matrices(): 
    matriz = [[1,2,3],
              [4,5,6],
              [7,8,9]]
 
    for matri in matriz:
        print(matri)
    
    elemento1 = matriz[0][1]
    print(elemento1)
    matriz[0][1] = 10
    for matri in matriz:
        print(matri)
matrices()

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matriz)
print(matriz[0])

numbers = (1,2,3,4,5,6)
print(numbers)
print(type(numbers))
print(numbers[0])

