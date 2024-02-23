from pageObjects.HomePage import HomePage
from pageObjects.DownloadPage import Download
from utilities.readProperties import ReadConfig
import time


class Test_Download():
    baseURL = ReadConfig.getApplicationURL()

    def test_download(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDownload()
        time.sleep(3)

        self.dp = Download(self.driver)
        download_links = self.dp.clickDownload()

        for link_index in range(0, len(download_links)+1):
            if link_index == 2:  # Note: Indexing starts from 0, so change to 1 for the second link
                download_links[link_index].click()

        time.sleep(2)



