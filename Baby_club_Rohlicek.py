from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import time

# Initialize WebDriver
options = Options()
driver = webdriver.Firefox(service=FirefoxService(executable_path="C:/Python39/Scripts/geckodriver.exe"),
                           options=options)


def test_cancel_baby_club_membership():

    # Step 1: Open www.rohlik.cz and log in
    driver.get("https://www.rohlik.cz")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Click on the account icon to open login form
    account_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='header-user-icon']")))
    account_icon.click()

    # Enter email and password
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys("test_rohlicek@yopmail.com")

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("Pass_123!")

    # Click "Přihlásit se" button
    login_button = driver.find_element(By.XPATH, "//button[@data-test='btnSignIn']")
    login_button.click()

    # Wait for login to complete
    time.sleep(3)

    # Step 2: Navigate to the Baby Club Rohlíček profile page
    driver.get("https://www.rohlik.cz/rohlicek/profil")

    # Step 3: Locate the "Zrušit členství v dětském klubu Rohlíček" option and click
    cancel_membership_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Zrušit členství v dětském klubu Rohlíček')]")))
    cancel_membership_option.click()

    # Step 4: Confirm cancellation in the pop-up
    cancel_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zrušit členství')]"))
    )
    cancel_button.click()

    # Step 5: Check if the "Rohlíček" label is gone from the profile page
    driver.get("https://www.rohlik.cz/uzivatel/profil")

    # Wait for the page to fully load
    time.sleep(5)

    try:
        membership_label = driver.find_elements(By.XPATH, "//span[contains(@class, 'parentsClubLabel')]")

        if membership_label:
            print("Membership still active! 'Rohlíček' label is visible on profile.")
            assert False
        else:
            print("Membership label removed. Cancellation successful!")

    finally:
        # Step 7: Close the browser
        driver.quit()


if __name__ == "__main__":
    test_cancel_baby_club_membership()