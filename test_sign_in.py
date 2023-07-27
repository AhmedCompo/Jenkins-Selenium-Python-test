from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

driver.get("http://selenium.dev")

driver.quit()
