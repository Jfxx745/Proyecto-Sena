import random
from datetime import datetime

# Software para calcular valor a pagar en el parqueadero con ticket

# Validar placa (debe tener 6 caracteres)
while True:
    placaVehiculo = input("Ingrese la placa del vehículo (6 caracteres): ")
    if len(placaVehiculo) == 6:
        break
    else:
        print("Error: la placa debe tener exactamente 6 caracteres.")

marcaVehiculo = input("Ingrese la marca del vehículo: ")

horaEntrada = input("Ingrese la hora de entrada (HH:MM): ")
horaSalida = input("Ingrese la hora de salida (HH:MM): ")

# Convertir a formato de hora
formato = "%H:%M"
horaEntrada_dt = datetime.strptime(horaEntrada, formato)
horaSalida_dt = datetime.strptime(horaSalida, formato)

# Generar ticket único
ticket = random.randint(1000, 9999)

# Cálculo del tiempo de estadía
tiempo = horaSalida_dt - horaEntrada_dt
tiempoEstadia = tiempo.total_seconds() / 3600  # convertir a horas

# Tarifas
precioPrimeraHora = 3000
precioHoraAdicional = 2000

# Cálculo del valor a pagar
if tiempoEstadia <= 1:
    valorPagar = precioPrimeraHora
else:
    valorPagar = precioPrimeraHora + (tiempoEstadia - 1) * precioHoraAdicional

# Verificar tarifa especial
if tiempoEstadia > 10:
    tipoTarifa = "Especial"
else:
    tipoTarifa = "Normal"

# Salida
print("\n--- Resumen del Parqueadero ---")
print("Vehículo:", marcaVehiculo, "-", placaVehiculo)
print("Tiempo de estadía:", round(tiempoEstadia, 2), "horas")
print("Tipo de tarifa:", tipoTarifa)
print("Valor a pagar: $", int(valorPagar))
print("Ticket para retirar vehículo:", ticket)