import unittest
import random
import functools
from QuickSort import quick_sort
from List import List
from ListItem import ListItem


class TestList(unittest.TestCase):
    def setUp(self):
        self.int_list = List()
        self.int_list.append(ListItem(0))
        self.int_list.append(ListItem(15))
        self.int_list.append(ListItem(3))
        self.int_list.append(ListItem(212))
        self.int_list.append(ListItem(2))
        self.int_list.append(ListItem(9))
        self.int_list.append(ListItem(8))
        self.int_list.append(ListItem(60))
        self.int_list.append(ListItem(300))
        self.int_list.append(ListItem(0))

        self.str_list = List()
        self.str_list.append(ListItem("a"))
        self.str_list.append(ListItem("c"))
        self.str_list.append(ListItem("v"))
        self.str_list.append(ListItem("b"))
        self.str_list.append(ListItem("q"))
        self.str_list.append(ListItem("a"))
        self.str_list.append(ListItem("z"))
        self.str_list.append(ListItem("e"))
        self.str_list.append(ListItem("g"))
        self.str_list.append(ListItem("p"))

    def test_quick_sort_int(self):
        self.assertEqual(
            quick_sort(self.int_list.get_items(), 0, len(self.int_list) - 1),
            [0, 0, 2, 3, 8, 9, 15, 60, 212, 300],
        )

    def test_quick_sort_str(self):
        self.assertEqual(
            quick_sort(self.str_list.get_items(), 0, len(self.str_list) - 1),
            ["a", "a", "b", "c", "e", "g", "p", "q", "v", "z"],
        )

    def test_quick_sort_list(self):
        self.assertRaises(
            Exception,
            quick_sort,
            List(),
            0,
            len(self.str_list) - 1,
        )
