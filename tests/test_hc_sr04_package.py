import unittest
from unittest.mock import patch, call

# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO

from hc_sr04 import HCSR04


class TestBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.gpio_patcher = patch("hc_sr04.GPIO")
        cls.gpio_mock = cls.gpio_patcher.start()

    def setUp(self) -> None:
        self.gpio_mock.reset_mock()

    def test_by_default_bcm_pins_are_selected(self) -> None:
        # Given
        trigger = 24
        echo = 18
        # When
        HCSR04(trigger, echo)
        # Then
        self.gpio_mock.setmode.assert_any_call(self.gpio_mock.BCM)

    def test_needs_a_trigger_and_an_echo_pin(self) -> None:
        trigger = 24
        echo = 18
        sensor = HCSR04(trigger, echo)

        self.assertIs(trigger, sensor._trig_pin)
        self.assertIs(echo, sensor._echo_pin)

    def test_the_trigger_pin_is_defined_as_an_output(self) -> None:
        # Given
        trigger = 24
        echo = 18
        # When
        HCSR04(trigger, echo)
        self.gpio_mock.setup.assert_any_call(trigger, self.gpio_mock.OUT)

    def test_the_echo_pin_is_defined_as_an_input(self) -> None:
        # Given
        trigger = 24
        echo = 18
        # When
        HCSR04(trigger, echo)
        self.gpio_mock.setup.assert_any_call(echo, self.gpio_mock.IN)

    def test_the_trigger_pin_is_set_to_false_to_prevent_floating_value(self) -> None:
        # Given
        trigger = 24
        echo = 18
        # When
        HCSR04(trigger, echo)
        self.gpio_mock.output.assert_any_call(trigger, False)


if __name__ == "__main__":
    unittest.main()
