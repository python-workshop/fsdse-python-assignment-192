from unittest import TestCase


class TestIs_power_of_two(TestCase):
    def test_is_power_of_two(self):
        try:
            from build import is_power_of_two
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, is_power_of_two, None)
        self.assertEqual(is_power_of_two(0), False)
        self.assertEqual(is_power_of_two(1), True)
        self.assertEqual(is_power_of_two(2), True)
        self.assertEqual(is_power_of_two(15), False)
        self.assertEqual(is_power_of_two(16), True)
