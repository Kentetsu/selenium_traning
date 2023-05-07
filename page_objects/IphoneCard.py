from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IphoneCard:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get(self.url + "/desktops/iphone")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='iPhone']")))
        self.driver.execute_script("window.stop();")

    def check_search_element(self):
        search = self.driver.find_element(By.ID, 'search')
        return search

    def check_cart_element(self):
        cart = self.driver.find_element(By.ID, 'cart')
        return cart

    def check_pict_screen(self):
        pict_screen = self.driver.find_element(By.CSS_SELECTOR, "li > a.thumbnail")
        return pict_screen

    def check_nav_tabs(self):
        nav_tabs = self.driver.find_element(By.CSS_SELECTOR, "div.col-sm-8 > ul.nav-tabs")
        return nav_tabs

    def check_main_logo(self):
        main_logo = self.driver.find_element(By.XPATH, "//div[@class='row']/div[@class='col-sm-4']")
        return main_logo
