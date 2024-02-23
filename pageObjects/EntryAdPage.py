from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EntryAd():
    window_close_xpath = "//p[normalize-space()='Close']"
    lnk_reload_ad_xpath = "//a[normalize-space()='click here']"


    def __init__(self, driver):
        self.driver = driver

    def clickCloseAd(self):
        try:
            close_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.window_close_xpath)))
            close_element.click()
        except:
            print("Close element not found")

    def clickReloadAd(self):
        try:
            close_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.lnk_reload_ad_xpath)))
            close_element.click()
        except:
            print("Reload ad element not found")




