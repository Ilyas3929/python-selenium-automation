Feature: Test for Target sign in form verification

  Scenario: User is able to navigate to the Sing in page when logged out
    Given Open Target main page
    When User is clicking on the Account icon
    When User is clicking on Sign in from the right side navigation menu
    Then Sign in form is openned