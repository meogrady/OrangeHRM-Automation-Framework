from selenium.webdriver.common.by import By

from src.base.base_page import BasePage
from src.base.base_element import BaseElement
from src.locator.locator import Locator


class OhrmLoginPage(BasePage):

    url = 'https://opensource-demo.orangehrmlive.com/'

    @property
    def ohrm_username_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#txtUsername')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#txtPassword')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_submit_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input#btnLogin')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_error_message(self):
        locator = Locator(By.CSS_SELECTOR, 'id#spanMessage')
        return BaseElement(self.driver, locator=locator)

    # TODO: Add code for social media links using etree

    @property
    def ohrm_login_linkedin_page(self):
        locator = Locator(By.XPATH, "//img[@alt='LinkedIn OrangeHRM group']")
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_facebook_page(self):
        locator = Locator(By.XPATH, "//img[@alt='OrangeHRM on Facebook']")
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_twitter_page(self):
        locator = Locator(By.XPATH, "//img[@alt='OrangeHRM on twitter']")
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_youtube_page(self):
        locator = Locator(By.XPATH, "//img[@alt='OrangeHRM on youtube']")
        return BaseElement(self.driver, locator=locator)


