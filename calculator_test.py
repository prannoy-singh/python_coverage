from calculator import add, multiply
from unittest import TestCase

class RunTests(TestCase):
    def test_add(self):
        self.assertEqual(add(5,5), 10)

    def test_multiply(self):
        self.assertEqual(multiply(5,5), 25)