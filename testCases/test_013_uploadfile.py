from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.UploadPage import Upload
import time

class Test_Upload():
    baseURL = ReadConfig.getApplicationURL()

    def test_upload(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickUpload()

        self.up = Upload(self.driver)
        self.up.uploadfile()
        time.sleep(2)
        self.up.clickSubmit()
        time.sleep(3)

