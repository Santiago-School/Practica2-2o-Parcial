print("Francisco Santiago Carrasco Correa 0421 3°W 09/10/24")
print(" ")

def distancia(punto1, punto2):
    # extraemos las coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2
    # calculamos la distancia usando la formula
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# ejemplo de uso
punto_a = (16, 26)
punto_b = (46, 66)

distancia = distancia(punto_a, punto_b)

print("la distancia dirigida entre los puntos es:", distancia)
