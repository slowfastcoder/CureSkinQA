# Created by An Tran at 4/23/2023
Feature: Users can navigate to the product page and click add to cart

  Scenario: User wants to search for cureskin cleansing gel product
    Given open the main page
    Given user searches for cleansing product
    When user clicks on Add to Cart
    And the cart side bar opens
    Then Verify that correct quantity of 1 is added

  Scenario: User wants to increment the quantity of a product in the cart by 1
    Given open the main page
    Given user searches for cleansing product
    When user clicks on Add to Cart
    And the cart side bar opens
    And the user increments the quantity by 1
    Then verify that price has doubled
    Then verify that the product quantity is set to 2