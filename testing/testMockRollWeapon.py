import unittest
from unittest.mock import MagicMock
from data import loadchar, char_stub
from src import roll_weapon

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_roll_axe(self):
        loadchar.load = MagicMock(return_value=char_stub.load())
        result = roll_weapon.roll_damage(loadchar.load.return_value, "Axe")
        print(result)
        self.assertEqual(result, 13)

    def test_roll_firbolt(self):
        loadchar.load = MagicMock(return_value=char_stub.load())
        result = roll_weapon.roll_damage(loadchar.load.return_value, "Firebolt")
        print(result)
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()
