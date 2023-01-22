import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class CompleteSign(BasePage):

    def click_personal(self):
        self.driver.find_element(By.XPATH, "//input[@value='personal']").click()


    def continue_button(self):
        continue_button = (By.XPATH, "//span[normalize-space()='CONTINUE']")
        return self.driver.find_element(*continue_button).click()
        time.sleep(2)

    def enter_data(self, value):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type your answer here...']").send_keys(value)

    def verify_error(self):
        message_error = (By.XPATH, "//p[contains(text(),'Please enter a valid email address.')]")
        try:
            displayed = self.driver.find_element(*message_error).is_displayed()
        except NoSuchElementException as e:
            displayed = False

        if displayed:
            text = self.driver.find_element(*message_error).text
        else:
            text = "NoSuchElement"
        return displayed, text
