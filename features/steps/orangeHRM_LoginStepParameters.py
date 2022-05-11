from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys


@given(u'First launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
    context.driver.maximize_window()


@when(u'Open OrangeHRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{psw}"')
def enterUserAndPassword(context, user, psw):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(psw)


@when(u'Click on login button')
def clickLogin(context):
    context.driver.find_element_by_xpath("//*[@id='btnLogin']").click()


@then(u'User must successfully login to the dashboard page')
def verifyLogin(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]").text
    assert text == 'Dashboard'
    context.driver.close()