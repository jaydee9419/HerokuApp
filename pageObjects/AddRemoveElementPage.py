from selenium.webdriver.common.by import By


class AddRemoveElement():
    btn_add_xpath = "//button[normalize-space()='Add Element']"
    btn_remove_xpath = "//button[normalize-space()='Delete'][1]"

    def __init__(self, driver):
        self.driver = driver

    def clickAddButton(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def clickRemoveButton(self):
        self.driver.find_element(By.XPATH, self.btn_remove_xpath).click()
