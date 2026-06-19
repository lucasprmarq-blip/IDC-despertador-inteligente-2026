Aquí tienes el contenido adaptado a texto completamente plano y limpio, listo para que lo pegues:

Despertador Inteligente IoT para Sueño Ligero

Este proyecto de Internet de las Cosas utiliza una Raspberry Pi Pico, un acelerómetro y un buzzer para diseñar un despertador inteligente capaz de despertarte exclusivamente durante tu fase de sueño ligero, garantizando que empieces el día mucho más descansado.

Como funciona

El dispositivo monitoriza en tiempo real los movimientos del usuario en la cama. El sistema está estructurado en una arquitectura dividida que se comunica de forma bidireccional mediante puerto serie por cable USB.

Por un lado, el hardware con el archivo main.py en la Pico lee constantemente los datos del acelerómetro por protocolo I2C y los envía al ordenador. Si se activa la alarma, hace sonar un buzzer de forma intermitente. Cuenta con un sistema de seguridad nativo donde la alarma solo se apaga presionando físicamente el botón integrado de la propia placa.

Por otro lado, el software con el archivo despertador.py en el ordenador recibe los datos, calcula la magnitud total del movimiento sumando sus tres ejes espaciales y controla la ventana horaria. Si el usuario se mueve dentro del tramo configurado, por ejemplo de las 7:30 a las 8:00, el script detecta que está en fase de sueño ligero y ordena el disparo inmediato a la placa.

Requisitos y Componentes

Para el hardware se necesita una Raspberry Pi Pico, un sensor acelerómetro con conexión I2C, un buzzer pasivo y un cable de conexión USB a Micro-USB. Los pines utilizados por defecto son el pin GPIO 16 para el buzzer, los pines GPIO 4 y GPIO 5 para las líneas SDA y SCL del acelerómetro, y el pin interno 23 para el botón integrado de la placa.

Para el software, el script del ordenador requiere tener instalado Python 3 y la librería externa pyserial.

Instrucciones de Uso

Primero debes cargar el firmware guardando el código de main.py dentro de la memoria de la Raspberry Pi Pico utilizando un editor como Thonny.

Después, abre el archivo despertador.py en tu ordenador y modifica la variable PUERTO_COM con el puerto que tenga asignado tu placa, como COM9 en Windows o /dev/ttyACM0 en Linux.

Finalmente, deja la Pico conectada por USB al ordenador y ejecuta el script despertador.py desde la terminal de tu sistema operativo.

Limitaciones Técnicas y Retos Resueltos

Durante el desarrollo del proyecto surgieron varias limitaciones que obligaron a reestructurar el diseño inicial.

El diseño original contemplaba un modelo de inteligencia artificial entrenado en Edge Impulse para analizar el sueño. Debido a problemas de compatibilidad para instalar dicha librería en el entorno de Python local, se sustituyó el modelo por un algoritmo basado en la magnitud geométrica pura de los tres ejes, logrando la misma precisión con un código mucho más ligero.

Además, como la Raspberry Pi Pico no puede mantener la hora por sí misma al desconectarse de la corriente, se delegó el control del reloj al script del ordenador, utilizando la hora del sistema operativo para validar las ventanas de sueño de forma externa.
