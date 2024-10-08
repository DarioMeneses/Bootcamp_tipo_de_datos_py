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

contacts = {"Dario": {"Apeelido:": "Meneses",
                        "Altura:": 1.64,
                        "Edad:": 28,
                        "Telefono:": 3168117340,
                        "Signo zodiacal:": "Virgo",
                        "Serie favorita:": "Nanatsu no taizai",
                        "Cancion favorita:": "Todo hombre es una historia - Kraken",
                        "Comida favorita:": "Papas fritas",
                        "Lugar soñado vacaciones:": "Suiza",
                        "Habilidad secreta:": "Leer mentes",
                        "Pasatiempo:": "Tocar guitarra",
                        "Heroe o persona que admiras:": "Elkin Ramirez",
                        "Libro que mas me ha impactado:": "La senda del perdedor",
                        "Cenar con alguien:": "Jose cruz",
                        "Superpoder:": "Manipular la materia",
                        "Que logro personal te enorgullece:": "Cumplir con trabajos que parecian improbables"
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