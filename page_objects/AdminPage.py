from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdminPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.driver.get(self.url + "/admin")
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-heading")))

    def check_header_logo(self):
        header_logo = self.driver.find_element(By.ID, 'header-logo')
        return header_logo

    def check_main_panel(self):
        main_panel = self.driver.find_element(By.CSS_SELECTOR, 'div.col-sm-4 > div.panel')
        return main_panel

    def check_username(self):
        username = self.driver.find_element(By.NAME, "username")
        return username

    def check_button_login(self):
        login_button = self.driver.find_element(By.XPATH, "//div[@class='text-right']/button[*]")
        return login_button

    def check_password(self):
        password = self.driver.find_element(By.NAME, "password")
        return password
