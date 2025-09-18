Feature: Test for Target cart verification

  Scenario: User can verify that on Target page if cart is empty “Your cart is empty” message is shown
    Given Open Target main page
    When Cart is empty
    Then Verify “Your cart is empty” message is shown
