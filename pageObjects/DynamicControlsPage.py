from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls():
    cbox_checkbox_xpath = "//input[@type='checkbox']"
    btn_remove_xpath = "//button[normalize-space()='Remove']"
    btn_add_xpath = "//button[normalize-space()='Add']"
    input_confirmationmessage_xpath = "//p[@id='message']"

    def __init__(self, driver):
        self.driver = driver

    def clickCheckbox(self):
        self.driver.find_element(By.XPATH, self.cbox_checkbox_xpath).click()

    def remove_A_checkbox(self):
        self.driver.find_element(By.XPATH, self.btn_remove_xpath).click()

    def getRemoveConfirmationmsg(self):
        try:
            remove_confirmation_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.input_confirmationmessage_xpath))
            )
            return remove_confirmation_element.text
        except:
            print("getRemoveConfirmationmsg function not worked")

    def add_A_checkbox(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def getAddbackConfirmationmsg(self):

        try:
            add_confirmation_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.input_confirmationmessage_xpath))
            )
            return add_confirmation_element.text
        except:
            print("getAddbackConfirmationmsg function not worked")








