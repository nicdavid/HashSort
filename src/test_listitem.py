import unittest
from ListItem import ListItem


class TestListItem(unittest.TestCase):
    def setUp(self):
        self.item = ListItem("0")

    def test_init(self):
        self.assertEqual(self.item.get_value(), "0")
        self.assertEqual(self.item.get_next(), None)
        self.assertEqual(self.item.get_previous(), None)
        self.assertEqual(self.item.has_next(), False)
        self.assertEqual(self.item.has_previous(), False)

    def test_add_next(self):
        self.assertEqual(self.item.set_next(ListItem("1")), True)
        self.assertEqual(self.item.get_value(), "0")
        self.assertEqual(self.item.has_next(), True)
        self.assertEqual(self.item.get_next().get_value(), "1")

    def test_add_previous(self):
        self.assertEqual(self.item.set_previous(ListItem("-1")), True)
        self.assertEqual(self.item.get_value(), "0")
        self.assertEqual(self.item.has_previous(), True)
        self.assertEqual(self.item.get_previous().get_value(), "-1")

    def test_to_string(self):
        self.assertEqual(str(self.item), "0")
