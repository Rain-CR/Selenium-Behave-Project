from behave import *


@when('I click "{page_link_text}" link')
def step_impl(context, page_link_text):
    context.verify_url.go_to(page_link_text)


@then('I am redirected to sign-up page')
def step_impl(context):
    assert context.browser.get_current_url() == context.verify_url.URL
