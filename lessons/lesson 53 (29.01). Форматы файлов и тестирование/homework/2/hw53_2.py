import unittest


def count_vowels(string: str):
    vowels = 'aeiou'
    count = 0
    for letter in string.lower():
        if letter in vowels:
            count += 1
    return count

class TestFunction(unittest.TestCase):
    def TestDiffTypes(self):
        self.assertEqual(count_vowels('asddaf123'), 2)

    def TestEmpty(self):
        self.assertEqual(count_vowels(""), 0)

    def TestNoVowels(self):
        self.assertEqual(count_vowels("rbnf"), 0)

if __name__ == "__main__":
    unittest.main()

