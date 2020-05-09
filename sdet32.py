#python unittest framework
#skipping test
#skip test 
#SKIP TEST based on condition
#skip test with reason output s shows the test case is skipped
import unittest
class Apptesting(unittest.TestCase):
    @unittest.SkipTest#will skip search
    def test_search(self):
        print("This is search")
    @unittest.skip("I am skipping this test")#skip with reason
    def test_advancedsearch(self):
        print("This is advanced search")
    @unittest.skipIf(1==1,"ERROR MESSAGE")
    def test_prepaidrecharge(self):
        print("This is prepaid search")
    def test_postpaidrechare(self):
        print("this is postpaid recharge")
    def test_loginbygmail(self):
        print("this is gmail")
    def test_loginbytwitter(self):
        print("this is twitter")
if __name__ == "__main__":
    unittest.main()
    










