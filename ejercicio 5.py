#Si un lote de terreno tiene X metros de frente por Y metros de fondo: calcular e imprimir la cantidad da metros de alambre para cercarlo. (X e Y serán leídos al comenzar el programa).
x=float(input("Ingrese los metros del ancho del terreno: "))
y=float(input("Ingrese los metros del largo del terreno: "))
largo=y*2
ancho=x*2
resultado=largo+ancho
print("la cantidad de metros de alambre que necesitas es de: ",resultado)