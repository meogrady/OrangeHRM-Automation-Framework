import time

from src.pages.ohrm_login_page import OhrmLoginPage
from src.pages.MainMenu.Leave.ohrm_assign_leave import OhrmAssignLeave
from src.pages.MainMenu.Dashboard.quick_launch_menu import OhrmQuickLaunchMenu


def test_quick_launch_assign_leave(firefox_driver):
    # Create objects, go to login page
    ohrm_login = OhrmLoginPage(driver=firefox_driver)
    ohrm_login.go()

    # Log into OrangeHRM
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    # Link 'Assign Leave' Icon from Quick Launch group.
    quick_launch_menu = OhrmQuickLaunchMenu(driver=firefox_driver)
    time.sleep(1)
    quick_launch_menu.ohrm_navigate_to_assign_leave_page().click()

    # Get text from page and assert
    assign_leave = OhrmAssignLeave(driver=firefox_driver)
    text = assign_leave.assign_leave_page_title().get_text()

    assert text, "Assign Leave"

    firefox_driver.quit()


def test_quick_launch_leave_list(firefox_driver):
    pass


def test_quick_launch_timesheets(firefox_driver):
    pass


def test_quick_launch_apply_leave(firefox_driver):
    pass


def test_quick_launch_my_leave(firefox_driver):
    pass


def test_quick_launch_my_timesheet(firefox_driver):
    pass
