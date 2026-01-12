from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class, 'styles_listingPageResultsCount')]")
PRODUCT_LINK = (By.CSS_SELECTOR, '[data-test="product-title"]')


@given ('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when('Search for {product}')
def search_for_notebook(context, product):
    context.driver.wait.until(EC.presence_of_element_located(SEARCH_FIELD)).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()

@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.driver.wait.until(EC.presence_of_element_located(SEARCH_RESULTS_TEXT))
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'
    sleep(5)

@then('Add {product} to cart')
def add_product(context, product):
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_LINK))
    context.driver.find_element(*PRODUCT_LINK).click()
    print("Clicked on product")
    sleep(7)
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]").click()
    print("Clicked Add to Cart")
    sleep(5)

@then('Verify cart shows product')
def verify_cart_product(context):
    #sleep(5)
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="modal-drawer-heading"]')))
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="modal-drawer-heading"]').text
    assert 'Added to cart' in actual_text, f"Expected 'Added to cart' text not in {actual_text}"
    print("✓ Test passed! Product successfully added to cart.")