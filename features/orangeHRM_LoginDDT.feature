Feature: OrangeHRM Login

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given First need to launch chrome browser
    When Open the OrangeHRM homepage
    And Enter the username "<username>" and password "<password>"
    And Click on the login button
    Then User must successfully login to dashboard page

    Examples:
    | username | password |
    | admin    | admin123 |
    | admin123 | admin    |
    | adminxyz | admin123 |
    | admin    | adminxyz |
