import unittest
from employee import Employee

class test_employee_class(unittest.TestCase):
    """for testing of the Employee class in 'employee.py'"""

    def setUp(self):
        """create a new employee"""
        self.CEO = Employee('Robert','Brown',57000)


    def test_give_default_raise(self):
        """Test for giving a default raise"""
        test = self.CEO.give_raise()
        self.assertEqual(test,62000)

    def test_give_custom_raise(self):
        """Test for giving a raise other than the default"""
        test = self.CEO.give_raise(10000)
        self.assertEqual(test,67000)

