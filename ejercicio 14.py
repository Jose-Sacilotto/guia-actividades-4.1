#Ingresar por teclado un lado y la hipotenusa de un triángulo rectángulo, calcular e imprimir el lado restante, la superficie y los ángulos de dicho triángulo.
import math
from math import radians
lado=float(input("Ingrese un lado del triangulo: "))
hipotenusa=float(input("Ingrese la hipotenusa del triangulo: "))
ladox=float(hipotenusa**2-lado**2)**0.5
superficie=float((lado*ladox)/2)
angulo=math.degrees(math.asin(lado/hipotenusa))
print(f"lado restante {ladox}, superficie {superficie}")
print(f"angulo 1= 90°, angulo 2= {angulo}°, angulo 3= {180-90-angulo}°")
