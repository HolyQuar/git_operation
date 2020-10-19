# uittest_module
"""
-- not as effortless as the doctest module,
--but it allows a more comprehensive set of tests to be maintained in a separate file:
"""
def average(values):
    return sum(values)/len(values)
import unittest
class TestStatisticsFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40.0)
        self.assertEqual(round(average([1,5,7]),1),4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20,30,70)
# Calling from the command line invokes all tests
unittest.main()