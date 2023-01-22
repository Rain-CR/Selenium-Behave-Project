from behave import *
import time


@when('I click personal value')
def step_impl(context):
    context.complete_signup.click_personal()


@when('I click continue button')
def step_impl(context):
    context.complete_signup.continue_button()
    time.sleep(2)


@when('I input correct first name')
def step_impl(context):
    context.complete_signup.enter_data('Cosmin')


@when('I input correct last name')
def step_impl(context):
    context.complete_signup.enter_data('Craciun')


@when('I input "{email}"')
def step_impl(context, email):
    context.complete_signup.enter_data(email)


@then('I verify the "{text}" is displayed')
def step_impl(context, text):
    assert context.complete_signup.verify_error()[0]
    assert context.complete_signup.verify_error()[1] == text


@then(u'I verify the "Please enter a valid email address." is not displayed')
def step_impl(context):
    assert context.complete_signup.verify_error()[0] is False
