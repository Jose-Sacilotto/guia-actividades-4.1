#Dado un vehículo de cuatro ruedas; cada una con un radio de cincuenta centímetros, calcular e imprimir cuántas vueltas dará cada rueda para desplazarse un kilómetro.
import math
diametro=int(50*2)
circunferencia=math.pi*diametro
distancia=100000
vueltas=distancia/circunferencia
print(f"cada rueda dara: {vueltas}")
