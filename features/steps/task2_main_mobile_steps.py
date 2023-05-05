import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('User clicks on the hamburger icon')
def click_menu(context):
    context.app.main_page.expandmenu()

@when('clicks on shop by product on the mobile')
def click_menu(context):
    context.app.main_page.click_productmobile()

@when('select "Face Wash" on mobile')
def click_menu(context):
    time.sleep(30)
    context.app.main_page.expandmenu.click_faceWashMobile()