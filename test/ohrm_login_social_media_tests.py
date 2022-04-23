import time
from src.pages.ohrm_login_page import OhrmLoginPage


def test_ohrm_can_navigate_to_linkedin_page(firefox_driver) -> None:
    """
    Tests that clicking the LinkedIn icon at bottom of
    page result in navigation to the OrangeHRM LinkedIn
    page.
    :return: None
    """
    ohrm_login = OhrmLoginPage(driver=firefox_driver)
    ohrm_login.go()

    ohrm_login.ohrm_login_linkedin_page.click()
    time.sleep(1)
    firefox_driver.quit()


def test_ohrm_can_navigate_to_facebook_page(firefox_driver) -> None:
    """
    Tests that clicking the Facebook icon at bottom of
    page result in navigation to the OrangeHRM Facebook
    page.
    :return: None
    """
    ohrm_login = OhrmLoginPage(driver=firefox_driver)
    ohrm_login.go()

    ohrm_login.ohrm_login_facebook_page.click()
    time.sleep(2)
    firefox_driver.quit()


def test_ohrm_can_navigate_to_twitter_page(firefox_driver) -> None:
    """
    Tests that clicking the Twitter icon at bottom of
    page result in navigation to the OrangeHRM Twitter
    page.
    :return: None
    """
    ohrm_login = OhrmLoginPage(driver=firefox_driver)
    ohrm_login.go()

    ohrm_login.ohrm_login_twitter_page.click()
    time.sleep(1)
    firefox_driver.quit()


def test_ohrm_can_navigate_to_youtube_page(firefox_driver) -> None:
    """
    Tests that clicking the YouTube icon at bottom of
    page result in navigation to the OrangeHRM YouTube
    page.
    :return: None
    """
    ohrm_login = OhrmLoginPage(driver=firefox_driver)
    ohrm_login.go()

    ohrm_login.ohrm_login_youtube_page.click()
    time.sleep(1)
    firefox_driver.quit()

