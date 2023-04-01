from selenium.webdriver.common.by import By

from src.base.base_page import BasePage
from src.base.base_element import BaseElement
from src.locator.locator import Locator


class OhrmLoginPage(BasePage):

    base_url = 'https://opensource-demo.orangehrmlive.com/'

    @property
    def ohrm_username_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input.oxd-input.oxd-input--active[name="username"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input.oxd-input.oxd-input--active[name="password"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_submit_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login'
                                           '-button') 
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_title(self):
        locator = Locator(By.CSS_SELECTOR, 'h5.oxd-text oxd-text--h5 orangehrm-login-title')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_username_error_message(self):
        locator = Locator(By.XPATH, './/input[@name="username"]/../../span')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_password_error_message(self):
        locator = Locator(By.XPATH, './/input[@name="password"]/../../span')
        return BaseElement(self.driver, locator=locator)

    def ohrn_login_alert_error_message(self):
        locator = Locator(By.CSS_SELECTOR, 'p.oxd-text.oxd-text--p.oxd-alert-content-text')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_page_footer_linkedin_link(self) -> BaseElement:
        locator = Locator(By.CSS_SELECTOR, 'a[href*="www.linkedin.com"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_page_footer_facebook_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href*="facebook.com"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_page_footer_twitter_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href*="twitter.com"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def ohrm_login_page_footer_youtube_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href*="www.youtube.com"]')
        return BaseElement(self.driver, locator=locator)