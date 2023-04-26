from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

#locators

SAVE_PRICE = ""


class ProductPage(Page):
    SEARCH_BUTTON = (By.CLASS_NAME, "header__search")
    SEARCH_TEXT = (By.ID, "Search-In-Modal")
    SEARCH_RESULTS = (By.CLASS_NAME, "predictive-search__list-item")

    POPUP_CLOSE = (By.CLASS_NAME, "popup-close")

    #locators from cart page
    ADD_CART = (By.NAME, "add")
    MINI_CART = (By.CLASS_NAME, "mini-cart__inner")
    SUB_TOTAL = (By.CLASS_NAME, "subtotal")
    QUANTITY_INPUT = (By.CLASS_NAME, "quantity__input")
    SUB_TOTAL_PRICE = (By.CLASS_NAME, "mini-cart-subtotal")
    INCREMENT_BUTTON = (By.NAME, "plus")




    def search_product(self, search_key):

        #self.click(*self.SEARCH_BUTTON)
        #self.input_text(search_key, *self.SEARCH_TEXT)

        if self.wait_for_element_appear(*self.POPUP_CLOSE):
            self.click(*self.POPUP_CLOSE)

        if self.wait_for_element_appear(*self.SEARCH_BUTTON):
            self.click(*self.SEARCH_BUTTON)
            self.input_text(search_key, *self.SEARCH_TEXT)

    def input_search(self, search_key):
        pass

    def select_product(self):
        self.wait_for_element_appear(*self.SEARCH_RESULTS)
        self.click(*self.SEARCH_RESULTS)


    def add_cart(self):
        self.wait_for_element_click(*self.ADD_CART)

    def verify_cart_sidebar(self, text):
        self.wait_for_element_appear(*self.MINI_CART)
        #self.verify_partial_text(text *self.SUB_TOTAL)

    def verify_price(self):
        self.wait_for_element_appear(*self.MINI_CART)
        #self.verify_element_text(*self.QUANTITY_INPUT, qty)
        self.wait_for_element_appear(*self.SUB_TOTAL_PRICE)
        currenttotalprice = self.find_element(*self.SUB_TOTAL_PRICE)
        print(currenttotalprice.text)
        SAVE_PRICE = currenttotalprice.text

    def increment_quantity(self, qty):
        #i = 0
        #while i < int(qty):
            self.wait_for_element_appear(*self.INCREMENT_BUTTON)
            self.wait_for_element_click(*self.INCREMENT_BUTTON)
            #i = i+i

    def verify_qty1(self,qty):
        self.verify_element_attribute_value(qty, *self.QUANTITY_INPUT)


