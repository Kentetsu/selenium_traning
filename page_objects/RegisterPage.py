from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='My Account']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content > p")))

    def check_already_have_an_account_string(self):
        already_string = self.driver.find_element(By.CSS_SELECTOR, "div#content > p")
        return already_string

    def check_main_info_table(self):
        main_info = self.driver.find_element(By.CSS_SELECTOR, "fieldset#account")
        return main_info

    def check_firstname_input(self):
        firstname_input = self.driver.find_element(By.ID, "input-firstname")
        return firstname_input

    def check_password_input(self):
        password_input = self.driver.find_element(By.ID, "input-password")
        return password_input

    def check_privacy_checkbox(self):
        privacy_checkbox = self.driver.find_element(By.XPATH, "//input[@name='agree']")
        return privacy_checkbox

    def check_right_table(self):
        right_table = self.driver.find_element(By.XPATH, "//aside[@id='column-right']/div[@class='list-group']")
        return right_table
