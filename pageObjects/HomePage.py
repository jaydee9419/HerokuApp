from selenium.webdriver.common.by import By

# identifying the required elements from the homepage
class HomePage():
    lnk_AB_testing_xpath = "//a[normalize-space()='A/B Testing']"
    lnk_add_remove_elements_xpath = "//a[normalize-space()='Add/Remove Elements']"
    lnk_ckeckbox_xpath = "//a[normalize-space()='Checkboxes']"
    lnk_contextmanu_xpath = "//a[normalize-space()='Context Menu']"
    lnk_disappearing_elements_xpath = "//a[normalize-space()='Disappearing Elements']"
    lnk_drag_and_drop_xpath = "//a[normalize-space()='Drag and Drop']"
    lnk_dropdown_xpath = "//a[normalize-space()='Dropdown']"
    lnk_dynamic_controls = "//a[normalize-space()='Dynamic Controls']"
    lnk_dynamicallyload_xpath = "//a[normalize-space()='Dynamic Loading']"
    lnk_entry_ad_xpath = "//a[normalize-space()='Entry Ad']"
    lnk_download_xpath = "//a[normalize-space()='File Download']"
    lnk_upload_xpath = "//a[normalize-space()='File Upload']"
    lnk_authoForm_xpath = "//a[normalize-space()='Form Authentication']"
    lnk_mousehover_xpath = "//a[normalize-space()='Hovers']"
    lnk_alerts_xpath = "//a[normalize-space()='JavaScript Alerts']"
    lnk_geolocation_xpath = "//a[normalize-space()='Geolocation']"
    lnk_keypress_xpath = "//a[normalize-space()='Key Presses']"

    def __init__(self, driver):
        self.driver = driver

    def clickABTest(self):
        self.driver.find_element(By.XPATH, self.lnk_AB_testing_xpath).click()

    def clickAddRemoveElement(self):
        self.driver.find_element(By.XPATH, self.lnk_add_remove_elements_xpath).click()

    def clickCheckbox(self):
        self.driver.find_element(By.XPATH, self.lnk_ckeckbox_xpath).click()

    def clickContextManu(self):
        self.driver.find_element(By.XPATH, self.lnk_contextmanu_xpath).click()

    def clickDisappearing(self):
        self.driver.find_element(By.XPATH, self.lnk_disappearing_elements_xpath).click()

    def clickDragandDrop(self):
        self.driver.find_element(By.XPATH, self.lnk_drag_and_drop_xpath).click()

    def clickDropdown(self):
        self.driver.find_element(By.XPATH, self.lnk_dropdown_xpath).click()

    def clickDynamicControls(self):
        self.driver.find_element(By.XPATH, self.lnk_dynamic_controls).click()

    def clickDynamicallyLoad(self):
        self.driver.find_element(By.XPATH, self.lnk_dynamicallyload_xpath).click()

    def clickEntryAd(self):
        self.driver.find_element(By.XPATH, self.lnk_entry_ad_xpath).click()

    def clickDownload(self):
        self.driver.find_element(By.XPATH, self.lnk_download_xpath).click()

    def clickUpload(self):
        self.driver.find_element(By.XPATH, self.lnk_upload_xpath).click()

    def clickAuthoForm(self):
        self.driver.find_element(By.XPATH, self.lnk_authoForm_xpath).click()

    def clickMouseHover(self):
        self.driver.find_element(By.XPATH, self.lnk_mousehover_xpath).click()

    def clickJAVAScriptAlerts(self):
        self.driver.find_element(By.XPATH, self.lnk_alerts_xpath).click()

    def clickGeolocation(self):
        self.driver.find_element(By.XPATH, self.lnk_geolocation_xpath).click()

    def clickKeyPress(self):
        self.driver.find_element(By.XPATH, self.lnk_keypress_xpath).click()




