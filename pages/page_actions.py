from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PageActions(BasePage):
    
    def resolve_locator(self, locator):
        if isinstance(locator, tuple):
            return locator
        if locator.startswith("//") or locator.startswith("(//"):
            return (By.XPATH, locator)
        elif locator.startswith(".") or locator.startswith("#") or "[" in locator:
            return (By.CSS_SELECTOR, locator)
        else:
            return (By.ID, locator)

    def wait_locator(self, locator):
        return self.wait.until(EC.visibility_of_element_located (locator))
    
    def find_locator(self, locator):
        locator = self.resolve_locator(locator)
        self.wait_locator(locator)
        field = self.driver.find_element(*locator)
        return field

    def input_text_to_field(self, locator, text):
        field = self.find_locator(locator)
        field.send_keys(text)
    
    def click_button(self, locator):  
        button = self.find_locator(locator)
        button.click()

    def count_element(self, locator):
        locator = self.resolve_locator(locator)
        elements = self.driver.find_elements(*locator)
        return len(elements)
    
    def get_error_message(self, locator):
        return self.find_locator(locator).text