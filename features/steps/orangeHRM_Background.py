from behave import *
from selenium import webdriver
import time

@given(u'Launched browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
    context.driver.maximize_window()


@when(u'Opened application')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Entered valid username and password')
def enterUserAndPassword(context):
    context.driver.find_element_by_id("txtUsername").send_keys("Admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")


@when(u'Clicked login')
def clickLogin(context):
    context.driver.find_element_by_xpath("//*[@id='btnLogin']").click()


@then(u'Users need to login into the dashboard page')
def verifyLogin(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]").text
    assert text == 'Dashboard'
    context.driver.close()


@when(u'Check the leave list')
def checkLeaveList(context):
    context.driver.find_element_by_xpath("//*[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td[2]/div/a/img").click()


@then(u'Log out after checking the leave list')
def clickLogout(context):
    context.driver.find_element_by_css_selector("#welcome").click()
    time.sleep(2)
    context.driver.find_element_by_partial_link_text("Logout").click()
    context.driver.close()


@when(u'Check the timesheets')
def checkTimesheets(context):
    context.driver.find_element_by_xpath("//*[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td[3]/div/a/img").click()


@then(u'Log out after checking the timesheets')
def clickLogout(context):
    context.driver.find_element_by_css_selector("#welcome").click()
    time.sleep(2)
    context.driver.find_element_by_partial_link_text("Logout").click()
    context.driver.close()