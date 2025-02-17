# Automate Test Case for Baby Club Rohlíček

## Description

This automated test performs the cancellation of a Rohlíček Baby Club membership on the [rohlik.cz](https://www.rohlik.cz) website. The test includes the following steps:

### Test Steps:

1. Logging into the website  
2. Navigating to the Rohlíček profile page  
3. Clicking the **"Zrušit členství v dětském klubu Rohlíček"** button  
4. Confirming the cancellation  
5. Verifying that the membership is successfully removed  

## Requirements

Before running the test, ensure that you have the following installed:

- **Python 3.9 or higher**
- **Selenium** (Install using: `pip install selenium`)
- **Geckodriver** (Required for Firefox WebDriver)

## Running the Test

To execute the test, follow these steps:

1. Save the test script as `baby_club_rohlicek.py`.
2. Open a command prompt and run the script:

   python baby_club_rohlicek.py

The Firefox browser will open automatically, execute the test, and close upon completion.