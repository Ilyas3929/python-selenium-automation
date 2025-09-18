Feature: Test for cart functionality


 Scenario: User can verify that on Target page if cart is empty “Your cart is empty” message is shown
    Given Open Target main page
    When Clicking on cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: "User is able to search for tea and add it to the cart"
    Given Open Target main page
    When Search for tazo strawberry matcha tea
    And Adding product to the cart
    And Clicking on cart icon
    Then Verify Tazo Strawberry Matcha Latte Sweetened Green Tea Concentrate - 32 fl oz is in the cart


  Scenario: "User is able to search for iphone"
    Given Open Target main page
    When Search for iPhone 16 Pro Silicone Case with MagSafe