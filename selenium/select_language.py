import unittest

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        # With driver download automaticaly
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = self.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        #driver.get('http://demo.onestepcheckout.com/')
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        driver = self.driver

        exp_options = ['English', 'French', 'German']
        act_options = []
        driver.implicitly_wait(3)

        select_language = Select(driver.find_element('id','select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in driver.current_url)

        select_language = Select(driver.find_element('id','select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
