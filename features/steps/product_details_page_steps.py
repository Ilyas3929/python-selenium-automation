from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[class*='sc-d536ec74-1']")


@given("Open target product A-93281243 page")
def open_target(context):
    context.driver.get("https://www.target.com/p/hanes-unisex-garment-dyed-long-sleeve-cotton-t-shirt/-/A-93281243?preselect=93281261#lnk=sametab")
    sleep(2)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ["anchor slate", "black", "concrete gray", "crimson fall", "cypress green", "deep forte blue", "navy", "new railroad grey"]
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for c in colors:
        c.click()
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]
        print('Current color', selected_color)
        actual_colors.append(selected_color)
    print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'