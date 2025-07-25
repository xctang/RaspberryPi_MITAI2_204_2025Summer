from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=22, trigger=4)  # Use correct GPIOs

while True:
    try:
        print(f"Distance: {sensor.distance * 100:.1f} cm")
    except Exception as e:
        print(f"Sensor error: {e}")
    sleep(0.5)
