import unittest
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = self.driver

        driver.implicitly_wait(30)
        driver.maximize_window()

        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('platzi')
        search_field.submit()

        sleep(3)
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
