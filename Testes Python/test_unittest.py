"""
Codigo de teste disponiblilisado em Python testing in Visual  Studio Code, 
disponivel em https://code.visualstudio.com/docs/python/testing

pip install unittest
"""

import unittest  # The test framework

import inc_dec  # The code to test


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)


if __name__ == '__main__':
    unittest.main()
