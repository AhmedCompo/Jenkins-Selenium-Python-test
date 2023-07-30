from selenium import webdriver
options = webdriver.ChromeOptions()
options.addArguments("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()

driver.get("http://www.python.org")
