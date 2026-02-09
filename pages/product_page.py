from pages.page_actions import PageActions
from locators.locators import ProductLocators
class ProductPage(PageActions):
        
    def add_to_cart(self, item):
        self.click_button(item)

    def click_cart_button(self):
        self.click_button(ProductLocators.shopping_cart_link)