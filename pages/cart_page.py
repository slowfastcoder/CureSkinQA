from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


#locators

class CartPage(Page):

    CartIDLoc = (By.ID, "cart-icon-bubble")
    DECREMENT_BUTTON = (By.NAME, "minus")
    ADD_CART_BIGBUTTON = (By.XPATH, "//add-to-cart")
    EMPTY_CART = (By.CLASS_NAME, "mini-cart__empty-text")

    def open_cart(self):
        self.click(*self.CartIDLoc)

    def add_to_cart(self):
        Addbuttons = self.find_elements(*self.ADD_CART_BIGBUTTON)
        #Addbuttons[0].click()
        self.wait_for_element_click(*self.ADD_CART_BIGBUTTON)

    def decrement_qty(self):
        self.wait_for_element_appear(*self.DECREMENT_BUTTON)
        self.wait_for_element_click(*self.DECREMENT_BUTTON)

    def verify_emp(self):
        self.wait_for_element_appear(*self.EMPTY_CART)
        self.verify_element_text("Your cart is currently empty", *self.EMPTY_CART)

