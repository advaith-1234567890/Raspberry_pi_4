from gpiozero import Button, LED
from time import sleep

button = Button(12)
led = LED(18)

try:
    while True:
        button.when_pressed = led.on
        button.when_released = led.off      

except KeyboardInterrupt:
    led.close()
