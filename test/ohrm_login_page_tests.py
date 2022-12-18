from src.pages.ohrm_login_page import OhrmLoginPage
from src.pages.ohrm_landing_page import OhrmLandingPage


def test_ohrm_login_with_valid_credentials(firefox_driver):
    # Create objects, go to login page
    ohrm_landing = OhrmLandingPage(firefox_driver)
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # Fill-in fields with valid credentials
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    # Verify that login is successful
    assert ohrm_landing.ohrm_landing_page_welcome.get_text() == 'Dashboard'
    firefox_driver.quit()


def test_ohrm_login_with_empty_credentials(firefox_driver):
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with valid credentials
    ohrm_login.ohrm_username_input.set_text('')
    ohrm_login.ohrm_password_input.set_text('')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrm_login_error_message.get_text() == 'Required'
    firefox_driver.quit()


def test_ohrm_login_with_empty_username_valid_password(firefox_driver):
    firefox_driver.quit()


def test_ohrm_login_with_valid_username_empty_password(firefox_driver):
    firefox_driver.quit()


def test_ohrm_login_with_invalid_username_valid_password(firefox_driver):
    firefox_driver.quit()


def test_ohrm_login_with_valid_username_invalid_password(firefox_driver):
    firefox_driver.quit()
