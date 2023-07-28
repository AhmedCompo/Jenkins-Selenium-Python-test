from selenium import webdriver
import chromedriver_autoinstaller

def test_google():
    # Automatically install and use the appropriate ChromeDriver version
    chromedriver_autoinstaller.install()

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()

    # Navigate to Google
    driver.get('https://www.google.com')

    # Do some tests (e.g., check the title)
    assert "Google" in driver.title

    # Clean up
    driver.quit()

if __name__ == "__main__":
    test_google()
