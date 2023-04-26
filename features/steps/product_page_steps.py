from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('user searches for {product} product')
def search(context, product):
    context.app.product_page.search_product(product)
    context.app.product_page.select_product()

@when('user clicks on Add to Cart')
def select_product(context):
    context.app.product_page.add_cart()


@when('the cart side bar opens')
def verify_cart_page_check(context):
    sleep(30)
    context.app.product_page.verify_cart_sidebar("Sub")

@then('Verify that correct quantity of {qty} is added')
def verify_qty(context, qty):
    context.app.product_page.verify_qty1(qty)

@when('the user increments the quantity by {qty}')
def increment_qty(context, qty):
    context.app.product_page.increment_quantity(qty)

@then('verify that price has doubled')
def verify_price(context):
    context.app.product_page.verify_price()

@then('verify that the product quantity is set to {quantity}')
def verify_qty2(context, quantity):
    context.app.product_page.verify_qty1(quantity)
