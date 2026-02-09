from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)
