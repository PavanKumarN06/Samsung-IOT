

from gpiozero import LED
from time import sleep
import requests

# ThingSpeak Configuration
WRITE_API_KEY = "BG3WGQ0TOPS3LEIL"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Define GPIO pins (BCM numbering)
red = LED(17)
amber = LED(27)
green = LED(22)

# Function to send data to ThingSpeak
def send_to_thingspeak(red_status, amber_status, green_status):
    data = {
        "api_key": WRITE_API_KEY,
        "field1": red_status,
        "field2": amber_status,
        "field3": green_status
    }

    try:
        response = requests.post(THINGSPEAK_URL, data=data, timeout=10)

        if response.status_code == 200 and response.text != "0":
            print("ThingSpeak updated successfully!")
        else:
            print("ThingSpeak update failed:", response.text)

    except requests.RequestException as e:
        print("ThingSpeak connection error:", e)


try:
    while True:

        # GREEN
        green.on()
        amber.off()
        red.off()
        print("GREEN ON")

        send_to_thingspeak(0, 0, 1)
        sleep(3)

        # AMBER
        green.off()
        amber.on()
        red.off()
        print("AMBER ON")

        send_to_thingspeak(0, 1, 0)
        sleep(3)

        # RED
        green.off()
        amber.off()
        red.on()
        print("RED ON")

        send_to_thingspeak(1, 0, 0)
        sleep(3)

        # AMBER
        green.off()
        amber.on()
        red.off()
        print("AMBER ON")

        send_to_thingspeak(0, 1, 0)
        sleep(3)

except KeyboardInterrupt:
    print("Traffic light stopped")

finally:
    green.off()
    amber.off()
    red.off()

    print("All traffic lights OFF")
