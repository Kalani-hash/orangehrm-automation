from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_dashboard_loaded(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb")))


    def click_my_leave(self):
        # Ensure this locator is correct for the Leave navigation link
        leave_menu_item = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
        )
        leave_menu_item.click()
