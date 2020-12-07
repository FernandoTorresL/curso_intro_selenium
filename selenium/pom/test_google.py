import unittest
from selenium import webdriver
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # self.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')
        cls.driver = webdriver.Chrome(executable_path = './../../../../chromedriver_dir/87_0_4280_88/chromedriver')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
