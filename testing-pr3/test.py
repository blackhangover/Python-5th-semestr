# программа для тестирования модулей

import unittest

from guesser import Guesser

class TestGuesser(unittest.TestCase):

    def setUp(self):
        self.guesser = Guesser("word")

    def test_1(self):
        self.assertEqual(self.guesser.is_geussed(), False)
        pass

    def test_2(self):
        self.guesser.open_char('w')
        self.assertEqual(self.guesser.get_opened(), 'w???')
        self.guesser.open_char('o')
        self.assertEqual(self.guesser.get_opened(), 'wo??')
        pass

    if __name__ == "__main__":
        unittest.main()
