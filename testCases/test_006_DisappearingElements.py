from pageObjects.HomePage import HomePage
from pageObjects.DisappearingElementsPage import DisappearingElemets
from utilities.readProperties import ReadConfig
import time


class Test_Checkbox():
    baseURL = ReadConfig.getApplicationURL()

    def test_checkbox(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDisappearing()
        time.sleep(1)

        self.dep = DisappearingElemets(self.driver)
        self.dep.getDisappearingElemets()
