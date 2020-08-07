import time

from hc_sr04._version import __version__, __version_info__
import RPi.GPIO as GPIO


class HCSR04(object):
    def __init__(self, trigger, echo):
        self._trig_pin = trigger
        self._echo_pin = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._trig_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
        print("setting trigger pin to False to make sure it's not floating")
        GPIO.output(self._trig_pin, False)

    def measure_distance(self) -> int:
        self._pulse_trigger()
        return 0

    def _pulse_trigger(self):
        GPIO.output(self._trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self._trig_pin, False)
