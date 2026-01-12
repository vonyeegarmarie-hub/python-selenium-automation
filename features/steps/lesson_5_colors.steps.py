from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-94637797 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/toddler-boys-long-sleeve-graphic-t-shirt-cat-jack/-/A-94637797?preselect=94712905')
    sleep(4)

@then ('Verify user can click through colors')
def verify_colors(context):
    expected_colors =['Off-White','Gray', 'Green', 'Dusty Blue']
    actual_colors =[]

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    sleep(6)
    for c in colors[:4]:
        c.click()
        sleep(5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'