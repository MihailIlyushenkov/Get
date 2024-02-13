import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21,0)

print(GPIO.input(24))
GPIO.output(21,GPIO.input(24))