import unittest
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        # With driver download automaticaly
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver = self.driver

        driver.implicitly_wait(30)
        driver.maximize_window()

        #driver.get('http://demo.onestepcheckout.com/')
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element('xpath', '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element('xpath', '//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements than existent")
                break
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")

        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'searchtest2_report'))
