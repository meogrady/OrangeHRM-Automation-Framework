from selenium import webdriver
from src.pages.ohrm_login_page import OhrmLoginPage
from src.pages.ohrm_landing_page import OhrmLandingPage

driver = webdriver.Firefox()


def test_ohrm_login_with_valid_credentials():
    # Create objects, go to login page
    ohrm_landing = OhrmLandingPage(driver=driver)
    ohrm_login = OhrmLoginPage(driver=driver)
    ohrm_login.go()

    # Fill-in fields with valid credentials
    ohrm_login.ohrm_username_input.set_text('Admin')
    ohrm_login.ohrm_password_input.set_text('admin123')
    ohrm_login.ohrm_submit_button.click()

    # Verify that login is successful
    assert ohrm_landing.ohrm_landing_page_welcome.get_text() == 'Welcome Paul', 'ERROR: Credential mismatch'

    driver.quit()


def test_ohrm_login_with_empty_credentials():
    # Create object, go to login page
    ohrm_login = OhrmLoginPage(driver=driver)
    ohrm_login.go()

    # TODO: Should assert navigated to login page

    # Fill-in fields with valid credentials
    ohrm_login.ohrm_username_input.set_text('')
    ohrm_login.ohrm_password_input.set_text('')
    ohrm_login.ohrm_submit_button.click()

    assert ohrm_login.ohrm_login_error_message.get_text() == 'Username cannot be empty'


def test_ohrm_login_with_empty_username_valid_password():
    pass


def test_ohrm_login_with_valid_username_empty_password():
    pass


def test_ohrm_login_with_invalid_username_valid_password():
    pass


def test_ohrm_login_with_valid_username_invalid_password():
    pass
