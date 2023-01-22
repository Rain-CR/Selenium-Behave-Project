from behave import *


@When('I input correct email')
def step_impl(context):
    context.sign_in_form.input_email('craciun.raducosmin@yahoo.com')


@When('I write a password')
def step_impl(context):
    context.sign_in_form.input_password("Somethin.something123")


@When('I clear the password')
def step_impl(context):
    context.sign_in_form.delete_password()


@Then('Message error is displayed')
def step_impl(context):
    assert context.sign_in_form.check_error_message_after_delete_password() == "Please enter your password!"


@Then('Log in button id disabled')
def step_impl(context):
    try:
        login = context.browser.check_btn_login_disabled()
        login.click()
        print('clickable')
    except:
        print('not clickable')
