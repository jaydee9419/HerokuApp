from selenium.webdriver.common.by import By

class Download():
    lnk_files_tag = "a"

    def __init__(self, driver):
        self.driver = driver

    def clickDownload(self):
        links = self.driver.find_elements(By.TAG_NAME, self.lnk_files_tag)
        return links

