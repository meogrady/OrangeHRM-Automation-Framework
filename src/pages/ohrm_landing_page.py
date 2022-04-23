from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from src.base.base_element import BaseElement
from src.locator.locator import Locator


class OhrmLandingPage(BasePage):

    url = 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'

    @property
    def ohrm_landing_page_welcome(self):
        locator = Locator(By.CSS_SELECTOR, 'a#welcome')
        return BaseElement(driver=self.driver, locator=locator)

