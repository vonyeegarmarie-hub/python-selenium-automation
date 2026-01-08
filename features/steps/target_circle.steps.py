from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given  ('Open target circle page')
def target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then ('Verify at least benefit cells')
def verify_benefit_cells(context):
    sleep (5)
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.mediaBlock.mediaBlock-story.mediaBlock-1x1')
    actual_count = len(benefit_cells)
    print (f'Found {actual_count} benefit cells')
    assert actual_count >=3, f"Expected at least 3 benefit cells, but found {actual_count}"