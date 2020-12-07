import unittest
from selenium import webdriver
from time import sleep


class NavigationTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path = './../../../chromedriver_dir/87_0_4280_88/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
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
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
