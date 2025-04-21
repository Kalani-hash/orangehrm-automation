from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_leave_page_loaded(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//h5[text()='Leave List']")))

