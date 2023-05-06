Feature: Open the main page and navigate to a tab in mobile emulator
  # Enter feature description here

  Scenario: User can search for face wash in mobile emulator
    Given open the main page
    When User clicks on the hamburger icon
    When clicks on shop by product on the mobile
    And select Face Washes on mobile
    Then verify url contains "face-wash" is shown