import unittest
from unittest.mock import patch, call

# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO

from hc_sr04 import HCSR04


class TestDistanceMeasuring(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.gpio_patcher = patch("hc_sr04.GPIO")
        cls.gpio_mock = cls.gpio_patcher.start()

    def setUp(self) -> None:
        self.gpio_mock.reset_mock()

    def test_measure_distance_returns_an_int(self):
        # Given
        trigger = 24
        echo = 18
        sensor = HCSR04(trigger, echo)
        # When
        distance = sensor.measure_distance()
        # Then
        self.assertIsInstance(distance, int)

    def test_measure_distance_puts_a_pulse_on_the_trigger_pin(self):
        # Given
        trigger = 24
        echo = 18
        sensor = HCSR04(trigger, echo)
        # When
        sensor.measure_distance()
        # Then
        expected_calls = [call(trigger, True), call(trigger, False)]
        self.gpio_mock.output.assert_has_calls(expected_calls)


if __name__ == "__main__":
    unittest.main()
