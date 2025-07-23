import pygame
from gpiozero import Button

pygame.init()

#
Noise =  pygame.mixer.Sound("/home/pi/GPIO-Music-Box/samples/DigitalAlarm.wav")

btn_Noise = Button(2)

#def hello():
#    print('hello')
    
btn_Noise.when_pressed = Noise.play
