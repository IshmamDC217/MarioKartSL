from machine import Pin
import time

# Button names and GPIO pin numbers
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)

def blink(led, count=1, on_duration=0.5, off_duration=0.5):
    """Blink an LED a specified number of times."""
    for _ in range(count):
        led.value(1)
        time.sleep(on_duration)
        led.value(0)
        time.sleep(off_duration)

while True:
    time.sleep(0.2)  # Delay

    if button1.value() == 1 and button2.value() == 1:
        print("Buttons 1 and 2 pressed")
        blink(red, count=3, on_duration=0.5, off_duration=0.5)
        green.value(1)  # Green LED on after blinking red
        time.sleep(1)
        green.value(0)  # Green LED off after 1 second

    elif button1.value() == 1:
        print("Button 1 pressed")
        red.value(1)  # Red left on
        green.value(0)
        amber.value(0)

    else:
        # If no buttons are being pressed
        green.value(1)
        amber.value(0)
        red.value(0)

