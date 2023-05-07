from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CatalogPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get(self.url + "/desktops")
        self.wait.until(EC.visibility_of_element_located((By.ID, "top-links")))

    def check_top_links(self):
        top_links = self.driver.find_element(By.ID, "top-links")
        return top_links

    def check_nav_menu(self):
        nav_menu = self.driver.find_element(By.CSS_SELECTOR, "nav#menu")
        return nav_menu

    def check_left_menu(self):
        left_menu = self.driver.find_element(By.CSS_SELECTOR, "aside#column-left > div.list-group")
        return left_menu

    def check_left_banner(self):
        left_banner = self.driver.find_element(By.XPATH, "//div[@class='swiper-viewport']/div[@id='banner0']")
        return left_banner

    def check_central_description(self):
        central_description = self.driver.find_element(By.XPATH, "//div[@id='content']/div[@class='row']")
        return central_description
