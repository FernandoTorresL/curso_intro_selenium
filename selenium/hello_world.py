import unittest

from pyunitreport import HTMLTestRunner
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Con Windows
        # cls.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')

        # Con MacOs
        # cls.driver = webdriver.Chrome(executable_path = '../../../../chromedriver/mac64_m1/v103/chromedriver')

        # With driver download automaticaly
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = cls.driver

        # Wait for 10 seconds
        driver.implicitly_wait(10)


    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')


    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
