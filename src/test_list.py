import unittest
from List import List
from ListItem import ListItem


class TestList(unittest.TestCase):
    def setUp(self):
        self.list = List()

    def test_init(self):
        self.assertEqual(self.list.length, 0)
        self.assertEqual(self.list.get_head(), None)
        self.assertEqual(self.list.get_tail(), None)

    def test_append(self):
        self.assertEqual(self.list.append(ListItem("0")), True)
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.get_head().get_value(), "0")
        self.assertEqual(self.list.get_tail(), None)
        self.list.append(ListItem("1"))
        self.assertEqual(self.list.length, 2)
        self.assertEqual(self.list.get_head().get_value(), "0")
        self.assertEqual(self.list.get_tail().get_value(), "1")
        self.list.append(ListItem("2"))
        self.assertEqual(self.list.length, 3)
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.get_head().get_value(), "0")
        self.assertEqual(self.list.get_tail().get_value(), "2")
        self.assertEqual(self.list.get_head().get_next().get_value(), "1")
        self.assertEqual(self.list.get_tail().get_previous().get_value(), "1")
        middle = self.list.get_head().get_next()
        self.assertEqual(middle.get_next().get_value(), "2")
        self.assertEqual(middle.get_previous().get_value(), "0")

    def test_get_items(self):
        self.assertEqual(self.list.get_items(), [])
        self.list.append(ListItem("0"))
        self.list.append(ListItem("1"))
        self.list.append(ListItem("2"))
        self.assertEqual(self.list.get_items(), ["0", "1", "2"])

    def test_get_string(self):
        self.assertEqual(self.list.get_string(), "")
        self.list.append(ListItem("0"))
        self.list.append(ListItem("1"))
        self.list.append(ListItem("2"))
        self.assertEqual(self.list.get_string(), "0, 1, 2")
