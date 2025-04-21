import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

@pytest.mark.usefixtures("driver")
def test_leave_page_navigation(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.click_my_leave()

    leave = LeavePage(driver)
    assert leave.is_leave_page_loaded()
