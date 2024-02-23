from selenium.webdriver.common.by import By

class AuthonticationForm():
    txt_username_xpath = "//input[@id='username']"
    txt_password_xpath = "//input[@id='password']"
    btn_submit_xpath = "//i[normalize-space()='Login']"
    txt_error_xpath = "//div[@id='flash']"

    def __init__(self, driver):
        self.driver = driver

    def filluname(self):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys("Hello")

    def fillpwd(self):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys("Hello")

    def submitButtoon(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def getErrorMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_error_xpath).text
        except:
            print("We are unable to produce error message")
