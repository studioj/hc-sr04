import unittest
from unittest.mock import patch, call

# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
sys.modules["smbus"] = fake_rpi.smbus  # Fake smbus (I2C)

from hc_sr04 import HCSR04


class TestBasics(unittest.TestCase):
    def test_by_default_bcm_pins_are_selected(self):
        trigger = 24
        echo = 18
        with patch("hc_sr04.GPIO") as mocked_gpio:
            HCSR04(trigger, echo)
            mocked_gpio.setmode.assert_any_call(mocked_gpio.BCM)

    def test_needs_a_trigger_and_an_echo_pin(self):
        trigger = 24
        echo = 18
        sensor = HCSR04(trigger, echo)

        self.assertIs(trigger, sensor._trig_pin)
        self.assertIs(echo, sensor._echo_pin)

    def test_the_trigger_pin_is_defined_as_an_output(self):
        # Given
        trigger = 24
        echo = 18
        # When
        with patch("hc_sr04.GPIO") as mocked_gpio:
            HCSR04(trigger, echo)
            mocked_gpio.setup.assert_any_call(trigger, mocked_gpio.OUT)

    def test_the_echo_pin_is_defined_as_an_input(self):
        # Given
        trigger = 24
        echo = 18
        # When
        with patch("hc_sr04.GPIO") as mocked_gpio:
            HCSR04(trigger, echo)
            mocked_gpio.setup.assert_any_call(echo, mocked_gpio.IN)
