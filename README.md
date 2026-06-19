# Despertador Inteligente IoT para Sueño Ligero

Este proyecto de Internet de las Cosas (IoT) utiliza una **Raspberry Pi Pico**, un acelerómetro y un buzzer para diseñar un despertador inteligente capaz de despertarte exclusivamente durante tu fase de **sueño ligero**, garantizando que empieces el día mucho más descansado.

---

## ¿Cómo funciona?

El dispositivo monitoriza en tiempo real los movimientos del usuario en la cama. El sistema está estructurado en una arquitectura dividida que se comunica de forma bidireccional mediante puerto serie (USB):

* **Hardware (`main.py` en la Pico):** Lee constantemente los datos del acelerómetro por I2C y los envía al ordenador. Si se activa la alarma, hace sonar un buzzer de forma intermitente. Cuenta con un sistema de seguridad nativo: la alarma solo se apaga presionando físicamente el botón integrado de la placa Pico.
* **Software (`despertador.py` en el Ordenador):** Un script en Python recibe los datos, calcula la magnitud total del movimiento sumando sus tres ejes espaciales y controla la ventana horaria. Si el usuario se mueve dentro del tramo configurado (ej. 07:30 a 08:00), el script detecta que está en fase de sueño ligero y ordena el disparo inmediato a la placa.

---

## Requisitos y Componentes

### Hardware
* Raspberry Pi Pico (o Pico W)
* Sensor Acelerómetro (Conexión I2C)
* Buzzer Pasivo
* Cable de conexión USB a Micro-USB

### Conexiones de Pines (Configuración por defecto)
* **Buzzer:** Pin GPIO 16
* **Acelerómetro I2C:** SDA (Pin GPIO 4) | SCL (Pin GPIO 5)
* **Botón de apagado:** Pin interno 23 (Botón integrado de la Pico)

### Software e Instala de Dependencias
El script del ordenador requiere **Python 3** y la librería `pyserial`. Puedes instalarla ejecutando:
```bash
pip install pyserial
