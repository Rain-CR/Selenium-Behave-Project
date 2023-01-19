Feature: Form Page
Scenario: Verify error
    Given I am on the Jules App-sign-in
    When  I input correct email
    And I write a password
    And I clear the password
    Then Message error is displayed
    And Log in button is disabled