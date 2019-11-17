from behave import *
from selenium.webdriver import Chrome

@given(u'User is on login page')
def login_page(context):
    context.driver.get("https://www.facebook.com")

@when(u'user enters username')
def step_impl(context):
    context.driver.find_element_by_id('email').send_keys('abcd')

@when(u'user enters password')
def step_impl(context):
    context.driver.find_element_by_id('pass').send_keys('abcd')


@when(u'user clicks on signin button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@type='submit']").click()

@then(u'user should be logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should be logged in')


@then(u'user should get welcome message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should get welcome message')


@when(u'user enters search data')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters search data')

