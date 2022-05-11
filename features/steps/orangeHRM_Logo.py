from behave import *
from selenium import webdriver


@given(u'Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
    context.driver.maximize_window()


@when(u'Open OrangeHRM  homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'Verify that the logo present on page')
def varifyLogo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()