import unittest
from data import loadchar

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_LoadZug(self):
        result = loadchar.load("Zug")
        self.assertEqual(result, ['Zug', {'CHA': 10, 'CON': 9, 'DEX': 8, 'INT': 12, 'STR': 12, 'WIS': 13}])

    def test_LoadSamson(self):
        result = loadchar.load("Samson")
        self.assertEqual(result, ['Samson', {'STR': 10, 'DEX': 18, 'CON': 9, 'WIS': 13, 'INT': 16, 'CHA': 12}])

    def test_LoadPanic(self):
        result = loadchar.load("Panic")
        self.assertEqual(result, ['Panic', {'STR': 10, 'DEX': 15, 'CON':14, 'WIS': 13, 'INT': 10, 'CHA': 18}])

    def test_Loadtest(self):
        result = loadchar.load("Test")
        self.assertEqual(result, ['Test', {'CHA': 'test', 'CON': 'test', 'DEX': 'test', 'INT': 'test', 'STR': 'test', 'WIS': 'test'}])

if __name__ == '__main__':
    unittest.main()
