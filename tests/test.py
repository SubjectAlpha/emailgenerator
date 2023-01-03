import unittest
from emailgenerator import main

class TestEmailGenerator(unittest.TestCase):
    def test_file_create_works(self):
        self.assertEqual(1, main(test_flag_create=True))
    
    def test_email_distribution_works(self):
        self.assertEqual(1, main(test_flag_distribute=True))

if __name__ == "__main__":
    unittest.main()
