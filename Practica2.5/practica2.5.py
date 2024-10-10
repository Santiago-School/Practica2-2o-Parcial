print(" ")
print("Francisco Santiago Carrasco Correa 0421 3°W 08/10/24")
print(" ")

#se designan las variables y el return
def areacirculo(radio):
    pi = 3.141592653589793
    return pi * radio ** 2

def volumencilindro(radio, altura):
    area_base = areacirculo(radio)
    return area_base * altura

# ejemplo del uso
radio = 5
altura = 10

area = areacirculo(radio)
volumen = volumencilindro(radio, altura)

print("area del circulo:", area)
print("volumen del cilindro:", volumen)
