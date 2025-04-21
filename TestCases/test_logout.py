import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.login_page import LoginPage

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    user_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))
    )
    user_dropdown.click()
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_link.click()
    assert "login" in driver.current_url.lower()
