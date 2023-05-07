from page_objects.AdminInterPage import AdminInterPage
from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.IphoneCard import IphoneCard
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage


def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.check_search_element()
    main_page.check_product_row()
    main_page.check_navbar_element()
    main_page.check_content_element()
    main_page.check_footer_info_row()


def test_catalog_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.check_top_links()
    catalog_page.check_nav_menu()
    catalog_page.check_left_menu()
    catalog_page.check_left_banner()
    catalog_page.check_central_description()


def test_iphone_card(driver):
    iphone_card = IphoneCard(driver)
    iphone_card.check_search_element()
    iphone_card.check_cart_element()
    iphone_card.check_pict_screen()
    iphone_card.check_nav_tabs()
    iphone_card.check_main_logo()


def test_admin_page(driver):
    admin_page = AdminPage(driver)
    admin_page.check_header_logo()
    admin_page.check_main_panel()
    admin_page.check_username()
    admin_page.check_button_login()
    admin_page.check_password()


def test_register_page(driver):
    register_page = RegisterPage(driver)
    register_page.check_already_have_an_account_string()
    register_page.check_main_info_table()
    register_page.check_firstname_input()
    register_page.check_password_input()
    register_page.check_privacy_checkbox()
    register_page.check_right_table()


def test_admin_functional_page(driver):
    test = AdminInterPage(driver)
    test.add_test_product()
    test.remove_test_product()


def test_add_new_user(driver):
    main = MainPage(driver)
    main.add_new_test_user()


def test_change_currency(driver):
    main = MainPage(driver)
    main.change_currency("€")
