from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')


@given('open the main page')
def open_main(context):
    context.app.main_page.open_main()
    context.app.main_page.close_popup()


@when('click on shop by {product}')
def search_product(context, product):
    context.app.main_page.click_productbtn()


@when('select "{product}"')
def select_facewash(context, product):
    context.app.main_page.verifyText(product)


@then('verify url contains "{name}" is shown')
def verifyurl(context, name):
    context.app.main_page.verifyUrl(name);


