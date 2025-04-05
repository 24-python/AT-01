import unittest
#from main import add, subtract, multiply, divide
#from main import check


# class TestMath(unittest.TestCase):
#
#     def test_check(self):
#         self.assertTrue(check(10))
#         self.assertTrue(check(6))
#         self.assertTrue(check(12))
#         self.assertFalse(check(11))
#         self.assertTrue(check(16))
#         self.assertTrue(check(20))

#class TestMath(unittest.TestCase):

    # def test_add(self):
    #     self.assertEqual(add(10, 5), 15)
    #     self.assertNotEqual(add(10, 5), 5)
    #
    # def test_subtract(self):
    #     self.assertEqual(subtract(10, 5), 5)
    #     self.assertNotEqual(subtract(10, 5), 3)
    #
    # def test_multiply(self):
    #     self.assertEqual(multiply(10, 5), 50)
    #     self.assertNotEqual(multiply(10, 5), 100)
    #
    # def test_divide(self):
    #     self.assertEqual(divide(10, 5), 2)
    #     self.assertNotEqual(divide(10, 5), 4)

from main import divide
class TestMath(unittest.TestCase):

    def test_divide_sussess(self):
        self.assertEqual(divide(10, 5), 0)
        self.assertEqual(divide(6, 5), 1)
        self.assertEqual(not divide(70, 65), 0)

    def test_divide_fail(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)


if __name__ == '__main__':
    unittest.main()