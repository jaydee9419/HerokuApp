import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ABTestingPage import AB_testing
from utilities.readProperties import ReadConfig
import os



class Test_001_Abtesting():
    baseURL = ReadConfig.getApplicationURL()

    def test_ABtesting(self, setup):

        # setup browser, application url and maximising window
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # creating home page object class and calling methods
        self.hp = HomePage(self.driver)
        self.hp.clickABTest()

        # creating home page object class and calling methods
        self.abp = AB_testing(self.driver)
        self.confmsg = self.abp.getConfirmationMsg()

        # validation
        if self.confmsg == "A/B Test Control":
            print(f"Here is the page heading after clicking the AB testing link: {self.confmsg}")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "AB_Testing.png")
            assert False















