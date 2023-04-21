from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')


@given('open the main page')
def open_main(context):
    context.app.main_page.open_main()


@when('click on shop by {product}')
def search_product(context, product):
    context.app.main_page.click_productbtn()

@when('select Face Wash')
def search_product(context):
    pass #if we click on it, the face wash title dissapears

@then('verify that {product}" is shown')
def verifyText(context, product):
    context.app.main_page.verifyText(product)


