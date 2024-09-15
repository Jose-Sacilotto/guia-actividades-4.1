#Teniendo como dato la hipotenusa y el ángulo que forma ésta con la base de un triángulo rectángulo. calcular e imprimir los datos y ángulos restantes.
valorhipotenusa=float(input("Ingrese el valor de la hipotenusa: "))
angulo=float(input("Ingrese el valor del angulo: "))
print(f"El valor de la hipotenusa es: {valorhipotenusa}, El valor del angulo base es:{angulo}, el valor del angulo n°2 es 90°, el valor del angulo n°3 es: {180-90-angulo}")
