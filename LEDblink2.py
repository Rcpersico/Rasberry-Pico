from machine import Pin ,PWM
from time import sleep

max=50000

led = PWM(Pin("LED", Pin.OUT))
led.freq(1000)


while True:
    for duty in range(0,max,1000):
        led.duty_u16(duty)
        sleep(0.01)
        
    for duty in range(max, 0, -1000):
        led.duty_u16(duty)
        sleep(0.01)
    