#!/usr/bin/env python3
import RPi.GPIO as GPIO

# GPIO 27 == Pin 13
BEAM_PIN = 17

def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        print("beam unbroken")
    else:
        print("beam broken")

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

    message = input("Press enter to quit\n\n")
    GPIO.cleanup()

if __name__ == "__main__":
    main()