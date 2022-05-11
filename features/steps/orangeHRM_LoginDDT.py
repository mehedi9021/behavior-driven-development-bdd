from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys


@given(u'First need to launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
    context.driver.maximize_window()


@when(u'Open the OrangeHRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter the username "{user}" and password "{psw}"')
def enterUserAndPassword(context, user, psw):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(psw)


@when(u'Click on the login button')
def clickLogin(context):
    context.driver.find_element_by_xpath("//*[@id='btnLogin']").click()


@then(u'User must successfully login to dashboard page')
def verifyLogin(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"