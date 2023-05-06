# Created by An Tran at 4/27/2023
Feature: User can add a product to the cart and remove the product to 0


  Scenario: User can add a product and remove the product from the cart
     Given open the main page
     When user clicks on the search icon via mobile
     Given user searches for sun product
     When user clicks on Add to Cart
     And the cart side bar opens
     And user reduces the quantity to 0
     Then verify that the cart is empty