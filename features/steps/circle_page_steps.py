from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CIRCLE_LINKS = (By.CSS_SELECTOR, '[class="cell-item-content"]')


@given("Open Target Circle page")
def open_main(context):
    context.driver.get("https://www.target.com/circle")

@then("Verify there are at least 10 benefit cells")
def verify_cells(context):
    context.driver.wait.until(EC.element_to_be_clickable(CIRCLE_LINKS))
    cells = context.driver.find_elements(*CIRCLE_LINKS)
    print(f"Cells {cells}")
    assert len(cells) >= 10