import serial
import time

PUERTO = 'COM9'
VELOCIDAD = 115200

ARCHIVO_SALIDA = 'calma.csv' # o movimiento después

print(f"Conectando al puerto {PUERTO}...")
try:
    ser = serial.Serial(PUERTO, VELOCIDAD, timeout=1)
    time.sleep(2)
    print("¡Conectado con éxito!")
except Exception as e:
    print(f"Error al conectar: {e}")
    exit()

print(f"Grabando en '{ARCHIVO_SALIDA}'... Presiona Ctrl+C en la consola para parar.")

with open(ARCHIVO_SALIDA, 'w') as f:
    f.write("x,y,z\n") # Cabecera para Edge Impulse
    try:
        while True:
            if ser.in_waiting > 0:
                linea = ser.readline().decode('utf-8', errors='ignore').strip()
                if len(linea.split(',')) == 3:
                    print(linea)
                    f.write(linea + '\n')
    except KeyboardInterrupt:
        print(f"\nGrabación finalizada. Archivo '{ARCHIVO_SALIDA}' guardado.")
    finally:
        ser.close()
