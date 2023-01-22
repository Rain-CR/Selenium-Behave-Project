from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class VerifyUrl(BasePage):
    URL = "https://jules.app/sign-up"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()
