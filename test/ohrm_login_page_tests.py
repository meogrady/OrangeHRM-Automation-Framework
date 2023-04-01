from src.pages.ohrm_login_page import OhrmLoginPage
from src.pages.MainMenu.Dashboard.ohrm_dashboard_page import OhrmDashboardPage


def test_ohrm_login_with_valid_credentials(firefox_driver):
    # Create objects, go to login page
    ohrm_dashboard = OhrmDashboardPage(firefox_driver)
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # Fill-in fields with valid credentials
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    # Verify that login is successful
    assert ohrm_dashboard.ohrm_dashboard_page_header_title.get_text() == 'Dashboard'
    firefox_driver.quit()


def test_ohrm_login_with_empty_credentials(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with empty credentials
    ohrm_login.ohrm_username_input.set_text('')
    ohrm_login.ohrm_password_input.set_text('')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrm_login_username_error_message.get_text() == 'Required'
    assert ohrm_login.ohrm_login_password_error_message.get_text() == 'Required'
    firefox_driver.quit()


def test_ohrm_login_with_empty_username_valid_password(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with empty credentials
    ohrm_login.ohrm_username_input.set_text('')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrm_login_username_error_message.get_text() == 'Required'
    firefox_driver.quit()


def test_ohrm_login_with_valid_username_empty_password(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with empty credentials
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrm_login_password_error_message.get_text() == 'Required'
    firefox_driver.quit()


def test_ohrm_login_with_invalid_username_valid_password(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with empty credentials
    ohrm_login.ohrm_username_input.set_text('Invalid')
    ohrm_login.ohrm_password_input.set_text('invalid123')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrn_login_alert_error_message().get_text() == 'Invalid credentials'
    firefox_driver.quit()


def test_ohrm_login_with_valid_username_invalid_password(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with empty credentials
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin124')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrn_login_alert_error_message().get_text() == 'Invalid credentials'
    firefox_driver.quit()
