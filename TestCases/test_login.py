import pytest
from PageObjects.login_page import LoginPage
from PageObjects.dashboard_page import DashboardPage

def test_home_page_title(driver):
    login_page = LoginPage(driver)
    login_page.load()
    assert "OrangeHRM" in login_page.get_title()

def test_login_functionality(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()
    assert "dashboard" in driver.current_url.lower()  # Check if "dashboard" (case-insensitive) is in the URL
