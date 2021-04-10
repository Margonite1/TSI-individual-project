import unittest
from src import select_stat

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_All_Stats(self):
        result = select_stat.all_stats([18,18,18,18,18,18] ,{"STR":0, "DEX":0, "CON":0, "WIS":0, "INT":0,"CHA":0})
        self.assertEqual(result, {'CHA': 18, 'CON': 18, 'DEX': 18, 'INT': 18, 'STR': 18, 'WIS': 18})

    def test_All_Stats2(self):
        result = select_stat.all_stats([] ,{"STR":18, "DEX":18, "CON":18, "WIS":18, "INT":18,"CHA":18})
        self.assertEqual(result, {'CHA': 18, 'CON': 18, 'DEX': 18, 'INT': 18, 'STR': 18, 'WIS': 18})

    def test_select_stats(self):
        result = select_stat.select_stats([18,"end"],{"STR": 0},["STR"])
        self.assertEqual(result,{"STR": 18})

    def test_pick_stat(self):
        result = select_stat.pick_stat(["STR"])
        self.assertEqual(result,"STR")

    def test_pick_number(self):
        result = select_stat.pick_number([18,"end"])
        self.assertEqual(result, 18)


if __name__ == '__main__':
    unittest.main()
