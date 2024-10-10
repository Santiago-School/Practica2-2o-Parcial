print("Francisco Santiago Carrasco Correa 0421 3°W 09/10/24")
print(" ")

def ultimapalabra(frase):
    # eliminamos espacios en blanco al inicio y al final
    frase = frase.strip()
    
    # dividimos la frase en palabras usando espacios como separador
    palabras = frase.split()
    
    # si hay palabras, regresamos la longitud de la ultima
    if palabras:
        return len(palabras[-1])
    else:
        return 0  # regresamos 0 si no hay palabras

# ejemplo de uso
texto = "   Santiago no es un infiel   "
longitud = ultimapalabra(texto)

print("la longitud de la última palabra es:", longitud)
