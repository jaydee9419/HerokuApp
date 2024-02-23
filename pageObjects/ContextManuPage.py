from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class ContextManu():
    box_contextbox_xpath = "//div[@id='hot-spot']"


    def __init__(self, driver):
        self.driver = driver

    def clickContextManu(self):
        box = self.driver.find_element(By.XPATH, self.box_contextbox_xpath)
        actionChains = ActionChains(self.driver)
        actionChains.context_click(box).perform()
        time.sleep(2)

        alert = self.driver.switch_to.alert
        alert.accept()

