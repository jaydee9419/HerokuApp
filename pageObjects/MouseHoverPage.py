from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MouseHover():
    img_1_xpath = "//div[1]/img[1]"
    txt_user1_xpath ="//div[1]/div[1]/h5[1]"
    img_2_xpath = "//div[2]/img[1]"
    txt_user2_xpath = "//div[2]/div[1]/h5[1]"
    img_3_xpath = "//div[3]/img[1]"
    txt_user3_xpath = "//div[3]/div[1]/h5[1]"

    def __init__(self, driver):
        self.driver = driver

    def firstImage(self):
        first_image = self.driver.find_element(By.XPATH, self.img_1_xpath)
        ActionChains(self.driver).move_to_element(first_image).perform()
        print(self.driver.find_element(By.XPATH, self.txt_user1_xpath).text)

    def secondImage(self):
        second_image = self.driver.find_element(By.XPATH, self.img_2_xpath)
        ActionChains(self.driver).move_to_element(second_image).perform()
        print(self.driver.find_element(By.XPATH, self.txt_user2_xpath).text)

    def thirdImage(self):
        third_image = self.driver.find_element(By.XPATH, self.img_3_xpath)
        ActionChains(self.driver).move_to_element(third_image).perform()
        print(self.driver.find_element(By.XPATH, self.txt_user3_xpath).text)

