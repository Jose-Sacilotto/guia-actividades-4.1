# Dados dos lados de un triángulo, calcular la hipotenusa mediante Pitágoras.
import math
catetoa=float(input("Ingresa el valor de un lado del triangulo: "))
catetob=float(input("Ingresa el valor de el otro lado del triangulo: "))
c = math.sqrt(catetoa**2 + catetob**2)
print(f"La hipotenusa del triangulo es: {c}")