from features.pages.sign_up import SignUp
from browser import Browser
from features.pages.sign_up_URL_verify import VerifyUrl
from features.pages.sign_in_form import FormPage


def before_all(context):
    context.browser = Browser()
    context.sign_up = SignUp(context.browser.driver)
    context.verify_url = VerifyUrl(context.browser.driver)
    context.sign_in = FormPage(context.browser.driver)


def after_all(context):
    context.browser.close()
