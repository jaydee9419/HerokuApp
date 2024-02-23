from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.DinamicallyLoadPage import DainamicallyLoad
import time

class Test_DynamicallyLoad():
    baseURL = ReadConfig.getApplicationURL()

    def test_DynamicallyLoad(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDynamicallyLoad()

        self.dlp = DainamicallyLoad(self.driver)
        self.dlp.clickExample1()
        self.dlp.clickStart()

        self.getMsg = self.dlp.getConfirmattionmsg()
        if self.getMsg == "Hello World!":
            print(self.getMsg)
            assert True
        else:
            assert False

        self.driver.back()
        self.dlp.clickExample2()
        self.dlp.clickStart()

        self.getMsg = self.dlp.getConfirmattionmsg()
        if self.getMsg == "Hello World!":
            print(self.getMsg)
            assert True
        else:
            assert False
