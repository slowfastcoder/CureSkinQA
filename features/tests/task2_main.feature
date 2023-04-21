Feature: User can shop by product Face Washes

  Scenario: User wants to search for face wash
    Given open the main page
    When click on shop by product
    And select Face Wash
    Then verify that "Face Washes" is shown