from pageObjects.HomePage import HomePage
from pageObjects.EntryAdPage import EntryAd
from utilities.readProperties import ReadConfig
import time


class Test_EntryAd():
    baseURL = ReadConfig.getApplicationURL()

    def test_EntryAd(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickEntryAd()
        time.sleep(3)

        self.Eadp = EntryAd(self.driver)
        self.Eadp.clickCloseAd()
        self.Eadp.clickReloadAd()
        time.sleep(5)

