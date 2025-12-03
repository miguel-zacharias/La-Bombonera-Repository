
# -------------------------------------------
# ACESSE O WOKWI ONLINE AQUI - https://wokwi.com/projects/449317234326711297
# -------------------------------------------


from machine import Pin, PWM
from utime import sleep, ticks_us, ticks_diff, ticks_ms
from picozero import Speaker

# -----------------------------
# CONFIGURAÇÃO DE HARDWARE
# -----------------------------
trig = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
buzzer = Speaker(16)

servo = PWM(Pin(15))
servo.freq(50)

# -----------------------------
# FUNÇÃO PARA MEDIR DISTÂNCIA
# -----------------------------
def medir_distancia():
    trig.low()
    sleep(0.002)

    trig.high()
    sleep(0.00001)
    trig.low()

    while echo.value() == 0:
        start = ticks_us()

    while echo.value() == 1:
        end = ticks_us()

    duracao = ticks_diff(end, start)
    distancia = (duracao * 0.0343) / 2
    return distancia


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
tempo_cheio = None
motor_rodando = False   # controla o loop contínuo do motor

while True:
    distancia = medir_distancia()
    print(f"Distância: {distancia:.1f} cm")

    # -------------------------------------------
    # SE < 50 CM → CONTAR 3s PARA CONFIRMAR "CHEIO"
    # -------------------------------------------
    if distancia < 50:
        if tempo_cheio is None:
            tempo_cheio = ticks_ms()

        if ticks_diff(ticks_ms(), tempo_cheio) >= 3000:
            print("📦 BAÚ CHEIO — MOTOR RODANDO")

            # Som de alerta
            buzzer.on()
            sleep(0.1)
            buzzer.off()

            motor_rodando = True
        else:
            print("Objeto detectado, verificando 3 segundos...")

    # -------------------------------------------
    # SE ≥ 50 CM → BAÚ VAZIO
    # -------------------------------------------
    else:
        tempo_cheio = None
        motor_rodando = False
        print("Baú vazio — motor parado")
        buzzer.off()
        servo.duty_ns(1500000)  # posição neutra
        sleep(0.2)


    # -------------------------------------------
    # MOTOR RODANDO CONTINUAMENTE (SEM PARAR)
    # -------------------------------------------
    if motor_rodando:
        # servo alternando de 0 para 180 sem parar
        servo.duty_ns(1000000)   # posição 0
        sleep(1)

        servo.duty_ns(2000000)   # posição 180
        sleep(1)

