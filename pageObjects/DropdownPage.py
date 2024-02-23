from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class Dropdown():
    select_dropdown_xpath = "//select[@id='dropdown']"

    def __init__(self, driver):
        self.driver = driver

    def selectOptions_by_visable_text(self):
        options = self.driver.find_element(By.XPATH, self.select_dropdown_xpath)
        open_options = Select(options)
        open_options.select_by_visible_text('Option 1')

        time.sleep(3)
        open_options.select_by_visible_text('Option 2')

    def selectOptions_by_index_number(self):
        options = self.driver.find_element(By.XPATH, self.select_dropdown_xpath)
        open_options = Select(options)
        open_options.select_by_index(1)

        time.sleep(3)
        open_options.select_by_index(2)

    def selectOptions_by_value(self):
        options = self.driver.find_element(By.XPATH, self.select_dropdown_xpath)
        open_options = Select(options)
        open_options.select_by_value('1')

        time.sleep(3)
        open_options.select_by_value('2')


