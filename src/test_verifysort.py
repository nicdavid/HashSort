import unittest
from VerifySort import verify_sort


class TestList(unittest.TestCase):
    def test_verify_sort(self):
        self.assertEqual(
            verify_sort(["a", "c", "d"]),
            True,
        )
        self.assertRaises(
            Exception,
            verify_sort,
            ["a", "e", "d"]
        )
        self.assertEqual(
            verify_sort([1, 2, 3]),
            True,
        )
        self.assertRaises(
            Exception,
            verify_sort,
            [1, 8, 4],
        )