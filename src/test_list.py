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

    def test_insert_sorted_head(self):
        # add to head
        self.assertEqual(self.list.insert_sorted(ListItem("c")), True)
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.get_items(), ["c"])

        # add to head
        self.list.insert_sorted(ListItem("b"))
        self.assertEqual(self.list.get_items(), ["b", "c"])

        # add to head
        self.list.insert_sorted(ListItem("a"))
        self.assertEqual(self.list.get_items(), ["a", "b", "c"])

    def test_insert_sorted_tail(self):
        # add to head
        self.assertEqual(self.list.insert_sorted(ListItem("c")), True)
        self.assertEqual(self.list.length, 1)
        self.assertEqual(self.list.get_items(), ["c"])

        # add to tail
        self.list.insert_sorted(ListItem("d"))
        self.assertEqual(self.list.get_items(), ["c", "d"])

        # add to tail
        self.list.insert_sorted(ListItem("e"))
        self.assertEqual(self.list.get_items(), ["c", "d", "e"])

    def test_insert_sorted_tail(self):
        # add items
        self.list.insert_sorted(ListItem("q"))
        self.list.insert_sorted(ListItem("g"))
        self.list.insert_sorted(ListItem("e"))
        self.list.insert_sorted(ListItem("p"))
        self.list.insert_sorted(ListItem("a"))
        self.assertEqual(self.list.get_items(), ["a", "e", "g", "p", "q"])
