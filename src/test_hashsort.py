import unittest
from HashSort import HashSort


class TestSimpleHashSort(unittest.TestCase):
    def setUp(self):
        self.table = HashSort(accuracy=2)

    def test_init(self):
        self.assertEqual(len(self.table), 0)

    def test_hash(self):
        self.assertEqual(self.table._hash("0"), 37)
        self.assertEqual(self.table._hash("1"), 74)
        self.assertEqual(self.table._hash("9"), 370)
        self.assertEqual(self.table._hash("a"), 407)
        self.assertEqual(self.table._hash("aa"), 418)
        self.assertEqual(self.table._hash("ab"), 419)
        self.assertEqual(self.table._hash("b"), 444)
        self.assertEqual(self.table._hash("ba"), 455)
        self.assertEqual(self.table._hash("bb"), 456)
        self.assertEqual(self.table._hash(""), 0)
        self.assertEqual(self.table._hash("aaa"), 418)
        self.assertEqual(self.table._hash("bbb"), 456)

    def test_add(self):
        self.assertEqual(self.table.add("a"), True)
        self.assertEqual(self.table.add("b"), True)
        self.assertEqual(self.table.add("c"), True)
        self.assertEqual(len(self.table), 3)

    def test_get_values(self):
        self.table.add("aa")
        self.table.add("a")
        self.table.add("ba")
        self.table.add("ab")
        self.table.add("bb")
        self.table.add("b")
        self.assertEqual(len(self.table), 6)
        self.assertEqual(self.table.get_values(), ["a", "aa", "ab", "b", "ba", "bb"])

    def test_sorted(self):
        self.table.add("a")
        self.table.add("a")
        self.table.add("b")
        self.table.add("b")
        self.table.add("d")
        self.table.add("z")
        self.table.add("za")
        self.assertEqual(self.table.get_values(), ["a", "a", "b", "b", "d", "z", "za"])


    def test_unsorted(self):
        self.table.add("za")
        self.table.add("b")
        self.table.add("g")
        self.table.add("a")
        self.table.add("z")
        self.table.add("d")
        self.assertEqual(self.table.get_values(), ["a", "b", "d", "g", "z", "za"])


class TestLargerHashSort(unittest.TestCase):
    def setUp(self):
        self.table = HashSort(accuracy=5)

    def test_sorting1(self):
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
            ["a", "aa", "aaa", "ab", "ab", "az", "b", "ba", "z", "za"],
        )

    def test_sorting2(self):
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
        self.assertEqual(
            self.table.get_values(),
            [
                "a",
                "gg",
                "m",
                "oml",
                "veg",
                "z",
                "za",
                "zz",
                "zza",
                "zzz",
                "zzza",
                "zzzz",
                "zzzza",
                "zzzzz",
            ],
        )
