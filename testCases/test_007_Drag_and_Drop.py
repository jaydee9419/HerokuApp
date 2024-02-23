from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.DragAndDropPage import DragAndDrop
import time

class Test_Drag_and_Drop():
    baseURL = ReadConfig.getApplicationURL()

    def test_Drag_and_Drop(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDragandDrop()

        self.dadp = DragAndDrop(self.driver)
        self.dadp.drag_and_drop_AtoB()
        time.sleep(1)
        self.dadp.drag_and_drop_BtoA()
        time.sleep(1)
        self.dadp.drag_and_drop_AtoB()
        time.sleep(1)
        self.dadp.drag_and_drop_BtoA()
        time.sleep(1)
        self.dadp.drag_and_drop_AtoB()
        time.sleep(1)
        self.dadp.drag_and_drop_BtoA()
        time.sleep(3)




