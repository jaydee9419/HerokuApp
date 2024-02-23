from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DainamicallyLoad():
    lnk_example1_xpath = "//a[normalize-space()='Example 1: Element on page that is hidden']"
    lnk_example2_xpath = "//a[normalize-space()='Example 2: Element rendered after the fact']"
    btn_start_xpath = "//button[normalize-space()='Start']"
    txt_confirmationmsg_xpath = "//h4[normalize-space()='Hello World!']"

    def __init__(self, driver):
        self.driver = driver

    def clickExample1(self):
        try:
            example1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.lnk_example1_xpath)))
            example1.click()
        except:
            print("Example2 element not found")

    def clickExample2(self):
        try:
            example2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.lnk_example2_xpath)))
            example2.click()
        except:
            print("Example2 element not found")


    def clickStart(self):
        try:
            start = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.btn_start_xpath)))
            start.click()
        except:
            print("Start element not found")

    def getConfirmattionmsg(self):
        try:
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_confirmationmsg_xpath)))

            return message_element.text
        except:
            print('Confirmattionmsg not displayed')

