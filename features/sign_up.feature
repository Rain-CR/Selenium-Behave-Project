Feature: Complete signup
  Scenario Outline: Try sign up with wrong/correct email format
    Given I am on the Jules App-sign-in
    When  I click "Sign up." link
    And  I click personal
    And I click continue
    And I input  the first name field
    And I click continue button
    And I input correct last name
    And I click continue button
    And I enter "{email}" in the email field
    Then A message with text "{text}" is displayed
    Then I verify the "Please enter a valid email address." is <status>

  Examples: Credentials
    | email   | status |
    | something  | displayed  |
    | something@something.com  |not displayed|