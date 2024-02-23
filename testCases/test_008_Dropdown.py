from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.DropdownPage import Dropdown
import time

class Test_Drag_and_Drop():
    baseURL = ReadConfig.getApplicationURL()

    def test_Drag_and_Drop(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDropdown()

        self.ddp = Dropdown(self.driver)
        self.ddp.selectOptions_by_visable_text()
        time.sleep(3)
        self.ddp.selectOptions_by_index_number()
        time.sleep(3)
        self.ddp.selectOptions_by_value()
        time.sleep(3)
