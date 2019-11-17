Feature:  Test End to End Search functionality of registered user

@Smoke
Scenario: End to End search without purchase
Given   User is on login page
When    user enters username
And     user enters password
And     user clicks on signin button
Then    user should be logged in
And     user should get welcome message
When    user enters search data

@Sanity
Scenario: End to End search without purchase1
Given   User is on login page
When    user enters username
And     user enters password
And     user clicks on signin button
And     user should get welcome message
When    user enters search data