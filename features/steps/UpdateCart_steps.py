from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('user reduces the quantity to 0')
def decrement_qty(context):
    context.app.cart_page.decrement_qty()

@then('verify that the cart is empty')
def verify_empty(context):
    sleep(5)
    context.app.cart_page.verify_emp()

@when('user clicks on the search icon via mobile')
def click_search(context):
    context.app.main_page.clicksearchmobile()

