Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given Launch chrome browser
    When Open OrangeHRM  homepage
    Then Verify that the logo present on page
    And Close browser