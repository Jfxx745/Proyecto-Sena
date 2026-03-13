import random
import math
from datetime import datetime

# --- VALIDAR PLACA ---
while True:
    placaVehiculo = input("Ingrese la placa del vehículo: ")
    
    if len(placaVehiculo) == 6:
        break
    else:
        print("Error: la placa debe tener exactamente 6 caracteres.")

# --- VALIDAR MARCA ---
while True:
    marcaVehiculo = input("Ingrese la marca del vehículo: ")
    
    if marcaVehiculo.strip() != "":
        break
    else:
        print("Error: debe ingresar la marca del vehículo.")

# --- VALIDAR HORA DE ENTRADA ---
while True:
    try:
        horaEntrada = input("Ingrese la hora de entrada (HH:MM): ")
        horaEntrada_dt = datetime.strptime(horaEntrada, "%H:%M")
        break
    except:
        print("Error: formato incorrecto. Debe ser HH:MM")

# --- VALIDAR HORA DE SALIDA ---
while True:
    try:
        horaSalida = input("Ingrese la hora de salida (HH:MM): ")
        horaSalida_dt = datetime.strptime(horaSalida, "%H:%M")
        
        if horaSalida_dt > horaEntrada_dt:
            break
        else:
            print("Error: la hora de salida debe ser mayor que la hora de entrada.")
    except:
        print("Error: formato incorrecto. Debe ser HH:MM")

# --- GENERAR TICKET ---
ticket = random.randint(1000, 9999)

# --- CALCULAR TIEMPO DE ESTADÍA ---
tiempo = horaSalida_dt - horaEntrada_dt
tiempoEstadia = tiempo.total_seconds() / 3600

# Redondear horas a cobrar
horasCobrar = math.ceil(tiempoEstadia)

# --- TARIFAS ---
precioPrimeraHora = 3000
precioHoraAdicional = 2000

# --- CALCULAR VALOR ---
if horasCobrar <= 1:
    valorPagar = precioPrimeraHora
else:
    valorPagar = precioPrimeraHora + (horasCobrar - 1) * precioHoraAdicional

# --- TARIFA ESPECIAL ---
if horasCobrar > 10:
    tipoTarifa = "Especial"
else:
    tipoTarifa = "Normal"

# --- SALIDA DE INFORMACIÓN ---
print("\n--- Resumen del Parqueadero ---")
print("Vehículo:", marcaVehiculo, "-", placaVehiculo)
print("Tiempo de estadía:", round(tiempoEstadia, 2), "horas")
print("Horas cobradas:", horasCobrar)
print("Tipo de tarifa:", tipoTarifa)
print("Valor a pagar: $", valorPagar)
print("Ticket para retirar vehículo:", ticket)