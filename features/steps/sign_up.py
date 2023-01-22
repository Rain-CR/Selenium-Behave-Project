from behave import *


@given('I am on the Jules App-sign-in')
def go_sign_up_page(context):
    context.sign_up_page.go_to_page()


@when('I click personal')
def step_impl(context):
    context.sign_up.click_personal()


@when('I click continue')
def step_impl(context):
    context.sign_up.continue_button()


@when('I input  the first name field')
def step_impl(context):
    context.sign_up.enter_data("Cosmin")


@when('I input the last name field')
def step_impl(context):
    context.sign_up.enter_data("Craciun")


@when('I enter "{email}" in the email field')
def step_impl(context, email):
    context.sign_up.enter_data(email)


@then('A message with text "{text}" is displayed')
def step_impl(context, text):
    assert context.sign_up.verify_error()[0]
    assert context.sign_up.verify_error()[1] == text


@then('The text "Please enter a valid email address." is not displayed')
def step_impl(context):
    assert context.sign_up.verify_error()[0] is False
