Feature: Adding a contact via an Android App

  Scenario Outline: Add a Contact
    Given we are on a "<device_name>" device
      And I click on the add contact button
    When I enter a name and email
    Then I click the Save button

    Examples: Devices
      | device_name                |
      | Android Emulator           | 
      | Samsung Galaxy S4 Emulator |


