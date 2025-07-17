# this is a simple LED control program
from gpiozero import LED
from time import sleep

led = LED(2)

while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
