from selenium.webdriver.common.by import By
import os


class BasicAuth():
    txt_confirmation_xpath = "//p[normalize-space()='Congratulations! You must have the proper credentials.']"

    def __init__(self, driver):
        self.driver = driver

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confirmation_xpath).text
        except:
            None