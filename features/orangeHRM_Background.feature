Feature: orangeHRM Login

  Background: common step
    Given Launched browser
    When Opened application
    And Entered valid username and password
    And Clicked login

    Scenario: Login to orangeHRM application
      Then Users need to login into the dashboard page

    Scenario: Leave list checking
      When Check the leave list
      Then Log out after checking the leave list

    Scenario: Timesheets checking
      When Check the timesheets
      Then Log out after checking the timesheets
