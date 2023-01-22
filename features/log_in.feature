Feature: Form Page
Scenario: Verify error
    Given I am on the Jules App-sign-in
    When  I input correct email
    And I write a password
    And I delete the password
    Then Log in button id disabled