from hauki import Hauki
import unittest


class TestHauki(unittest.TestCase):

    def test_count_vowels_contains_none(self):
        self.assertEqual(Hauki.count_vowels(None), 0)

    def test_count_vowels_contains_no_vowel(self):
        self.assertEqual(Hauki.count_vowels("ths mthd cnts zr vwls"), 0)

    def test_count_vowels_contains_vowels(self):
        self.assertEqual(Hauki.count_vowels("i must not let them"), 5)

    def test_count_vowels_contains_only_vowels(self):
        self.assertEqual(Hauki.count_vowels("aeu oioioio"), 10)

    def test_count_consecutive_vowels_contains_none(self):
        self.assertEqual(Hauki.count_consecutive_vowels(None), 0)

    def test_count_consecutive_vowels_contains_no_word(self):
        self.assertEqual(Hauki.count_consecutive_vowels(""), 0)

    def test_count_consecutive_vowels_contains_no_consecutive(self):
        self.assertEqual(Hauki.count_consecutive_vowels("lowercase only"), 0)

    def test_count_consecutive_vowels_contains_dual_consecutive(self):
        self.assertEqual(Hauki.count_consecutive_vowels("contains guaranteed"), 3)

    def test_count_consecutive_vowels_contains_triple_consecutive(self):
        self.assertEqual(Hauki.count_consecutive_vowels("contayins guaranteaed"), 3)

    def test_count_consecutive_vowels_contains_quart_consecutive(self):
        self.assertEqual(Hauki.count_consecutive_vowels("contuayins guaranteaeud woauyd"), 4)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
