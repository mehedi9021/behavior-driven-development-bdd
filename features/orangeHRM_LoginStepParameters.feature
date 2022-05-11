Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given First launch chrome browser
    When Open OrangeHRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page