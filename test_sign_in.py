from selenium import webdriver
options = new ChromeOptions();
options.setExperimentalOption("prefs", chromePrefs);
options.addArguments("--no-sandbox");
options.addArguments("--headless"); //!!!should be enabled for Jenkins
options.addArguments("--disable-dev-shm-usage"); //!!!should be enabled for Jenkins
options.addArguments("--window-size=1920x1080"); //!!!should be enabled for Jenkins
driver = new ChromeDriver(options);

#driver = webdriver.Chrome()

driver.get("http://www.python.org")
