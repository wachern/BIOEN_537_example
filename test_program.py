from program import hello
import unittest

class TestFunctions(unittest.TestCase):

    def testHello(self):
        result = hello()
        self.assertFalse(result == 'goodbye')

    def testHello1(self):
        result = hello()
        self.assertTrue(result == 'hello')