from hauki import Hiker
import unittest


class TestHiker(unittest.TestCase):
    hiker = Hiker()

    def test_count_vowels_contains_none(self):
        self.assertEqual(self.hiker.count_vowels(None), 0)

    def test_count_vowels_contains_no_vowel(self):
        self.assertEqual(self.hiker.count_vowels("ths mthd cnts zr vwls"), 0)

    def test_count_vowels_contains_vowels(self):
        self.assertEqual(self.hiker.count_vowels("i must not let them"), 5)

    def test_count_vowels_contains_only_vowels(self):
        self.assertEqual(self.hiker.count_vowels("aeu oioioio"), 10)

    def test_count_consecutive_vowels_contains_none(self):
        self.assertEqual(self.hiker.count_consecutive_vowels(None), 0)

    def test_count_consecutive_vowels_contains_no_word(self):
        self.assertEqual(self.hiker.count_consecutive_vowels(""), 0)

    def test_count_consecutive_vowels_contains_no_consecutive(self):
        self.assertEqual(self.hiker.count_consecutive_vowels("lowercase only"), 0)

    def test_count_consecutive_vowels_contains_dual_consecutive(self):
        self.assertEqual(self.hiker.count_consecutive_vowels("contains guaranteed"), 3)

    def test_count_consecutive_vowels_contains_triple_consecutive(self):
        self.assertEqual(self.hiker.count_consecutive_vowels("contayins guaranteaed"), 3)

    def test_count_consecutive_vowels_contains_quart_consecutive(self):
        self.assertEqual(self.hiker.count_consecutive_vowels("contuayins guaranteaeud woauyd"), 4)

    def test_main_method_for_one_line(self):
        result = self.hiker.answer("inputFile.txt")
        second = [5, 7, 5, 'Yes']
        self.assertListEqual(result, second)


if __name__ == '__main__':
    unittest.main()
