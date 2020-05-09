#Python unittest
#setUp- execute before each test methods
#tearDown- execute after completion each test method
#setUpClass-one time before starting
#tearDownClass - one time after starting
#setUpModule - created before class ,runs before everything oncde
#tearDownModule - created before class,run omnce after everything
import unittest
from selenium import webdriver
import time
def setUpModule():
    print("setupmodule")
def tearDownModule():
    print("teardownmodule")
class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("OPEN APP")
    @classmethod
    def tearDownClass(cls):
        print("CLOSE APP")
    @classmethod
    def setUp(self):
        print("This is login test")
        #print("This is login test")
    @classmethod
    def tearDown(self):
        print("this is logout method")
    def test_search(self):
        print("this is for search")
    """@classmethod
    def setUp(self):
        print("This is login test")"""
    def test_advancesearch(self):
        print("This is advance search")
    def test_prepaid(self):
        print("This is prepaid")
    def test_postpaid(self):
        print("this is postpaid")
    """@classmethod
    def tearDown(self):
        print("this is logout method")"""
if __name__ == "__main__":
    unittest.main()