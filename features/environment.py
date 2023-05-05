from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from app.application import Application


def browser_init(context, test_name):
    """
    :param test_name:
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path='I:\python bdd automation course\chromdriver 4.19.23\chromedriver.exe')
    #context.driver = webdriver.Chrome(executable_path='I:/seleniumdrivers/chrome/chromedriver')

#mobile emulator
    mobile_emulation = {"deviceName": "Nexus 5"}

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities())


    #context.browser = webdriver.Safari()
    #context.browser = webdriver.Firefox()

    #browser stack setup
    bs_user = 'bothmaster_plYPsd'
    bs_pw = 'CsBhzdsLMnFsxssES3vL'
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '112.0',
        'os': 'Windows',
        'os_version': '10',
        'name': test_name
        #'name': 'Bstack-[Python] Sample Test'
        # 'browser_version': '112.0',

    }
    url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'


    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('--window-size=1920,1080')
    #options.add_argument('--start-maximized')

    #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)


    #context.driver = webdriver.Chrome(chrome_options=options, executable_path='I:\python bdd automation course\chromdriver 4.19.23\chromedriver.exe')


    #options2 = webdriver.FirefoxOptions()
    #options2.add_argument("-headless")
    #options2.add_argument('--window-size=1920,1080')
    #options2.add_argument('--start-maximized')
    #firefox_binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    #options2.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #context.driver = webdriver.Firefox(options=options2, firefox_binary=firefox_binary, executable_path='I:\seleniumdrivers\\firefox0.33\geckodriver.exe')


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
