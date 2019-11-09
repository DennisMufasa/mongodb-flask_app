# third-party import
import unittest

# local import
from ..api.v1.models.utils import password_checker

class Test_Password_checker(unittest.TestCase):
    def test_password_len(self):
        password_check1 = password_checker('boo')
        password_check2 = password_checker('lysergicaciddyethylammide')
        self.assertEqual(password_check1, 'password too short')
        self.assertEqual(password_check2, 'password too long')


if __name__ == "__main__":
    unittest.main()
