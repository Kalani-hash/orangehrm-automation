from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def get_title(self):
        return self.driver.title

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb")))
