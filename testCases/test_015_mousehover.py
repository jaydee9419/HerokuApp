from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.MouseHoverPage import MouseHover
import time


class Test_MouseHover():
    baseURL = ReadConfig.getApplicationURL()

    def test_mousehover(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMouseHover()

        self.mhp = MouseHover(self.driver)
        self.mhp.firstImage()
        self.mhp.secondImage()
        self.mhp.thirdImage()

        time.sleep(5)
