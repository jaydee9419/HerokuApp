from selenium.webdriver.common.by import By


# identifying the required elements from the AB testing page
class AB_testing():
    txt_AB_Testpage_xpath = "//h3[normalize-space()='A/B Test Control']"

    def __init__(self, driver):
        self.driver = driver

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_AB_Testpage_xpath).text

        except:
            None
