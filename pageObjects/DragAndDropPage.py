from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDrop():
    img_a_xpath = "//div[normalize-space()='A']"
    img_b_xpath = "//div[normalize-space()='B']"

    def __init__(self, driver):
        self.driver = driver


    def drag_and_drop_AtoB(self):
        source = self.driver.find_element(By.XPATH, self.img_a_xpath)
        target = self.driver.find_element(By.XPATH, self.img_b_xpath)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def drag_and_drop_BtoA(self):
        source = self.driver.find_element(By.XPATH, self.img_a_xpath)
        target = self.driver.find_element(By.XPATH, self.img_b_xpath)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

