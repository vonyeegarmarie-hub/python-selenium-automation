from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_results(context):
    expected_message = 'Your cart is empty'
    sleep(3)
    actual_message = context.driver.find_element(By.XPATH, "//*[contains(@class,'styles_ndsHeading__phw6r')]").text
    print(actual_message)
    assert expected_message in actual_message, f'Expected message {expected_message}, not in actual message {actual_message}'


@when('Click Sign In')
def click_sign_in(context):
            context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()


@then('From right side navigation menu, click Sign In')
def side_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_message = 'Sign in or create account'
    actual_message =context.driver.find_element(By. XPATH, "//*[contains(@class,'styles_ndsHeading__phw6r')]").text
    print(actual_message)
    assert expected_message in actual_message, f'Expected message {expected_message}, not in actual message {actual_message}'