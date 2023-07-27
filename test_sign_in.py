from selenium import webdriver
import chromedriver_autoinstaller


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
