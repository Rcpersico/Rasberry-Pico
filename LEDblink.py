from machine import Pin
from time import sleep
led = Pin('LED', Pin.OUT)
while True:
    led.on()
    sleep(10)
    led.off()
    sleep(0.2)
    
    