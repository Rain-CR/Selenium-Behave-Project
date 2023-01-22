from browser import Browser
from pages.log_in_page import FormPage
from pages.verify_url import VerifyUrl
from pages.sign_up import CompleteSign


def before_all(context):
    context.browser = Browser()
    context.form_page = FormPage(context.browser.driver)
    context.verify_url = VerifyUrl(context.browser.driver)
    context.complete_signup = CompleteSign(context.browser.driver)


def after_all(context):
    context.browser.close()
