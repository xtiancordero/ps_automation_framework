from pages.page_actions import PageActions
from locators.locators import CheckoutLocators


class CheckoutPage(PageActions):
    
    def fill_out_forms(self, firstname, lastname, postal_code):
        self.input_text_to_field(CheckoutLocators.first_name_field, firstname)
        self.input_text_to_field(CheckoutLocators.last_name_field, lastname)
        self.input_text_to_field(CheckoutLocators.zip_code_field, postal_code)
        self.click_button(CheckoutLocators.continue_button)

    def checkout_order(self, firstname, lastname, postal_code):
        self.click_button(CheckoutLocators.checkout_button)
        self.fill_out_forms(firstname, lastname, postal_code)
        self.click_button(CheckoutLocators.finish_button)

    def complete_order_message(self):
        return self.find_locator(CheckoutLocators.page_header).text
        
    def remove_item(self, item_number):
        item = f'({CheckoutLocators.remove_button})[{item_number}]'
        self.click_button(item)
    