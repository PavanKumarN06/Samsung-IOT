
from gpiozero import LED
import psutil
led_red = LED(14)

while True:
    command = input("Enter command: ").lower()

    if command == "on":
        led_red.on()
        print("LED is ON")

    elif command == "off":
        led_red.off()
        print("LED is OFF")

    elif command == "exit":
        led_red.off()
        print("Program stopped")

    else:
        print("Invalid command! Please type on, off, or exit.")
    print(psutil.disk_partitions())
    print(psutil.disk_usage('/'))
