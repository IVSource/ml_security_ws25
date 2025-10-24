import unittest
from date import validate_datestring


class TestDateValidation(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(validate_datestring("2025-10-05"))

    def test_too_short(self):
        self.assertFalse(validate_datestring("a-"))  # < 8 chars

    def test_too_long(self):
        self.assertFalse(validate_datestring("4560-1235-5687"))

    def test_invalid_characters(self):
        self.assertFalse(validate_datestring(
            "bad!name"))  # letters not allowed

    def test_invalid_month(self):
        self.assertFalse(validate_datestring("2023-13-10"))  # month > 12

    def test_invalid_day(self):
        self.assertFalse(validate_datestring("2023-12-32"))  # day > 31

    def test_non_leap_year_feb_29(self):
        self.assertFalse(validate_datestring("2023-02-29")
                         )  # 2023 is not a leap year

    def test_leap_year_feb_29(self):
        self.assertTrue(validate_datestring(
            "2024-02-29"))  # 2024 is a leap year

    def test_month_day_mismatch(self):
        self.assertFalse(validate_datestring("2023-04-31")
                         )  # April has only 30 days

    def test_a_goofy_date(self):
        self.assertFalse(validate_datestring(
            "0000-00-00"))  # clearly invalid date
        self.assertFalse(validate_datestring(
            "1584-65-85"))  # clearly invalid date


if __name__ == "__main__":
    unittest.main()
