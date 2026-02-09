from selenium.webdriver.common.by import By


class LoginLocators():
    username = 'user-name'
    password = '//input[@data-test="password"]'
    login_button ='//input[@data-test="login-button"]'
    lock_out_error = '//h3[@data-test="error"]'

class CheckoutLocators():
    checkout_button = 'checkout'
    first_name_field = 'first-name'
    last_name_field = 'last-name'
    zip_code_field = 'postal-code'
    continue_button = 'continue'
    finish_button = 'finish'
    page_header = '.complete-header'
    remove_button = '//button[text()="Remove"]'
    cart_quantity = '.cart_quantity'


class ProductLocators():
    shopping_cart_link = '//a[@data-test="shopping-cart-link"]'
    backpack_item = '#add-to-cart-sauce-labs-backpack'
    bikelight_add_to_cart = '#add-to-cart-sauce-labs-bike-light'
    bikelight_item = '//*[text()="Sauce Labs Bike Light"]' 
    tshirt_item = '#add-to-cart-sauce-labs-bolt-t-shirt'
    jacket_item = '#add-to-cart-sauce-labs-fleece-jacket'
