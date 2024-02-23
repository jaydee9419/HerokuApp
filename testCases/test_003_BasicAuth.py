import pytest
from utilities.readProperties import ReadConfig
import os
from pageObjects.BasicAuthPage import BasicAuth


class Test_003_BasicAuth():
    baseURL = ReadConfig.getBasicAuthURL()

    def test_BasicAuth(self, setup):

        # setup browser, application url and maximising window
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bap = BasicAuth(self.driver)
        self.confmsg = self.bap.getConfirmationMsg()
        if self.confmsg == "Congratulations! You must have the proper credentials.":
            print(f"Hare is the responce from the basic auth web page: {self.confmsg}")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "Basic_auth.png")
            assert False


