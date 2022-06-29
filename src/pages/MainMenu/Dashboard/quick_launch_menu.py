from selenium.webdriver.common.by import By
from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.locator.locator import Locator


class OhrmQuickLaunchMenu(BasePage):

    def ohrm_navigate_to_assign_leave_page(self) -> BaseElement:
        locator = Locator(By.XPATH, '//span[contains(text(), "Assign Leave")]')
        return BaseElement(driver=self.driver, locator=locator)

    def ohrm_leave_list(self):
        pass

    def ohrm_timesheet(self):
        pass

    def ohrm_apply_leave(self):
        pass

    def ohrm_my_leave(self):
        pass

    def ohrm_my_timesheet(self):
        pass
