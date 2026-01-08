from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
SEARCH_INPUT = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
SEARCH_SUBMIT = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')

#@given ('Open target main page')
#def open_target_main_page(context):
    #context.driver.get('https://www.target.com/')

#@when ('Search for {product}')
def search_for_mango(context, product):
    print(f"Searching for: {product}")
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(5)  # Increase wait time
    print(f"Current URL after search: {context.driver.current_url}")

sleep (5)

@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
        assert search_word.lower() in context.driver.current_url.lower(),\
            f'Expected query not in {context.driver.current_url.lower()}'