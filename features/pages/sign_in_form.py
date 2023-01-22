from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):
    URL = "https://jules.app/sign-in"
    PAGE_TITLE = "Jules"
    EMAIL_SELECTOR = (By.XPATH, '//input')
    PASSWORD_SELECTOR = (By.XPATH, '//*[@type="password"]')
    LOGIN_BUTTON_SELECTOR = (By.ID, 'login-button')

    def input_email(self, email):
        self.driver.find_element(*self.EMAIL_SELECTOR).send_keys(email)

    def input_password(self):
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('ceva')

    def delete_password(self):
        password_element = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_element.send_keys(Keys.COMMAND + "a")
        password_element.send_keys(Keys.DELETE)

    def check_error_message_after_delete_password(self):
        message_text = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p').text
        return message_text

    def check_btn_login_disabled(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')
