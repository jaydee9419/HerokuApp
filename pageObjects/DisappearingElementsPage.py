from selenium.webdriver.common.by import By

class DisappearingElemets():
    lst_elements_xpath = "//ul//li"

    def __init__(self, driver):
        self.driver = driver

    def getDisappearingElemets(self):
        all_elements = self.driver.find_elements(By.XPATH, self.lst_elements_xpath)
        for item in all_elements:
            print(item.text)
