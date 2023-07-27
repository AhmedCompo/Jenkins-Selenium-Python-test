from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://selenium.dev")

driver.quit()
