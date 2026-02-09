import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from pages.page_actions import PageActions
from utilities.data_loader import load_test_data
from utilities.logger import get_logger

@pytest.fixture
def driver(request):
    chrome_options = Options()
    if os.environ.get("CI"):  # GitHub Actions sets this automatically
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--guest")
    chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False})
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    if request.node.rep_call.failed:
        driver.save_screenshot(f"reports/{request.node.name}.png")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture
def test_data():
    return load_test_data()    

@pytest.fixture
def logger():
    return get_logger("test")

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.fixture
def page_actions(driver):
    return PageActions(driver)