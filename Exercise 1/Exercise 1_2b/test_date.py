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
        self.assertFalse(validate_datestring("bad!name"))  # letters not allowed

    ## task: add a test case to find the bug.

if __name__ == "__main__":
    unittest.main()
