import unittest

from pyunitreport import HTMLTestRunner
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Con Windows
        # cls.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')

        # Con MacOs
        # cls.driver = webdriver.Chrome(executable_path = '../../../../chromedriver/mac64_m1/v103/chromedriver')

        # With driver download automaticaly
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = cls.driver
        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

        # Wait for 15 seconds
        driver.implicitly_wait(15)


    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, 'search')


    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element('name', 'q')


    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element('class name', 'input-text')


    def test_search_button_enabled(self):
        button = self.driver.find_element('class name', 'button')


    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element('class name', 'promos')
        banners = banner_list.find_elements('tag name', 'img')
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_elements('xpath','//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element('css selector', 'div.header-minicart span.icon')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    #unittest.main(verbosity = 2)
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Ecomerce_report'))
