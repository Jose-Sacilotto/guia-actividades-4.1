#Hacer un programa que ingresando como datos:
#   a. Kms. recorridos por un vehículo.
#   b. Precio del combustible por litro.
#   c. Kms. recorridos por cada litro
# Calcule:
#   i. La cantidad de litros consumidos
#   ii. Importe gastado en combustible.
#   iii. Imprimir los resultados
#   iv. Ejemplificar y realizar la prueba de escritorio
kilometroxvehiculo=float(input("Ingrese la cantidad de kilometros recorridos del vehiculo: "))
precioxlitro=float(input("Ingrese el precio de combustible por litro: "))
kilometrosxlitro=float(input("Ingrese la cantidad de kilometros por litro de combustible: "))
litrosconsumidos=float(kilometroxvehiculo/kilometrosxlitro)
importegastado=float(litrosconsumidos*precioxlitro)
print(f"La cantidad de litros consumidos es de: {litrosconsumidos}")
print(f"El importe gastado de combustible es de {importegastado}$")
