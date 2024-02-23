from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.KeyPressPage import KeyPress

class Test_keypress():
    baseURL = ReadConfig.getApplicationURL()

    def test_keypress(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickKeyPress()

        self.kpp = KeyPress(self.driver)
        self.kpp.postInput()
