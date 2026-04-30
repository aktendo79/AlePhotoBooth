import RPi.GPIO as GPIO
import time
import os

BUTTON = 4
LED = 17

GPIO.setmode(GPIO.BCM)

# LED invertito (3.3V -> LED -> GPIO)
LED_ON = GPIO.LOW
LED_OFF = GPIO.HIGH

press_time = None
last_toggle = 0
led_state = False
last_press = 0
DEBOUNCE = 0.2


def setup_gpio():
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)


def ensure_gpio():
    try:
        GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LED, GPIO.OUT)
    except:
        pass


def blink_fast(duration=2):
    end = time.time() + duration
    while time.time() < end:
        ensure_gpio()
        GPIO.output(LED, LED_ON)
        time.sleep(0.1)
        GPIO.output(LED, LED_OFF)
        time.sleep(0.1)


setup_gpio()

try:
    while True:
        ensure_gpio()

        if GPIO.input(BUTTON) == GPIO.LOW:

            # 👉 inizio pressione (con debounce)
            if press_time is None:
                if time.time() - last_press < DEBOUNCE:
                    time.sleep(0.01)
                    continue

                last_press = time.time()
                press_time = time.time()
                last_toggle = 0
                led_state = False

            elapsed = time.time() - press_time
            now = time.time()

            # 🎯 velocità progressiva LED
            if elapsed < 3:
                interval = 1.0   # lento
            elif elapsed < 5:
                interval = 0.4   # medio
            else:
                interval = 0.15  # veloce

            # toggle LED
            if now - last_toggle >= interval:
                led_state = not led_state
                GPIO.output(LED, LED_ON if led_state else LED_OFF)
                last_toggle = now

            # 🔁 REBOOT
            if 3 <= elapsed < 5:
                print("Reboot!")
                blink_fast(2)
                os.system("sudo reboot")
                break

            # ⛔ SHUTDOWN
            elif elapsed >= 5:
                print("Shutdown!")
                blink_fast(3)
                os.system("sudo shutdown now")
                break

        else:
            # rilascio bottone
            press_time = None
            GPIO.output(LED, LED_OFF)

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
