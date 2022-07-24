import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SearchTests(unittest.TestCase):

    def setUp(self):

        # With driver download automaticaly
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = self.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = self.driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = self.driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements('xpath','//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
