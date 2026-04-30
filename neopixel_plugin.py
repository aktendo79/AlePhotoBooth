import time
import board
import neopixel
import threading
import math

import pibooth
from pibooth.utils import LOGGER

hookimpl = pibooth.hookimpl

# =========================
# CONFIG
# =========================

PIXEL_PIN = board.D18
NUM_PIXELS = 24
BRIGHTNESS = 0.5

pixels = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False
)

# =========================
# GLOBAL STATE
# =========================

running_effect = None
effect_thread = None

# =========================
# UTILITY
# =========================

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# =========================
# EFFETTI
# =========================

def breathing_blue():
    while running_effect == "idle":
        for i in range(100):
            if running_effect != "idle":
                return
            brightness = (math.sin(i / 100 * math.pi) ** 2)
            pixels.fill((0, 0, int(255 * brightness)))
            pixels.show()
            time.sleep(0.02)

def knight_rider_loop():
    global running_effect

    pos = 0
    direction = 1

    while running_effect == "knight":
        pixels.fill((0, 0, 0))

        color = wheel((pos * 256 // NUM_PIXELS) & 255)

        pixels[pos] = color

        if pos - 1 >= 0:
            pixels[pos - 1] = tuple(int(c * 0.3) for c in color)
        if pos + 1 < NUM_PIXELS:
            pixels[pos + 1] = tuple(int(c * 0.3) for c in color)

        pixels.show()
        time.sleep(0.02)

        pos += direction

        if pos <= 0 or pos >= NUM_PIXELS - 1:
            direction *= -1

def shoot_sequence():
    # 🌈 gradiente 3s
    pixels.fill((0, 0, 0))
    pixels.show()

    steps = NUM_PIXELS
    delay = 3 / steps

    for i in range(steps):
        color = wheel(int((i / NUM_PIXELS) * 255))
        pixels[i] = color
        pixels.show()
        time.sleep(delay)

    # ⚡ lampeggio rapido
    for _ in range(6):
        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(0.08)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.08)

    # 💥 flash finale
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(2.0)

    pixels.fill((0, 0, 0))
    pixels.show()

def rainbow_cycle():
    while running_effect == "printing":
        for j in range(255):
            if running_effect != "printing":
                return
            for i in range(NUM_PIXELS):
                idx = (i * 256 // NUM_PIXELS) + j
                pixels[i] = wheel(idx & 255)
            pixels.show()
            time.sleep(0.02)

# =========================
# CONTROLLO THREAD
# =========================

def start_effect(name):
    global running_effect, effect_thread

    stop_effect()
    running_effect = name

    if name == "idle":
        effect_thread = threading.Thread(target=breathing_blue, daemon=True)
    elif name == "printing":
        effect_thread = threading.Thread(target=rainbow_cycle, daemon=True)
    elif name == "knight":
        effect_thread = threading.Thread(target=knight_rider_loop, daemon=True)
    else:
        return

    effect_thread.start()

def stop_effect():
    global running_effect, effect_thread

    running_effect = None

    if effect_thread and effect_thread.is_alive():
        effect_thread.join(timeout=0.3)

# =========================
# HOOK PIBOOTH
# =========================

@hookimpl
def state_wait_enter(app):
    LOGGER.warning("LED IDLE")
    start_effect("idle")

@hookimpl
def state_choose_enter(app):
    LOGGER.warning("LED KNIGHT RIDER")
    start_effect("knight")

@hookimpl
def state_capture_enter(app):
    LOGGER.warning("LED SHOOT SEQUENCE")
    stop_effect()
    shoot_sequence()

@hookimpl
def state_processing_enter(app):
    LOGGER.warning("LED PRINTING")
    start_effect("printing")

@hookimpl
def state_finish_enter(app):
    LOGGER.warning("LED FINISH")
    stop_effect()
    pixels.fill((0, 0, 0))
    pixels.show()

@hookimpl
def pibooth_cleanup(app):
    LOGGER.warning("LED CLEANUP")
    stop_effect()
    pixels.fill((0, 0, 0))
    pixels.show()
    pixels.deinit()
