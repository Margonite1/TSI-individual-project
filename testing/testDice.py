import unittest
from src import dice

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_die_20(self):
        result = dice.roll_die(20)
        self.assertEqual(result,20)

    def test_die_8(self):
        result = dice.roll_die(8)
        self.assertEqual(result, 8)

    def test_dice_3_20(self):
        result = dice.roll_dice(3, 20)
        self.assertEqual(result, 60)

    def test_dice20_4(self):
        result = dice.roll_dice(20, 4)
        self.assertEqual(result, 80)

if __name__ == '__main__':
    unittest.main()
