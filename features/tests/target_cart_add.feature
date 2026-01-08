# Created by kroum at 1/6/2026
Feature: add product to cart

  Scenario: user adds product to target cart
    Given Open target main page
     When Search for notebook wide ruled
     Then Search results for notebook wide are shown
     Then Add product to cart
     Then Verify cart shows product