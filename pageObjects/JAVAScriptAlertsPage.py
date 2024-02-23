from selenium.webdriver.common.by import By

class JAVAScriptAlerts():
    btn_alert_xpath = "//button[normalize-space()='Click for JS Alert']"
    btn_confirm_xpath = "//button[normalize-space()='Click for JS Confirm']"
    btn_prompt_xpath = "//button[normalize-space()='Click for JS Prompt']"

    def __init__(self, driver):
        self.driver = driver

    def clickAlert(self):
        self.driver.find_element(By.XPATH, self.btn_alert_xpath).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        print("Alert dismissed")


    def clickConfirm(self):
        self.driver.find_element(By.XPATH, self.btn_confirm_xpath).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("Alert accepted")


    def clickPrompt(self):
        self.driver.find_element(By.XPATH, self.btn_prompt_xpath).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("Jay Dee")
        alert.accept()
        print("Alert accepted")

