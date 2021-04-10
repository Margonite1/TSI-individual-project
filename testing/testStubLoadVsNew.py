import unittest
from src.load_new import load_or_new

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_load_new1(self):
        result = load_or_new("1")
        self.assertEqual(result, ["Zizok", {'STR': 10, 'DEX': 8, 'CON': 9, 'WIS': 13, 'INT': 16, 'CHA': 12}])

    def test_load_new2(self):
        result = load_or_new("2")
        self.assertEqual(result, ["Samson", {'STR': 18, 'DEX': 18, 'CON': 18, 'WIS': 18, 'INT': 18, 'CHA': 18}])

if __name__ == '__main__':
    unittest.main()
