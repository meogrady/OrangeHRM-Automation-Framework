from selenium.webdriver.common.by import By
from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.locator.locator import Locator


class OhrmAssignLeave(BasePage):

    def assign_leave_page_title(self) -> BaseElement:
        locator = Locator(By.CSS_SELECTOR, 'div#assign-leave h1')
        return BaseElement(driver=self.driver, locator=locator)
