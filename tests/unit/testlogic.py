import unittest

import logic.hexcheck


class TestLogic(unittest.TestCase):
    def test_positive_case(self):
        min_did = "0x0000"
        max_did = "0xffff"
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        self.assertEqual(min, 0x0000)  # add assertion here
        self.assertEqual(max, 0xffff)

    def test_not_a_hex_number_case(self):
        min_did = "0x0"
        max_did = "0xfffg"
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        self.assertIsNone(min)  # add assertion here
        self.assertIsNone(max)

    def test_too_long_hex_number(self):
        min_did = "0x00000"
        max_did = "0xfffff"
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        self.assertIsNone(min)  # add assertion here
        self.assertIsNone(max)

    def test_wrong_prefix_hex_number(self):
        min_did = "0v0"
        max_did = "0xffff"
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        print(min, max
              )
        self.assertIsNone(min)  # add assertion here
        self.assertIsNone(max)

    def test_empty_hex_number(self):
        min_did = ""
        max_did = ""
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        self.assertEqual(min, 0x0000)  # add assertion here
        self.assertEqual(max, 0xffff)

    def test_no_prefix_hex_number(self):
        min_did = "c0fe"
        max_did = "ffe0"
        min, max = logic.hexcheck.check_hex_numbers(min_did=min_did, max_did=max_did)
        self.assertEqual(min, 0xc0fe)  # add assertion here
        self.assertEqual(max, 0xffe0)


if __name__ == '__main__':
    unittest.main()
