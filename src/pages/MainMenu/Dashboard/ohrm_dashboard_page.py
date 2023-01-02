from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from src.base.base_element import BaseElement
from src.locator.locator import Locator


class OhrmDashboardPage(BasePage):

    url = 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'

    @property
    def ohrm_dashboard_page_header_title(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_assign_leave_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'button.oxd-icon-button.orangehrm-quick-launch-icon[title="Assign Leave"]')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_leave_list_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_timesheets_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_apply_leave_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_my_leave_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

    def navigate_to_my_timesheet_from_quick_launch(self):
        locator = Locator(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6')
        return BaseElement(driver=self.driver, locator=locator)

