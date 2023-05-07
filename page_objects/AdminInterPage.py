from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class AdminInterPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.driver.get(self.url + "/admin")
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-heading")))
        self.driver.find_element(By.ID, "input-username").send_keys("user")
        self.driver.find_element(By.ID, "input-password").send_keys("bitnami")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "column-left")))

    def goto_product_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".parent.collapsed[href='#collapse1']").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Products']")))
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Products']").click()
        return self.driver

    def add_test_product(self):
        self.driver = self.goto_product_page()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-plus']")))
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-plus']").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "input-name1")))
        self.driver.find_element(By.ID, "input-name1").send_keys("test name")
        self.driver.find_element(By.CSS_SELECTOR, "div[role='textbox']").send_keys("test description")
        self.driver.find_element(By.ID, "input-meta-title1").send_keys("test meta title1")
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Data']").click()
        self.driver.find_element(By.ID, "input-model").send_keys("1")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'test name')]")

    def remove_test_product(self):
        check_box_xpath = "//td[contains(text(), 'test name')]/parent::tr/td[@class='text-center']/input"
        self.driver = self.goto_product_page()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'test name')]")))
        self.driver.find_element(By.XPATH, check_box_xpath).click()
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-trash-o']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))

