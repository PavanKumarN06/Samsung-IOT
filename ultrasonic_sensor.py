
import RPi.GPIO as GPIO
import time

TRIG = 8
ECHO = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

time.sleep(1)

print("Testing HC-SR04 on GPIO 8 and GPIO 9")

try:
    while True:
        # Check that ECHO is LOW before triggering
        if GPIO.input(ECHO) == 1:
            print("ERROR: ECHO stuck HIGH - check wiring")
            time.sleep(1)
            continue

        GPIO.output(TRIG, False)
        time.sleep(0.05)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for ECHO to go HIGH
        timeout = time.monotonic() + 0.03
        while GPIO.input(ECHO) == 0:
            if time.monotonic() > timeout:
                print("TIMEOUT: ECHO never went HIGH")
                break
        else:
            start = time.monotonic()

            # Wait for ECHO to return LOW
            timeout = time.monotonic() + 0.03
            while GPIO.input(ECHO) == 1:
                if time.monotonic() > timeout:
                    break

            end = time.monotonic()

            if GPIO.input(ECHO) == 1:
                print("TIMEOUT: ECHO stayed HIGH")
            else:
                distance = (end - start) * 17150
                print("Distance: {:.2f} cm".format(distance))

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped")

finally:
    GPIO.cleanup()
