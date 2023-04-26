from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

#locators

CartIDLoc = (By.ID, "cart-icon-bubble")
class CartPage(Page):

    def open_cart(self):
        self.click(self, *CartIDLoc)

    def add_to_cart(self):
        pass
