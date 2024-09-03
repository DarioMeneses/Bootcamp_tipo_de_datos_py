def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
 while True:
    print("seleccione una operacion")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    option = input("Ingrese su opcion (1, 2, 3, 4, 5) ")
    
    if option == "5":
        print("Saliendo de la calculadora")
        break
    
    if option in ["1","2","3","4"]:
        numb1 = float(input("Ingrese el primer numero: "))
        numb2 = float(input("Ingrese el segundo numero: "))
        
        if option == "1":
            print("La suma es: ", add(numb1,numb2))
            
        elif option == "2":
            print("La resta es: ", subtract(numb1, numb2))
            
        elif option == "3":
            print("La multiplicacion es: ", multiply(numb1, numb2))
            
        elif option == "4":
                if numb2 == 0:
                    print("Error: No se puede dividir por cero.")
                else:
                    print("La división es:", divide(numb1,numb2))
            
    else:
            print("Opcion invalida, intenta nuevamente")
            
calculator()