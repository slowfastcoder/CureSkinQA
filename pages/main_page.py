from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class MainPage(Page):

    #locators on the mainpage
    labelXpath = (By.XPATH,"//*[@class='label']")
    SearchProductBtn = (By.LINK_TEXT, "Shop by Product")
    ExpectedTextLoc = (By.XPATH, "//*[@data-title='Face Washes']")

    def open_main(self):
        self.open_url()

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



