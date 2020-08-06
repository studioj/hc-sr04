from hc_sr04._version import __version__, __version_info__
import RPi.GPIO as GPIO


class HCSR04(object):
    def __init__(self, trigger, echo):
        self._trig_pin = trigger
        self._echo_pin = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._trig_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
