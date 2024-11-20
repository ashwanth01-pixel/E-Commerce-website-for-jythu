from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_homepage():
    # Set up the WebDriver (Assuming ChromeDriver is installed)
    driver = webdriver.Chrome()

    try:
        # Navigate to the application
        driver.get("http://localhost:5000/")  # Change to the correct URL if deployed
        time.sleep(2)  # Wait for page to load

        # Find element and validate the page
        element = driver.find_element(By.TAG_NAME, "body")
        assert "Hello, World!" in element.text

        print("Test Passed!")
    except Exception as e:
        print(f"Test Failed: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_homepage()
