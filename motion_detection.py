from gpiozero import MotionSensor
import requests
import time

# ThingSpeak Configuration
WRITE_API_KEY = "VASZM348KNK8FI5K"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# PIR Sensor connected to GPIO 15
pir = MotionSensor(15)

print("Waiting for PIR sensor to settle...")
time.sleep(2)

print("Motion Detection System Started")

last_status = None

while True:
    try:
        if pir.motion_detected:
            status = 1
            print("Motion Detected!")

        else:
            status = 0
            print("No Motion Detected")

        # Upload only when status changes
        if status != last_status:

            params = {
                "api_key": WRITE_API_KEY,
                "field1": status
            }

            response = requests.get(
                THINGSPEAK_URL,
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                print("Data uploaded successfully!")
                print("ThingSpeak Entry ID:", response.text)

                last_status = status

            else:
                print("Upload Failed:", response.status_code)

        time.sleep(15)

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        time.sleep(15)

    except KeyboardInterrupt:
        print("Program Stopped")
        break
