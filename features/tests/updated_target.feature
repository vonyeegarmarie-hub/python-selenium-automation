Feature: Tests for search

  Scenario: User can search for a mango on Target
    Given Open target main page
    When Search for mango
    Then Product results for mango are shown