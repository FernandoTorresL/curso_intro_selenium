import unittest

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class DynamicElements(unittest.TestCase):

    def setUp(self):
        # With driver download automaticaly
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = self.driver

        #driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element('xpath', f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i +1} is NOT FOUND")
                    tries += 1
                    driver.refresh()

        print(f"Finished in {tries} tries")

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
