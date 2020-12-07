import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path = r'C://selenium/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path = './../../../chromedriver_dir/87_0_4280_88/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middlename = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        #veremos si los elementos están habilitados
        self.assertTrue(first_name.is_enabled()
        and middlename.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        #mandamos los datos al formulario
        first_name.send_keys('Test')
        middlename.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('arqcftlothxuknlxkt@awdrt.com') #sacado de 10-minute mail
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
