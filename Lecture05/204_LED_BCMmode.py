import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)

try:
    while True:
        GPIO.output(2, 1)
        time.sleep(1)
        GPIO.output(2, 0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
