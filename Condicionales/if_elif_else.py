# Salarios promedio mensuales de algunos paises suramericanos  (en dólares)
salario_Uruguay = 1137    
salario_Chile = 837  
salario_Colombia = 454      
salario_Venezuela = 143  


salario_usuario = float(input("Introduce tu salario mensual (en dólares): "))

if salario_usuario < salario_Venezuela:
    print(f"Tu salario es menor al promedio en Venezuela.")
    print(f"Ojo es el salario mas bajo de la lista.")
elif salario_usuario < salario_Colombia:
    print(f"Tu salario es menor al promedio en Colombia.")
    print(f"Pero mayor al promedio en Venezuela.")
    
elif salario_usuario < salario_Chile:
    print(f"Tu salario es menor al promedio en Chile.")
    print(f"Pero mayor al promedio en Colombia y Venezuela")

elif salario_usuario < salario_Uruguay:
    print(f"Tu salario es menor al promedio en Uruguay.")
    print(f"Pero mayor al promedio en Chile, Colombia y Venezuela")
    
else:
    print("Tu salario es igual o superior al promedio en Uruguay, el país con el mayor promedio de esta lista.")
    print("¡Felicidades! Tienes un salario muy competitivo.")



