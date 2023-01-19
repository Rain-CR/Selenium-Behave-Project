Feature: Complete signup
  Scenario Outline: Try sign up with wrong/correct email format
    Given I am on the Jules App-sign-in
    When  I click "Sign up." link
    And  I click personal value
    And I click continue button
    And I input correct first name
    And I click continue button
    And I input correct last name
    And I click continue button
    And I input "<email>"
    Then I verify the "Please enter a valid email address." is <status>

  Examples: Credentials
    | email   | status |
    | something  | displayed  |
    | something@something.com  |not displayed|