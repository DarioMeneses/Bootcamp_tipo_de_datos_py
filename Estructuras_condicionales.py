# x = 10
# if x > 5:
#     print("x es mayor que 5")
# elif x == 5:
#     print("x es igual que 5")
# else:
#     print("x es menor que 5")

x = 15
y = 26
if x > 10 and y > 25:
    print(" X es mayor que 10 y Y es mayor que 25")
if x > 10 or y > 25:
    print("X es mayor que 10 o Y es mayor que 25")
if not x>10:
    print("X no es mayor que 10")
    
is_member = True
age = 15

if is_member:
    if age >= 15:
        print("Puedes entrar")
    else:
        print("No puedes entrar")
else:
    print("No eres miembro y no tienes acceso")
