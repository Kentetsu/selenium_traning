from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#search")))

    def check_search_element(self):
        search = self.driver.find_element(By.CSS_SELECTOR, "div#search")
        return search

    def check_navbar_element(self):
        navbar = self.driver.find_element(By.CSS_SELECTOR, "nav > div.navbar-ex1-collapse")
        return navbar

    def check_content_element(self):
        content = self.driver.find_element(By.ID, "content")
        return content

    def check_product_row(self):
        product_row = self.driver.find_element(By.XPATH, "//div[@id='content']/div[@class='row']")
        return product_row

    def check_footer_info_row(self):
        footer_info = self.driver.find_element(By.CSS_SELECTOR, "footer > div > div.row")
        return footer_info

    def add_new_test_user(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
        self.driver.find_element(By.XPATH, "//ul/li/a[contains(text(), 'Register')]").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
        self.driver.find_element(By.ID, "input-firstname").send_keys("test_firstname")
        self.driver.find_element(By.ID, "input-lastname").send_keys("test_lastname")
        self.driver.find_element(By.ID, "input-email").send_keys("test_email@yandex.ru")
        self.driver.find_element(By.ID, "input-telephone").send_keys("test_telephone")
        self.driver.find_element(By.ID, "input-password").send_keys("test_password")
        self.driver.find_element(By.ID, "input-confirm").send_keys("test_password")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='1'][name='agree']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()

    def change_currency(self, currency):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-caret-down']").click()
        if currency == "£":
            self.driver.find_element(By.CSS_SELECTOR, "button[name='GBP']").click()
        elif currency == "€":
            self.driver.find_element(By.CSS_SELECTOR, "button[name='EUR']").click()
        elif currency == "$":
            self.driver.find_element(By.CSS_SELECTOR, "button[name='USD']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                          "button[class='btn btn-link dropdown-toggle'] strong")))
        currency_marc = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle'] strong")
        assert currency_marc.text == currency
        return currency_marc


