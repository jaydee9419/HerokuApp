

from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.AuthonticationFormPage import AuthonticationForm

import os

class Test_AuthoForm():
    baseURl = ReadConfig.getApplicationURL()

    def test_authoform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickAuthoForm()

        self.afp = AuthonticationForm(self.driver)
        self.afp.filluname()
        self.afp.fillpwd()
        self.afp.submitButtoon()
        self.afp.getErrorMsg()
        print(self.afp.getErrorMsg())

        self.confirmsg = self.afp.getErrorMsg()

        if self.confirmsg == "Your username is invalid!\n×":
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "AuthForm.png")
            assert True
        else:
            print("Test got failed")
            assert False
