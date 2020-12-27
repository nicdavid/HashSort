import unittest
from HashTable import HashTable
from ListItem import ListItem


class TestSimpleHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(accuracy=1)

    def test_init(self):
        self.assertEqual(self.table.length, 0)
        self.assertEqual(len(self.table), 0)
        self.assertEqual(self.table.get_accuracy(), 1)

    def test_hash(self):
        self.assertEqual(self.table._hash("a"), 97)
        self.assertEqual(self.table._hash("b"), 98)
        self.assertEqual(self.table._hash("z"), 122)
        self.assertEqual(self.table._hash(" a "), 97)
        self.assertEqual(self.table._hash("A"), 97)
        self.assertEqual(self.table._hash("1"), 49)
        self.assertEqual(self.table._hash(";"), 59)

    def test_add_simple(self):
        self.assertEqual(self.table.add("a"), True)
        self.table.add("aq")
        self.table.add("saasdfasd")
        self.table.add("xasdeaasdfasdfasdf")
        self.table.add("facaasdfasdfas")
        self.table.add("fffsadfasdfasdfas")
        self.table.add("sdasdfasdfa")
        self.assertEqual(len(self.table), 7)
        self.assertEqual(self.table.add(ListItem("a")), False)
        self.assertEqual(len(self.table), 7)

    def test_add_complex(self):
        self.assertEqual(self.table.get_values(), [])
        self.table.add("a")
        self.table.add("a")
        self.table.add("b")
        self.table.add("b")
        self.table.add("d")
        self.table.add("z")
        self.table.add("zza")
        self.table.add("za")
        self.table.add("zaa")
        self.assertEqual(
            self.table.get_values(),
            [["a", "a"], ["b", "b"], ["d"], ["z", "zza", "za", "zaa"]],
        )

    def test_sort_sorted(self):
        self.table.add("a")
        self.table.add("a")
        self.table.add("b")
        self.table.add("b")
        self.table.add("d")
        self.table.add("z")
        self.table.add("za")
        self.assertEqual(self.table.sort(), True)
        self.assertEqual(
            self.table.get_values(), [["a", "a"], ["b", "b"], ["d"], ["z", "za"]]
        )

    def test_sort_unsorted(self):
        self.table.add("za")
        self.table.add("b")
        self.table.add("g")
        self.table.add("a")
        self.table.add("z")
        self.table.add("d")
        self.assertEqual(self.table.sort(), True)
        self.assertEqual(
            self.table.get_values(), [["a"], ["b"], ["d"], ["g"], ["z", "za"]]
        )

    def test_to_string(self):
        self.table.add("a")
        self.table.add("a")
        self.table.add("b")
        self.table.add("b")
        self.table.add("d")
        self.table.add("z")
        self.table.add("za")
        self.assertEqual(
            str(self.table), "[['a', 'a'], ['b', 'b'], ['d'], ['z', 'za']]"
        )


class TestLargerHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(accuracy=3)

    def test_add(self):
        self.assertEqual(self.table.get_values(), [])
        self.table.add("a")
        self.table.add("b")
        self.table.add("z")
        self.table.add("aa")
        self.table.add("ba")
        self.table.add("za")
        self.table.add("ab")
        self.table.add("ab")
        self.table.add("az")
        self.table.add("aaa")
        self.assertEqual(
            self.table.get_values(),
            [["a"], ["aa", "aaa"], ["ab", "ab"], ["az"], ["b"], ["ba"], ["z"], ["za"]],
        )

    def test_sort(self):
        self.table.add("zzz")
        self.table.add("m")
        self.table.add("zz")
        self.table.add("gg")
        self.table.add("z")
        self.table.add("zza")
        self.table.add("zzza")
        self.table.add("a")
        self.table.add("za")
        self.table.add("oml")
        self.table.add("zzzz")
        self.table.add("zzzza")
        self.table.add("veg")
        self.table.add("zzzzz")
        self.assertEqual(self.table.sort(), True)
        self.assertEqual(
            self.table.get_values(),
            [
                ["a"],
                ["gg"],
                ["m"],
                ["oml"],
                ["veg"],
                ["z"],
                ["za"],
                ["zz", "zza", "zzz", "zzza", "zzzz", "zzzza", "zzzzz"],
            ],
        )
