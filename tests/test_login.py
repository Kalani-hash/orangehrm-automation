import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_successful(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()
    assert "dashboard" in driver.current_url.lower()  # Check if "dashboard" (case-insensitive) is in the URL
