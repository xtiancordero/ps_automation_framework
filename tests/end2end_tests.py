from locators.locators import ProductLocators
from locators.locators import CheckoutLocators
from locators.locators import LoginLocators

def test_complete_order(login_page, product_page, checkout_page, test_data):
    #login
    login_page.login(test_data['login']['standard_user']['username'], 
                     test_data['login']['standard_user']['password'])
    #add to cart an item
    product_page.add_to_cart(ProductLocators.backpack_item)
    #go to cart
    product_page.click_cart_button()
    #checkout the item
    checkout_page.checkout_order(test_data['checkout_information']['first_name'], 
                                 test_data['checkout_information']['last_name'], 
                                 test_data['checkout_information']['postal_code'])
    #validate successful checkout
    assert checkout_page.complete_order_message() == test_data['expected']['order_confirmation']

def test_add_checkout_multiple_items(login_page, product_page, checkout_page, test_data):
    #Login with standard_user
    login_page.login(test_data['login']['standard_user']['username'], 
                     test_data['login']['standard_user']['password'])
    product_page.add_to_cart(ProductLocators.backpack_item)
    product_page.add_to_cart(ProductLocators.bikelight_add_to_cart)
 
    #Go to the cart
    product_page.click_cart_button()

    #Remove an item
    checkout_page.remove_item(2)

    #Validate item is remove
    assert checkout_page.count_element(CheckoutLocators.cart_quantity) == 1
    assert checkout_page.count_element(ProductLocators.bikelight_item) == 0

    #checkout the item
    checkout_page.checkout_order(test_data['checkout_information']['first_name'], 
                                 test_data['checkout_information']['last_name'], 
                                 test_data['checkout_information']['postal_code'])
    
    #validate successful checkout
    assert checkout_page.complete_order_message() == test_data['expected']['order_confirmation']

def test_locked_out_user(login_page, test_data):
    #Login with standard_user
    login_page.login(test_data['login']['locked_out_user']['username'], 
                     test_data['login']['locked_out_user']['password'])
    
    #Validate locked out message
    assert login_page.get_error_message(LoginLocators.lock_out_error) == test_data['expected']['locked_out_error']