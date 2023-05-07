from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#search")))
    driver.find_element(By.CSS_SELECTOR, "div#search")
    driver.find_element(By.CSS_SELECTOR, "nav > div.navbar-ex1-collapse")
    driver.find_element(By.ID, "content")
    driver.find_element(By.XPATH, "//div[@id='content']/div[@class='row']")
    driver.find_element(By.CSS_SELECTOR, "footer > div > div.row")


def test_catalog_page(driver, url):
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    driver.get(url + "/desktops")
    wait.until(EC.visibility_of_element_located((By.ID, "top-links")))
    driver.find_element(By.ID, "top-links")
    driver.find_element(By.CSS_SELECTOR, "nav#menu")
    driver.find_element(By.CSS_SELECTOR, "aside#column-left > div.list-group")
    driver.find_element(By.XPATH, "//div[@class='swiper-viewport']/div[@id='banner0']")
    driver.find_element(By.XPATH, "//div[@id='content']/div[@class='row']")


def test_product_card(driver, url):
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    driver.get(url + "/desktops/iphone")
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='iPhone']")))    # Fix long page loading
    driver.execute_script("window.stop();")
    driver.find_element(By.ID, 'search')
    driver.find_element(By.ID, 'cart')
    driver.find_element(By.CSS_SELECTOR, "li > a.thumbnail")
    driver.find_element(By.CSS_SELECTOR, "div.col-sm-8 > ul.nav-tabs")
    driver.find_element(By.XPATH, "//div[@class='row']/div[@class='col-sm-4']")


def test_admin_page(driver, url):
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    driver.get(url + "/admin")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-heading")))
    driver.find_element(By.ID, 'header-logo')
    driver.find_element(By.CSS_SELECTOR, 'div.col-sm-4 > div.panel')
    driver.find_element(By.NAME, "username")
    driver.find_element(By.XPATH, "//div[@class='text-right']/button[*]")
    driver.find_element(By.NAME, "password")


def test_register_page(driver, url):
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    driver.get(url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='My Account']")))
    driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    # /index.php?route=account/register
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content > p")))
    driver.find_element(By.CSS_SELECTOR, "div#content > p")
    driver.find_element(By.CSS_SELECTOR, "fieldset#account")
    driver.find_element(By.ID, "input-firstname")
    driver.find_element(By.ID, "input-password")
    driver.find_element(By.XPATH, "//input[@name='agree']")
    driver.find_element(By.XPATH, "//aside[@id='column-right']/div[@class='list-group']")
