from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from src.base.base_element import BaseElement
from src.locator.locator import Locator


class OhrmDashboardPage(BasePage):

    url = 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'

    @property
    def ohrm_landing_page_welcome(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

