import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Library import ConfigReader


def test_Login():
    global driver
    if(ConfigReader.readConfigData('Data','Browser'))=='Chrome':
        options = Options()
        options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        path = "../Drivers/chromedriver.exe"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = Chrome(options=options,executable_path=path)

    # driver.get("https://www.google.com")
    elif (ConfigReader.readConfigData('Data', 'Browser')) == 'Firefox':
        driver = webdriver.Firefox()
    driver.get(ConfigReader.readConfigData('Data','Application_url'))



    def close_browser():
        driver.quite()




