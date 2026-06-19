import machine
import time
import sys
import select

buzzer_pwm = machine.PWM(machine.Pin(16))
buzzer_pwm.freq(1000)
buzzer_pwm.duty_u16(0)

boton_pico = machine.Pin(23, machine.Pin.IN)

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))
try:
    i2c.writeto_mem(0x18, 0x20, b'\x57')
except:
    pass

alarma_activa = False
timer_intermitencia = time.ticks_ms()
estado_sonido = False

while True:
    try:
        data = i2c.readfrom_mem(0x18, 0x28 | 0x80, 6)
        x = int.from_bytes(data[0:2], 'little', signed=True) / 16384.0
        y = int.from_bytes(data[2:4], 'little', signed=True) / 16384.0
        z = int.from_bytes(data[4:6], 'little', signed=True) / 16384.0
    except:
        x, y, z = 0.0, 0.0, 0.0

    print(f"{x:.2f},{y:.2f},{z:.2f}")

    if boton_pico.value() == 1 and alarma_activa:
        alarma_activa = False
        buzzer_pwm.duty_u16(0)
        print("BOTON_PULSADO")

    if sys.stdin in [sys.stdin]:
        if select.select([sys.stdin], [], [], 0)[0]:
            comando = sys.stdin.readline().strip()
            if comando == "ENCENDER_ALARMA":
                alarma_activa = True
            elif comando == "APAGAR_ALARMA":
                alarma_activa = False
                buzzer_pwm.duty_u16(0)

    if alarma_activa:
        if time.ticks_diff(time.ticks_ms(), timer_intermitencia) > 500:
            estado_sonido = not estado_sonido
            buzzer_pwm.duty_u16(1000 if estado_sonido else 0)
            timer_intermitencia = time.ticks_ms()

    time.sleep(0.05)