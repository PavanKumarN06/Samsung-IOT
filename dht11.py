import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4, use_pulseio=False)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        if temperature is not None and humidity is not None:
            print("Temperature: {:.1f} C".format(temperature))
            print("Humidity: {:.1f} %".format(humidity))

    except RuntimeError as e:
        print("Reading error:", e)

    except Exception as e:
        print("Unexpected error:", repr(e))
        dht.exit()
        raise

    time.sleep(3)
