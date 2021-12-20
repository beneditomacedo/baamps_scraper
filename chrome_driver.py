from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/usr/local/bin/chromedriver'


def get_driver(driver_path=DRIVER_PATH):
    options = Options()
    options.headless = True
    options.add_argument("--windows-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    return driver
