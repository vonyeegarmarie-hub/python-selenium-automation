#Create a test case using BDD that opens target.com,
# clicks on the cart icon and verifies that “Your cart is empty”
# message is shown:
Feature: Verify empty cart
  # Enter feature description here

  Scenario: User verifies that “Your cart is empty”
    Given Open Target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  #Create a test case using BDD to verify that a logged
  # out user can navigate to Sign In:
 #Feature: Verify Sign in
  # Enter feature description here
  Scenario: logged out user can navigate to sign in
      Given Open Target.com
      When Click Sign In
      Then From right side navigation menu, click Sign In
      Then Verify Sign In form opened


