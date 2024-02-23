from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.DynamicControlsPage import DynamicControls
import time

class Test_DynamicControls():
    baseURL = ReadConfig.getApplicationURL()

    def test_DynamicControls(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDynamicControls()

        self.dcp = DynamicControls(self.driver)
        self.dcp.clickCheckbox()
        time.sleep(1)
        self.dcp.remove_A_checkbox()

        self.removemsg = self.dcp.getRemoveConfirmationmsg()
        if self.removemsg == "It's gone!":
            print(self.removemsg)
            assert True
        else:
            pass

        self.dcp.add_A_checkbox()

        self.backmsg = self.dcp.getAddbackConfirmationmsg()
        if self.backmsg == "It's back!":
            print(self.backmsg)
            assert True
        else:
            pass
        time.sleep(5)

        self.dcp.clickCheckbox()
        time.sleep(1)
        self.dcp.remove_A_checkbox()

        self.removemsg = self.dcp.getRemoveConfirmationmsg()
        if self.removemsg == "It's gone!":
            print(self.removemsg)
            assert True
        else:
            pass

        self.dcp.add_A_checkbox()

        self.backmsg = self.dcp.getAddbackConfirmationmsg()
        if self.backmsg == "It's back!":
            print(self.backmsg)
            assert True
        else:
            pass
        time.sleep(5)



