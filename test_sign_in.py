from selenium import webdriver

# Use ChromeOptions to specify the Chrome binary location
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/"  # Replace this with the actual path

# Initialize the WebDriver with Chrome driver and options
driver = webdriver.Chrome(options=chrome_options)

# Test Google.com
driver.get("https://www.google.com")

# Perform your tests here...

# Close the browser after the test is complete
driver.quit()
