import unittest
from app import greet_user, calculate_total, is_even

class TestAppFunctions(unittest. TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Joseph"),"Hello, Joseph!")
        self.assertEqual(greet_user("Jane"),"Hello, Jane!")
        
if __name__ == "__main__":
    unittest.main()
