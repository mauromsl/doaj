Feature: Applying for inclusion in DOAJ

  Scenario: Go to the public application form
    When I visit the public application page
    Then I see the public application form

  Scenario: Apply for the DOAJ using the public form
    When I submit the public application form
    Then The correct suggestion should have been saved
