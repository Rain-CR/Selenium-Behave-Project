from behave import *


@Given('I am on the Jules App-sign-in')
def step_impl(context):
    context.form_page.go_home()


@When('I input correct email')
def step_impl(context):
    context.form_page.input_email('ceva@ceva.com')


@When('I write a password')
def step_impl(context):
    context.form_page.input_password()


@When('I delete the password')
def step_impl(context):
    context.form_page.delete_password()


@Then('Log in button id disabled')
def step_impl(context):
    try:
        login = context.browser.check_btn_login_disabled()
        login.click()
        print('clickable')
    except:
        print('not clickable')