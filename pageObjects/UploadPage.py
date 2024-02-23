from selenium.webdriver.common.by import By
import os

filepath = os.path.abspath(os.curdir) + "\\testdata\\" + "myfile.pdf"



class Upload():
    input_fileupload_xpath = "//input[@id='file-upload']"
    btn_submit_xpath = "//input[@id='file-submit']"

    def __init__(self, driver):
        self.driver = driver

    def uploadfile(self):
        self.driver.find_element(By.XPATH, self.input_fileupload_xpath).send_keys(filepath)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()


