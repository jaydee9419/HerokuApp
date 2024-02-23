from pageObjects.HomePage import HomePage
from pageObjects.ContextManuPage import ContextManu
from utilities.readProperties import ReadConfig
import time


class Test_Checkbox():
    baseURL = ReadConfig.getApplicationURL()

    def test_checkbox(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickContextManu()
        time.sleep(1)

        self.cmp = ContextManu(self.driver)
        self.cmp.clickContextManu()
        time.sleep(1)

