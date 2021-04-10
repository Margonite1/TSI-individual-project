import unittest
from src import char_stat_roll

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_stat_roller(self):
        result = char_stat_roll.stat_roller()
        self.assertEqual(result, [18,18,18,18,18,18])


if __name__ == '__main__':
    unittest.main()
