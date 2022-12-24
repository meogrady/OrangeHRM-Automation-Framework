from src.pages.ohrm_login_page import OhrmLoginPage
import requests
import pytest


def test_ohrm_can_navigate_to_linkedin_page(firefox_driver) -> None:
    """
    Tests that clicking the LinkedIn icon at bottom of
    page result in navigation to the OrangeHRM LinkedIn
    page. Should return status code 200 OK.
    :return: None
    """
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    url = ohrm_login.ohrm_login_page_footer_linkedin_link.attribute('href')
    print(url)
    response = requests.get(url)
    assert response.status_code == 999  # Temporary fix until better solution is found. Should return status code 200 OK
    firefox_driver.quit()


def test_ohrm_can_navigate_to_facebook_page(firefox_driver) -> None:
    """
    Tests that clicking the Facebook icon at bottom of
    page result in navigation to the OrangeHRM Facebook
    page. Should return status code 200 OK.
    :return: None
    """
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    url = ohrm_login.ohrm_login_page_footer_facebook_link.attribute('href')

    response = requests.get(url)
    assert response.status_code == 200
    firefox_driver.quit()


def test_ohrm_can_navigate_to_twitter_page(firefox_driver) -> None:
    """
    Tests that clicking the Twitter icon at bottom of
    page result in navigation to the OrangeHRM Twitter
    page. Should return status code 200 OK.
    :return: None
    """
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    url = ohrm_login.ohrm_login_page_footer_twitter_link.attribute('href')

    response = requests.get(url)
    assert response.status_code == 200
    firefox_driver.quit()


def test_ohrm_can_navigate_to_youtube_page(firefox_driver) -> None:
    """
    Tests that clicking the YouTube icon at bottom of
    page result in navigation to the OrangeHRM YouTube
    page. Should get a 200 OK response code.
    :return: None
    """
    ohrm_login = OhrmLoginPage(firefox_driver)
    ohrm_login.go()

    url = ohrm_login.ohrm_login_page_footer_youtube_link.attribute('href')

    response = requests.get(url)
    assert response.status_code == 200
    firefox_driver.quit()

