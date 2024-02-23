from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.GeolocationPage import GeolocationPage
import time


class Test_GeoLocation():
    baseURl = ReadConfig.getApplicationURL()

    def test_geolocation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickGeolocation()

        self.glp = GeolocationPage(self.driver)
        self.glp.clickLocation()
        time.sleep(1)

        print(self.glp.getLatitudeInfo())
        self.latitude = self.glp.getLatitudeInfo()
        if self.latitude == "13.0023424":
            assert True
        else:
            assert False

        print(self.glp.getLongitudeInfo())
        self.longitude = self.glp.getLongitudeInfo()
        if self.longitude == "77.594624":
            assert True
        else:
            assert False

