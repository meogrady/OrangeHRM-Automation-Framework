from src.pages.ohrm_login_page import OhrmLoginPage
# from src.pages.MainMenu.Leave.ohrm_assign_leave import OhrmAssignLeave
from src.pages.MainMenu.Dashboard.ohrm_dashboard_page import OhrmDashboardPage


def test_verify_page(firefox_driver):
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()
    ohrm_dashboard = OhrmDashboardPage(firefox_driver)

    assert ohrm_dashboard.ohrm_dashboard_page_header_title.get_text() == 'Dashboard'
    firefox_driver.quit()

'''
def test_quick_launch_assign_leave(firefox_driver):
    # Create objects, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # Log into OrangeHRM
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    # Link 'Assign Leave' Icon from Quick Launch group.
    quick_launch_menu = OhrmQuickLaunchMenu(driver=firefox_driver)
    quick_launch_menu.ohrm_navigate_to_assign_leave_page().click()

    # Get text from page and assert
    assign_leave = OhrmAssignLeave(driver=firefox_driver)
    text = assign_leave.assign_leave_page_title().get_text()

    assert text, "Assign Leave"

    firefox_driver.quit()
'''

'''
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

'''