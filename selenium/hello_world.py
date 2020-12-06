import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path = './../../../chromedriver_dir/87_0_4280_88/chromedriver')
        driver = self.driver

        # Wait for 10 seconds
        driver.implicitly_wait(100)


    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')


    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
