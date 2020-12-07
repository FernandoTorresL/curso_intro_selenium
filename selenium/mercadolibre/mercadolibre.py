import unittest
from selenium import webdriver
from time import sleep


class NewClass(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path = './../../../../chromedriver_dir/87_0_4280_88/chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com/')

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()
        sleep(2)

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        sleep(2)
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(2)

        location = driver.find_element_by_partial_link_text("Bogotá D.C.")
        # Anterior
        #location.click()
        # Nuevo
        driver.execute_script("arguments[0].click();", location)
        sleep(2)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        #condition.click()
        driver.execute_script("arguments[0].click();", condition)
        sleep(2)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        sleep(2)

        higher_price = driver.find_element_by_class_name('andes-list__item-text')
        #higher_price.click()
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(2)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(article_price)

        print(articles, prices)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
