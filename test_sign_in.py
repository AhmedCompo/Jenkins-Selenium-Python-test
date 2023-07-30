from selenium import webdriver
options = webdriver.ChromeOptions()
options.setExperimentalOption("prefs", chromePrefs)
options.addArguments("--no-sandbox")
options.addArguments("--headless")
options.addArguments("--disable-dev-shm-usage")
options.addArguments("--window-size=1920x1080")
driver = new ChromeDriver(options);

#driver = webdriver.Chrome()

driver.get("http://www.python.org")
