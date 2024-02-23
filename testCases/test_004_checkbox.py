from pageObjects.HomePage import HomePage
from pageObjects.CheckboxPage import Checkbox
from utilities.readProperties import ReadConfig
import time


class Test_Checkbox():
    baseURL = ReadConfig.getApplicationURL()

    def test_checkbox(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickCheckbox()
        time.sleep(1)

        self.cp = Checkbox(self.driver)
        self.cp.clearAllSelectedCheckboxs()
        time.sleep(1)
        self.cp.selectAllCheckboxs()
        time.sleep(1)
        self.cp.clearAllSelectedCheckboxs()
        time.sleep(1)
        self.cp.selectFirstCheckbox()
        time.sleep(1)
        self.cp.clearAllSelectedCheckboxs()
        time.sleep(1)
        self.cp.selectSecondCheckbox()
        time.sleep(1)
        self.cp.clearAllSelectedCheckboxs()
        time.sleep(2)
