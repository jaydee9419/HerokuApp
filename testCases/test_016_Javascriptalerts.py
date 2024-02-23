from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.JAVAScriptAlertsPage import JAVAScriptAlerts
import time


class Test_JavaScriptAlerts():
    baseUrl = ReadConfig.getApplicationURL()

    def test_javaScriptAlerts(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickJAVAScriptAlerts()

        self.jsap = JAVAScriptAlerts(self.driver)
        self.jsap.clickAlert()
        # time.sleep(2)
        self.jsap.clickConfirm()
        # time.sleep(2)
        self.jsap.clickPrompt()
        # time.sleep(2)



