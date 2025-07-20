from gpiozero import Button
from time import sleep

button = Button(12)

try:
    while True:
        print(button.value)
        sleep(0.5)
        

except KeyboardInterrupt:
    led.close()
