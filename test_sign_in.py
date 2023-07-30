from selenium import webdriver
options = webdriver.ChromeOptions()
options.addArguments("--headless")
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()

driver.get("http://www.python.org")
