import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class KeyPress():
    input_box_xpath = "//input[@id='target']"
    txt_value_xpath = "//p[@id='result']"

    words = ["a", "b", "c", "d", "e"]



    def __init__(self, driver):
        self.driver = driver

    # def postInput(self):
    #     count = 15
    #     while count > 0:
    #         random_word = random.choice(self.words)
    #         self.driver.find_element(By.XPATH, self.input_box_xpath).send_keys(random_word)
    #         value = self.driver.find_element(By.XPATH, self.txt_value_xpath).text
    #         print(value)
    #         count -= 1
    #         self.driver.find_element(By.XPATH, self.input_box_xpath).clear()
    #         time.sleep(2)

    def postInput(self):
        self.driver.find_element(By.XPATH, self.input_box_xpath).click()
        action = ActionChains(self.driver)

        action.send_keys(Keys.TAB).perform()
        time.sleep(1)
        value = self.driver.find_element(By.XPATH, self.txt_value_xpath).text
        print(value)
