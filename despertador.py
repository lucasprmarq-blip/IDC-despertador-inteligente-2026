import serial
import time
import datetime

PUERTO_COM = 'COM9'
HORA_MINIMA = "07:30"
HORA_MAXIMA = "08:00"
UMBRAL_MOVIMIENTO = 1.25
MODO_TEST_IGNORAR_RELOJ = True

try:
    pico = serial.Serial(PUERTO_COM, 115200, timeout=1)
    pico.flushInput()
    pico.flushOutput()
    time.sleep(2)
except:
    exit()

alarma_disparada = False

while True:
    try:
        h = datetime.datetime.now().strftime("%H:%M")
        lin = pico.readline().decode('utf-8', errors='ignore').strip()
        
        if "BOTON_PULSADO" in lin:
            alarma_disparada = True
            continue

        if ',' in lin and not alarma_disparada:
            valores = lin.split(',')
            if len(valores) == 3:
                try:
                    x, y, z = float(valores[0]), float(valores[1]), float(valores[2])
                except ValueError:
                    continue
                
                magnitud = abs(x) + abs(y) + abs(z)
                
                en_ventana = HORA_MINIMA <= h < HORA_MAXIMA
                es_limite = h >= HORA_MAXIMA
                
                if MODO_TEST_IGNORAR_RELOJ:
                    en_ventana = True
                    es_limite = False

                if en_ventana and magnitude > UMBRAL_MOVIMIENTO:
                    pico.write(b"ENCENDER_ALARMA\n")
                    alarma_disparada = True
                    
                elif es_limite:
                    pico.write(b"ENCENDER_ALARMA\n")
                    alarma_disparada = True
                    
                else:
                    print(f"Hora: {h} | Magnitud: {magnitud:.2f}", end="\r")

    except KeyboardInterrupt:
        pico.write(b"APAGAR_ALARMA\n")
        pico.close()
        break
    except:
        pass