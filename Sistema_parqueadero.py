import random

# Software para calcular valor a pagar en el parqueadero con ticket

# Entrada de datos
placaVehiculo = input("Ingrese la placa del vehículo: ")
marcaVehiculo = input("Ingrese la marca del vehículo: ")
horaEntrada = float(input("Ingrese la hora de entrada (ej: 8.0 para 8:00): "))
horaSalida = float(input("Ingrese la hora de salida (ej: 20.5 para 20:30): "))

# Generar ticket único
ticket = random.randint(1000, 9999)  # número aleatorio de 4 dígitos

# Cálculo del tiempo de estadía
tiempoEstadia = horaSalida - horaEntrada

# Cálculo del valor a pagar
precioPrimeraHora = 3000
precioHoraAdicional = 2000

if tiempoEstadia <= 1:
    valorPagar = precioPrimeraHora
else:
    valorPagar = precioPrimeraHora + (tiempoEstadia - 1) * precioHoraAdicional

# Verificar si aplica tarifa especial
if tiempoEstadia > 10:
    tarifaEspecial = True
    tipoTarifa = "Especial"
else:
    tarifaEspecial = False
    tipoTarifa = "Normal"

# Salida de información
print("\n--- Resumen del Parqueadero ---")
print("Vehículo:", marcaVehiculo, "-", placaVehiculo)
print("Tiempo de estadía:", tiempoEstadia, "horas")
print("Tipo de tarifa:", tipoTarifa)
print("Valor a pagar: $", int(valorPagar))
print("Ticket para retirar vehículo:", ticket)