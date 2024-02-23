from selenium.webdriver.common.by import By

class Checkbox():
    cbx_checkboxitems_xpath= "//div//form//input"

    def __init__(self, driver):
        self.driver = driver

    def clearAllSelectedCheckboxs(self):
        selected_box = self.driver.find_elements(By.XPATH, self.cbx_checkboxitems_xpath)
        for item in selected_box:
            if item.is_selected():
                item.click()

    def selectAllCheckboxs(self):
        selected_box = self.driver.find_elements(By.XPATH, self.cbx_checkboxitems_xpath)
        for item in selected_box:
            item.click()

    def selectFirstCheckbox(self):
        selected_box = self.driver.find_elements(By.XPATH, self.cbx_checkboxitems_xpath)
        for item in range(len(selected_box)):
            if item < 1:
                selected_box[item].click()

    def selectSecondCheckbox(self):
        selected_box = self.driver.find_elements(By.XPATH, self.cbx_checkboxitems_xpath)
        for item in range(len(selected_box)):
            if item == 1:
                selected_box[item].click()

