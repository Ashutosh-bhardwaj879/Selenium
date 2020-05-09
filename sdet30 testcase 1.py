#python unitest framework
import unittest
class Test(unittest.TestCase):# T C inn test case should be upper
    def test_FirstTest(self):
        print("This is my first unittest case")

if __name__ == '__main__':
    unittest.main()