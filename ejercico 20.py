#Ingresar como dato el perímetro de un cuadrado. Calcular e imprimir el volumen del cubo que tiene como lado el cuadrado antes mencionado.
perimetrocuadrado=float(input("Ingrese el perimetro de un cuadrado: "))
lado=perimetrocuadrado/4
volumen=float(lado**3)
print(f"El volumen del cubo es: {volumen}")
