from gpiozero import Servo
from time import sleep

servo = Servo(14)

try:
    while True:
        servo.min()
        print("Servo at 0 degrees")
        sleep(2)

        servo.mid()
        print("Servo at 90 degrees")
        sleep(2)

        servo.max()
        print("Servo at 180 degrees")
        sleep(2)

except KeyboardInterrupt:
    servo.close()
