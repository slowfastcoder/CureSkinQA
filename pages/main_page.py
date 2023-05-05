import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class MainPage(Page):

    #locators on the mainpage
    labelXpath = (By.XPATH,"//*[@class='label']")
    SearchProductBtn = (By.XPATH, "//*[contains(text(),'Shop by Product')]")
    FaceWashMobileBtn = (By.XPATH, "//*[contains(text(),'Face Washes')]")

    listofButtons = (By.XPATH, "//*[@class='menu-drawer__menu-item list-menu__item focus-inset']") #[7] is fashwash
    ExpectedTextLoc = (By.XPATH, "//*[@data-title='Face Washes']")

    POPUP_CLOSE = (By.CLASS_NAME, "popup-close")
    HAMBURGER_ICON = (By.CLASS_NAME, "menu-drawer-container")

    def open_main(self):
        self.open_url()

    def expandmenu(self):
        self.click(*self.HAMBURGER_ICON)

    def close_popup(self):
        if self.wait_for_element_appear(*self.POPUP_CLOSE):
            self.click(*self.POPUP_CLOSE)

    def click_productmobile(self):
        self.wait_for_element_appear(*self.SearchProductBtn)
        self.click(*self.SearchProductBtn)

    def click_faceWashMobile(self):
        time.sleep(10)
        #self.wait_for_element_click(*self.FaceWashMobileBtn)
        #self.click(*self.FaceWashMobileBtn)
        #listofButtons = self.find_elements(*self.listofButtons)
        #listofButtons[7].click() #7 is fashwash in mobile
        self.action_chains_click(*self.FaceWashMobileBtn)




    def click_productbtn(self):
        listofButtons = self.find_elements(*self.labelXpath)
        listofButtons[7].click()
        #self.click(*self.SearchProductBtn)
        #self.wait_for_element_click(*self.SearchProductBtn)  won't find element



    def verifyText(self, expectedText):
        self.wait_for_element_appear(*self.ExpectedTextLoc)
        self.click(*self.ExpectedTextLoc)
        #self.verify_element_text(expectedText, *self.ExpectedTextLoc)

    def verifyUrl(self, expectedquery):
        self.verify_url_contains_query(expectedquery)



