#Dadas la base y la altura de un triángulo, calcular la superficie. También conociendo uno de sus ángulos calcular los otros dos lados.
import math
from math import radians
base=float(input("Ingrese la base de un triangulo: "))
altura=float(input("Ingrese la altura de un triangulo: "))
angulo=math.radians(float(input("Ingrese el valor del angulo: ")))
print(f"la superficie del triangulo es: {(base*altura)/2}")
print(f"base= {base}\nlado1 = {base*math.sin(angulo)}\nlado2 = {base*math.cos(angulo)}")
