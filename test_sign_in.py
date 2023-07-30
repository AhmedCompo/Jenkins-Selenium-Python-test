from selenium import webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()

driver.get("http://www.python.org")
