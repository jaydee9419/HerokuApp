import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AddRemoveElementPage import AddRemoveElement
from utilities.readProperties import ReadConfig
import os
import time


class Test_002_Add_Remove_Element():
    baseURL = ReadConfig.getApplicationURL()

    def test_Add_remove_element(self, setup):

        # setup browser, application url and maximising window
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # creating home page object class and calling methods
        self.hp = HomePage(self.driver)
        self.hp.clickAddRemoveElement()

        # creating Add remove page object and calling required methods
        self.arp = AddRemoveElement(self.driver)
        self.arp.clickAddButton()
        time.sleep(1)
        self.arp.clickRemoveButton()
        time.sleep(1)
        self.arp.clickAddButton()
        time.sleep(1)
        self.arp.clickRemoveButton()
        time.sleep(1)
        self.arp.clickAddButton()
        self.arp.clickAddButton()
        self.arp.clickAddButton()
        time.sleep(1)
        self.arp.clickRemoveButton()
        self.arp.clickRemoveButton()
        self.arp.clickRemoveButton()
        time.sleep(1)
