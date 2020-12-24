import structural
import random
import unittest
from unittest.mock import patch


class Test(unittest.TestCase):
    @patch('structural.RealVideo.real_downloading', return_value=random.randrange(10000, 99999))
    def test_real_downloading(self, real_downloading):
        structural.main()


if __name__ == "__main__":
    unittest.main()
