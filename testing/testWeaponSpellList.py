import unittest
from src import show_weapons_spells

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_wslist(self):
        result = show_weapons_spells.weapons_spell_list()
        self.assertEqual(result, ["Axe", "Greatsword", "Rapier", "Longbow",
                      "Firebolt", "Ray of Frost", "Vicious Mockery", "Heat Metal"])


if __name__ == '__main__':
    unittest.main()
