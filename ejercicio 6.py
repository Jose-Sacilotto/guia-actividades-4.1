# Un pintor sabe que con una pintura determinada puede pintar 3,6 metros cuadrados por cada medio litro. Sabiendo la altura y el largo de la pared a pintar, informar cuántos litros de pintura utilizará. (Altura y Largo en metros).
alto=float(input("ingrese la altura de la pared: "))
ancho=float(input("ingrese el ancho de la pared: "))
proporcion=3.6*2
resultado1=alto*ancho
print(f"los litros de pintura que necesita son: {resultado1/proporcion}")
