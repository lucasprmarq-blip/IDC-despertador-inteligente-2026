import time
from machine import Pin, I2C
import struct

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

LIS3DH_ADDR = 0x18

try:
    i2c.writeto_mem(LIS3DH_ADDR, 0x20, b'\x57')
    
    i2c.writeto_mem(LIS3DH_ADDR, 0x23, b'\x00')
    
    print("¡LIS3DH detectado e inicializado correctamente!")
except Exception as e:
    print("Error: No se encuentra el sensor. Revisa los cables y la dirección I2C.")
    print("Detalle del error:", e)

SCALE = 0.061 * 9.80665 / 1000.0

while True:
    try:
        data = i2c.readfrom_mem(LIS3DH_ADDR, 0xA8, 6)
        
        raw_x, raw_y, raw_z = struct.unpack('<hhh', data)
        
        x = (raw_x >> 4) * SCALE
        y = (raw_y >> 4) * SCALE
        z = (raw_z >> 4) * SCALE
        
        print(f"{x:.2f},{y:.2f},{z:.2f}")
        
    except Exception as e:
        print("Error leyendo los datos:", e)
        
    time.sleep(0.04)
