from selenium.webdriver.common.by import By

class GeolocationPage():
    btn_whereAmI_xpath = "//button[normalize-space()='Where am I?']"
    txt_latitude_xpath = "//div[@id='lat-value']"
    txt_longitude_xpath = "//div[@id='long-value']"


    def __init__(self, driver):
        self.driver = driver

    def clickLocation(self):
        self.driver.find_element(By.XPATH, self.btn_whereAmI_xpath).click()

    def getLatitudeInfo(self):
        try:

            return self.driver.find_element(By.XPATH, self.txt_latitude_xpath).text
        except:
            print("Unable to get the latitude info")

    def getLongitudeInfo(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_longitude_xpath).text
        except:
            print("Unable to get the longitude info")
