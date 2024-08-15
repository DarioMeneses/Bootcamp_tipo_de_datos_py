numbers = { 1: "uno",
            2: "dos",
            3: "tres"           
}
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])

informacion = { "Nombre: " : "Dario",
                "Apellido: " : "Meneses",
                "Edad: " : 28,
                "Cena: " : False 
    
}
for dato, valor in informacion.items():
    print(f"{dato}{valor}")

del informacion["Cena: "]
print(informacion)
claves = informacion.keys()
print(claves)
print(type(claves))
values = informacion.values()
print(values)
pairs = informacion.items()
print(pairs)

contacts = {"Jheyson": {"Apeelido:": "Galviz",
                        "Altura:": 1.69,
                        "Edad:": 32,
                        "Telefono:": 3167417556,
                        "Signo zodiacal:": "Picis",
                        "Serie favorita:": "Silicon Valley",
                        "Cancion favorita:": "Todo ira bien - Chenoa",
                        "Comida favorita:": "Frijoles, carne",
                        "Lugar soñado vacaciones:": "Silicon valley",
                        "Habilidad secreta:": "Repetir el dia para salvar muertos",
                        "Pasatiempo:": "Caminar con mis perros",
                        "Heroe o persona que admiras:": "Elon musk",
                        "Libro que mas me ha impactado:": "Salvese quien pueda",
                        "Cenar con alguien:": "Freddy Vega CEO Platzi",
                        "Superpoder:": "Vajar por multiversos",
                        "Que logro personal te enorgullece:": "Aprender python"
                        } ,          
                "Jose": {"Apeelido:": "Martinez",
                        "Altura:": 1.82,
                        "Edad:": 26,
                        "Telefono:": 3156789012,
                        "Signo zodiacal:": "Ciscor",
                        "Serie favorita:": "Breaking Bad",
                        "Cancion favorita:": "No puedo olvidar",
                        "Comida favorita:": "Pollo, carne",
                        "Lugar soñado vacaciones:": "Breaking Bad",
                        "Habilidad secreta:": "Cambiar el tiempo para volar",
                        "Pasatiempo:": "Leer",
                        "Heroe o persona que admiras:": "Chandler Bing",
                        "Libro que mas me ha impactado:": "El camino a la felicidad",
                        "Cenar con alguien:": "Enrrique Bunbury"
            }    
}
for nombre, detalles in contacts.items():
    print(f"Nombre: {nombre}")
    for clave, valor in detalles.items():
        print(f"{clave} {valor}")
    print("\n")